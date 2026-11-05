import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from build_from_upstream import build, PINNED_REVISION, validate_checkout


def line(i: int, n: int) -> str:
    return f'{i}/{n}"></div><img src=x onerror="p=window.p||[],p[{i}]=`#%!()+,-.:;=>?@[]^_{{|}}~`"><div class="'


class BuildIntegrationTests(unittest.TestCase):
    def fake_checkout(self, root: Path) -> Path:
        src = root / "CivSwitch"
        pico = src / "PicoSwitch"
        (pico / "tools").mkdir(parents=True)
        for filename in (src / "core.js", pico / "compress.js", pico / "package.json", pico / "tools" / "payload_to_macro.py"):
            filename.write_text("synthetic-data", encoding="utf-8")
        return src

    def test_manifest_generation_with_synthetic_upstream(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            src = self.fake_checkout(root)
            def fake_run(args, cwd=None):
                if args[:2] == ["git", "rev-parse"]:
                    return PINNED_REVISION + "\n"
                if args[:2] == ["node", "compress.js"]:
                    (src / "PicoSwitch" / "payload.txt").write_text(
                        "\n".join(line(i, 3) for i in range(1, 4)) + "\n", encoding="ascii")
                return "mock command output"
            with patch("build_from_upstream.run", side_effect=fake_run):
                m = build(src, root / "out", PINNED_REVISION, 40)
            self.assertEqual(m["message_count"], 3)
            self.assertEqual(m["controller_a_manual_presses"], 10)
            self.assertEqual(m["flipper_resume_prompts"], 6)
            self.assertTrue(m["all_strings_byte_preserved"])
            self.assertEqual(m["source_revision"], PINNED_REVISION)
            self.assertEqual(json.loads((root / "out" / "build_manifest.json").read_text())["message_count"], 3)
            self.assertEqual((root / "out" / "upstream_payload.txt").read_bytes().count(b"\n"), 3)

    def test_revision_mismatch_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            src = self.fake_checkout(Path(td))
            with patch("build_from_upstream.run", return_value="f" * 40):
                with self.assertRaisesRegex(RuntimeError, "Wrong CivSwitch revision"):
                    validate_checkout(src, PINNED_REVISION)


if __name__ == "__main__":
    unittest.main()
