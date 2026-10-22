import unittest,tempfile
from pathlib import Path
from term_colors import rgb,hex_color,palette
class ColorsTests(unittest.TestCase):
    def test_roundtrip(self): self.assertEqual(hex_color(rgb('#Aa00FF')),'#aa00ff')
    def test_bounds(self):
        with self.assertRaises(ValueError): hex_color([256,0,0])
    def test_invalid(self):
        with self.assertRaises(ValueError): rgb('#123')
    def test_builtin(self): self.assertEqual(len(palette('moss')),4)
    def test_custom(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'colors.json';p.write_text('["#123456"]')
            self.assertEqual(palette('',p),['#123456'])
    def test_missing(self):
        with self.assertRaises(ValueError): palette('missing')
