import unittest
from convert_payload import parse_payload, convert, parse_ducky_strings


def testline(i, n, data='p=window.p||[],p[0]=`abc`'):
    return f'{i}/{n}"></div><img src=x onerror="{data}"><div class="'

class PortTests(unittest.TestCase):
    def test_ascii_round_trip_and_order(self):
        sample = [testline(1,2), testline(2,2,'d=window.d||[],d[0]=`#%!()+,-.:;=>?@[]^_{|}~`')]
        src = ("\n".join(sample) + "\n").encode('ascii')
        lines = parse_payload(src)
        script = convert(lines)
        self.assertEqual(parse_ducky_strings(script), lines)
        self.assertEqual(script.splitlines().count('ESC'),2)
        self.assertEqual(script.splitlines().count('ENTER'),4)
        self.assertEqual(script.splitlines().count('WAIT_FOR_BUTTON_PRESS'),4)

    def test_254_byte_exact_limit(self):
        prefix = '1/1"></div><img src=x onerror="p=window.p||[],p[0]=`'
        suffix = '`"><div class="'
        max_data = 253 - len(prefix) - len(suffix)
        valid = prefix + ('z' * max_data) + suffix
        self.assertEqual(len(valid)+1,254)
        self.assertEqual(parse_payload((valid+'\n').encode()), [valid])
        with self.assertRaisesRegex(ValueError, '254-byte'):
            parse_payload((prefix+'z'*(max_data+1)+suffix+'\n').encode())

    def test_bad_indexes_and_non_ascii(self):
        with self.assertRaisesRegex(ValueError,'prefix'):
            parse_payload(testline(2,2).encode())
        with self.assertRaisesRegex(ValueError,'ASCII'):
            parse_payload(('1/1"è\n').encode('utf-8'))

    def test_both_line_endings(self):
        a, b = testline(1,2), testline(2,2)
        self.assertEqual(parse_payload((a+'\r\n'+b+'\r\n').encode()),[a,b])

    def test_large_realistic_payload_shape(self):
        # Compare all 87 synthetic upstream messages and every transport symbol.
        n = 87
        charset = '#%!()+,-.:;=>?@[]^_{|}~01'
        generated = [testline(i, n, f'p=window.p||[],p[{i}]=`{charset}`') for i in range(1, n+1)]
        lines = parse_payload(('\n'.join(generated) + '\n').encode('ascii'))
        script = convert(lines, delay=60)
        self.assertEqual(parse_ducky_strings(script), lines)
        self.assertEqual(script.splitlines().count('WAIT_FOR_BUTTON_PRESS'), 2*n)
        self.assertEqual(script.splitlines().count('ESC'), n)
        self.assertEqual(script.splitlines().count('ENTER'), 2*n)
        self.assertEqual(script.count('DEFAULT_STRING_DELAY 60'), 1)

    def test_reject_trailing_blanks_and_delays(self):
        with self.assertRaisesRegex(ValueError, 'whitespace'):
            parse_payload((testline(1,1)+'  \n').encode())
        with self.assertRaises(ValueError):
            convert([testline(1,1)], delay=0)

    def test_example_is_in_sync_with_converter(self):
        from pathlib import Path
        here = Path(__file__).resolve().parent
        payload = parse_payload((here / 'example_synthetic_payload.txt').read_bytes())
        expected = (here / 'example_generated_badusb.txt').read_text(encoding='ascii')
        self.assertEqual(convert(payload), expected)

    def test_only_supported_control_commands_are_emitted(self):
        # Static output-shape validation, not an interpreter or hardware test.
        items = [testline(1, 2), testline(2, 2)]
        script = convert(items)
        allowed = {'REM', 'DEFAULT_STRING_DELAY', 'WAIT_FOR_BUTTON_PRESS',
                   'ESC', 'DELAY', 'STRING', 'ENTER'}
        for cmd in script.splitlines():
            self.assertIn(cmd.split(' ', 1)[0], allowed)
        self.assertEqual(script.splitlines().count('WAIT_FOR_BUTTON_PRESS'), 4)
        self.assertEqual(script.splitlines().count('ESC'), 2)
        self.assertEqual(script.splitlines().count('ENTER'), 4)

if __name__ == '__main__': unittest.main()
