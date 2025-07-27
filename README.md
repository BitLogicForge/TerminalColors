# TerminalColors

A comprehensive Python utility for colorizing terminal output using ANSI escape codes. Supports standard, bright, 256-color, and RGB color modes, as well as background colors and text styles.

## Features

- 8/16 standard and bright colors
- 256-color palette support
- True RGB (24-bit) color support
- Background color support
- Text styles: bold, dim, italic, underline, blink, reverse, strikethrough
- Automatic reset of colors/styles
- Strip ANSI codes from text
- Easy-to-use convenience methods

## Installation

No external dependencies required. Just copy the files into your project.

## Usage

```python
from terminal_colors import TerminalColors

tc = TerminalColors(auto_reset=True)

# Basic colors
print(tc.red('Red text'))
print(tc.green('Green text'))
print(tc.blue('Blue text'))
print(tc.yellow('Yellow'))
print(tc.magenta('Magenta'))
print(tc.cyan('Cyan'))

# Bright colors
print(tc.red('Bright Red', bright=True))
print(tc.green('Bright Green', bright=True))

# Background colors
print(tc.white('White on Red', bg='red'))
print(tc.black('Black on Yellow', bg='yellow'))

# Styles
print(tc.bold('Bold'))
print(tc.italic('Italic'))
print(tc.underline('Underlined'))

# Combined styles and colors
print(tc.bold(tc.red('Bold Red Text')))

# RGB colors (if terminal supports it)
print(tc.rgb('Custom Pink', 255, 192, 203))

# 256 colors (if terminal supports it)
print(tc.color256('Orange-ish', 208))

# Nested colors
nested = tc.red(f"Red text with {tc.blue('blue')} and {tc.green('green')} inside")
print(nested)

# Strip colors
colored = tc.red('Colored text')
print(f"Original: {colored}")
print(f"Stripped: {tc.strip_colors(colored)}")
```

## API Reference

### TerminalColors

- `colorize(text, fg=None, bg=None, bright=False, *styles)`
- `red(text, bright=False, bg=None)`
- `green(text, bright=False, bg=None)`
- `blue(text, bright=False, bg=None)`
- `yellow(text, bright=False, bg=None)`
- `magenta(text, bright=False, bg=None)`
- `cyan(text, bright=False, bg=None)`
- `white(text, bright=False, bg=None)`
- `black(text, bright=False, bg=None)`
- `bold(text)`
- `italic(text)`
- `underline(text)`
- `rgb(text, r, g, b)`
- `color256(text, color_code)`
- `strip_colors(text)`

### Color and Style Enums

See `constants.py` for available color and style enums.

## License

MIT
