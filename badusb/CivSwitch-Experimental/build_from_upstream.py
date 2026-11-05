#!/usr/bin/env python3
"""Build and statically validate a source-pinned CivSwitch -> Flipper BadUSB port.

This is a build tool, not a Switch exploit runner. It does not communicate
with the console, modify firmware, or claim hardware compatibility.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

from convert_payload import convert, parse_ducky_strings, parse_payload

ORIGINAL_REPO = "https://github.com/Gezine/CivSwitch.git"
# Verified against the canonical GitHub repository on 2026-11-05.
PINNED_REVISION = "45649ae585c7df27a99ba378822ff5b1c124539c"


def run(argv: list[str], cwd: Path | None = None) -> str:
    proc = subprocess.run(
        argv, cwd=cwd, encoding="utf-8", errors="replace", text=True,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT, check=False,
    )
    if proc.returncode:
        raise RuntimeError(
            f"Command failed ({proc.returncode}): {' '.join(argv)}\n{proc.stdout[-4000:]}"
        )
    return proc.stdout


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def validate_checkout(source: Path, revision: str) -> None:
    needed = [
        source / "core.js",
        source / "PicoSwitch" / "compress.js",
        source / "PicoSwitch" / "package.json",
        source / "PicoSwitch" / "tools" / "payload_to_macro.py",
    ]
    for file in needed:
        if not file.is_file():
            raise FileNotFoundError(f"Missing CivSwitch upstream file: {file}")
    actual = run(["git", "rev-parse", "HEAD"], cwd=source).strip()
    if actual != revision:
        raise RuntimeError(f"Wrong CivSwitch revision: {actual}; expected {revision}")


def build(source: Path, output: Path, revision: str, delay: int) -> dict:
    validate_checkout(source, revision)
    pico = source / "PicoSwitch"
    run(["node", "--check", "core.js"], cwd=source)
    run(["npm", "install", "--ignore-scripts", "--no-audit", "--no-fund"], cwd=pico)
    log = run(["node", "compress.js"], cwd=pico)
    payload = pico / "payload.txt"
    lines = parse_payload(payload.read_bytes())
    script = convert(lines, delay)
    if parse_ducky_strings(script) != lines:
        raise AssertionError("DuckyScript STRING content differs from upstream payload")

    output.mkdir(parents=True, exist_ok=True)
    payload_dest = output / "upstream_payload.txt"
    ducky_dest = output / "CivSwitch_Flipper_Experimental.txt"
    shutil.copyfile(payload, payload_dest)
    ducky_dest.write_text(script, encoding="ascii", newline="\n")
    n = len(lines)
    sizes = [len(v.encode("ascii")) for v in lines]
    manifest = {
        "result": "STATIC_VALIDATION_ONLY",
        "hardware_tested": False,
        "console_exploit_verified": False,
        "source": ORIGINAL_REPO,
        "source_revision": revision,
        "upstream_core_sha256": sha256(source / "core.js"),
        "upstream_compress_sha256": sha256(pico / "compress.js"),
        "upstream_macro_generator_sha256": sha256(pico / "tools" / "payload_to_macro.py"),
        "upstream_payload_sha256": sha256(payload_dest),
        "flipper_script_sha256": sha256(ducky_dest),
        "message_count": n,
        "longest_message_bytes": max(sizes),
        "shortest_message_bytes": min(sizes),
        "total_message_bytes": sum(sizes),
        "numbered_messages_valid": True,
        "all_strings_byte_preserved": True,
        "esc_commands": n,
        "enter_commands": 2 * n,
        "controller_a_manual_presses": 2 * n + 4,
        "flipper_resume_prompts": 2 * n,
        "keyboard_delay_ms": delay,
        "build_log": log.strip(),
        "cautions": [
            "Composite keyboard+Nintendo gamepad HID is not reproduced.",
            "Manual sync and keyboard mapping must be tested on hardware.",
            "JavaScript exploit execution, compatibility, and persistence were not tested.",
        ],
    }
    (output / "build_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path,
        help="Existing local CivSwitch git checkout at --revision; skips cloning")
    parser.add_argument("--output", type=Path, default=Path("generated"))
    parser.add_argument("--revision", default=PINNED_REVISION,
        help="Exact full Git SHA to pin and validate")
    parser.add_argument("--string-delay", type=int, default=40)
    args = parser.parse_args()
    if not 20 <= args.string_delay <= 500:
        parser.error("--string-delay must be 20..500 milliseconds")
    if len(args.revision) != 40 or any(c not in "0123456789abcdef" for c in args.revision):
        parser.error("--revision must be a complete lowercase 40-character Git commit SHA")

    if args.source:
        manifest = build(args.source.resolve(), args.output.resolve(), args.revision, args.string_delay)
    else:
        with tempfile.TemporaryDirectory(prefix="civswitch-pinned-") as temp:
            source = Path(temp) / "CivSwitch"
            run(["git", "clone", ORIGINAL_REPO, str(source)])
            run(["git", "checkout", "--detach", args.revision], cwd=source)
            manifest = build(source, args.output.resolve(), args.revision, args.string_delay)

    print(f"Source pinned: {manifest['source_revision']}")
    print(f"Generated messages: {manifest['message_count']}")
    print(f"Payload SHA256: {manifest['upstream_payload_sha256']}")
    print(f"Ducky SHA256:   {manifest['flipper_script_sha256']}")
    print(f"Manual A presses: {manifest['controller_a_manual_presses']}")
    print(f"Flipper resumes:  {manifest['flipper_resume_prompts']}")
    print("STATIC VALIDATION PASSED. NO CONSOLE / FLIPPER COMPATIBILITY CLAIM.")


if __name__ == "__main__":
    main()
