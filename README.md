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

color = TerminalColors()

print(color.red("Red text"))
print(color.green("Green text", bright=True))
print(color.rgb("Custom RGB", 128, 0, 128))
print(color.color256("256-color", 202))
print(color.bold("Bold text"))
print(color.underline("Underlined text"))
print(color.colorize("Styled text", fg="blue", bg="yellow", bright=True, Style.BOLD, Style.UNDERLINE))

# Remove colors from a string
plain = color.strip_colors("\033[31mRed\033[0m")
print(plain)
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
