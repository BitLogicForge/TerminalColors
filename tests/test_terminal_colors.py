from terminal_colors import TerminalColors
import unittest


class TestTerminalColors(unittest.TestCase):
    def setUp(self):
        self.tc = TerminalColors(auto_reset=True)

    def test_basic_colors(self):
        self.assertIn("\033[31m", self.tc.red("test"))
        self.assertIn("\033[32m", self.tc.green("test"))
        self.assertIn("\033[34m", self.tc.blue("test"))

    def test_bright_colors(self):
        self.assertIn("\033[91m", self.tc.red("test", bright=True))
        self.assertIn("\033[92m", self.tc.green("test", bright=True))

    def test_background_colors(self):
        self.assertIn("\033[37;41m", self.tc.white("test", bg="red"))
        self.assertIn("\033[30;43m", self.tc.black("test", bg="yellow"))

    def test_styles(self):
        self.assertIn("\033[1m", self.tc.bold("test"))
        self.assertIn("\033[3m", self.tc.italic("test"))
        self.assertIn("\033[4m", self.tc.underline("test"))

    def test_rgb(self):
        result = self.tc.rgb("test", 128, 0, 128)
        self.assertIn("\033[38;2;128;0;128m", result)

    def test_256_color(self):
        result = self.tc.color256("test", 202)
        self.assertIn("\033[38;5;202m", result)

    def test_strip_colors(self):
        colored = self.tc.red("test")
        plain = self.tc.strip_colors(colored)
        self.assertEqual(plain, "test")

    def test_nested_colors(self):
        nested = self.tc.red(f"red {self.tc.blue('blue')}")
        self.assertIn("\033[31m", nested)
        self.assertIn("\033[34m", nested)

    def test_invalid_color(self):
        with self.assertRaises(ValueError):
            self.tc.red("test", bg="notacolor")
        with self.assertRaises(ValueError):
            self.tc.color256("test", 300)
        with self.assertRaises(ValueError):
            self.tc.rgb("test", 300, 0, 0)

    def test_invalid_style(self):
        with self.assertRaises(ValueError):
            self.tc.colorize("test", "red", "notastyle")


if __name__ == "__main__":

    unittest.main()
