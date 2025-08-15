"""
Terminal color utility for easy text colorization with ANSI escape codes.
Supports 8/16 colors, 256 colors, RGB colors, background colors, and text styles.
"""

import re
from .constants import ColorType, Color, Style

from typing import Optional, Union


class TerminalColors:
    """A comprehensive terminal color utility with support for various color modes and styles."""

    # ANSI Reset
    RESET = "\033[0m"

    # Compiled regex for stripping ANSI codes
    _ANSI_REGEX = re.compile(r"\033\[[0-9;]*m")

    def __init__(self, auto_reset: bool = True):
        """
        Initialize TerminalColors.

        Args:
            auto_reset: Whether to automatically add reset codes after colored text
        """
        self.auto_reset = auto_reset

    def _format_text(self, text: str, *codes: int) -> str:
        """Apply ANSI codes to text with optional auto-reset."""
        if not codes:
            return str(text)

        # Remove existing reset codes and replace with our codes to handle nesting
        clean_text = str(text)
        if self.RESET in clean_text:
            # Replace resets with our codes to maintain color in nested scenarios
            code_str = ";".join(map(str, codes))
            clean_text = clean_text.replace(self.RESET, f"\033[{code_str}m")

        code_str = ";".join(map(str, codes))
        formatted = f"\033[{code_str}m{clean_text}"

        return formatted + self.RESET if self.auto_reset else formatted

    def _parse_color(self, color: ColorType, bright: bool = False, bg: bool = False) -> list[int]:
        """Parse color input into ANSI codes."""
        codes = []

        if isinstance(color, (Color.Normal, Color.Bright)):
            code = color.value
            if bg:
                code += 10
            codes.append(code)
        elif isinstance(color, str):
            # Handle string color names
            try:
                if bright:
                    code = getattr(Color.Bright, color.upper()).value
                else:
                    code = getattr(Color.Normal, color.upper()).value
                if bg:
                    code += 10
                codes.append(code)
            except AttributeError:
                raise ValueError(f"Unknown color: {color}")
        elif isinstance(color, int):
            # 256-color mode
            if not 0 <= color <= 255:
                raise ValueError("Color code must be between 0 and 255")
            base_code = 48 if bg else 38
            codes.extend([base_code, 5, color])
        elif isinstance(color, tuple) and len(color) == 3:
            # RGB color
            r, g, b = color
            if not all(0 <= val <= 255 for val in (r, g, b)):
                raise ValueError("RGB values must be between 0 and 255")
            base_code = 48 if bg else 38
            codes.extend([base_code, 2, r, g, b])
        else:
            raise TypeError("color must be a Color enum, str, int (0-255), or RGB tuple")

        return codes

    def colorize(
        self,
        text: str,
        fg: Optional[ColorType] = None,
        bg: Optional[ColorType] = None,
        bright: bool = False,
        *styles: Union[Style, str],
    ) -> str:
        """
        Apply colors and styles to text.

        Args:
            text: Text to colorize
            fg: Foreground color
            bg: Background color
            bright: Use bright variant for enum colors
            styles: Text styles to apply

        Returns:
            Formatted text with ANSI codes
        """
        codes = []

        # Add foreground color
        if fg is not None:
            codes.extend(self._parse_color(fg, bright=bright, bg=False))

        # Add background color
        if bg is not None:
            codes.extend(self._parse_color(bg, bright=bright, bg=True))

        # Add styles
        for style in styles:
            if isinstance(style, Style):
                codes.append(style.value)
            elif isinstance(style, str):
                try:
                    codes.append(getattr(Style, style.upper()).value)
                except AttributeError:
                    raise ValueError(f"Unknown style: {style}")
            else:
                raise TypeError("style must be a Style enum or str")

        return self._format_text(text, *codes)

    # Convenience methods for common operations
    def red(self, text: str, bright: bool = False, bg: Optional[ColorType] = None) -> str:
        """Apply red color to text."""
        return self.colorize(text, fg=Color.Bright.RED if bright else Color.Normal.RED, bg=bg)

    def green(self, text: str, bright: bool = False, bg: Optional[ColorType] = None) -> str:
        """Apply green color to text."""
        return self.colorize(text, fg=Color.Bright.GREEN if bright else Color.Normal.GREEN, bg=bg)

    def blue(self, text: str, bright: bool = False, bg: Optional[ColorType] = None) -> str:
        """Apply blue color to text."""
        return self.colorize(text, fg=Color.Bright.BLUE if bright else Color.Normal.BLUE, bg=bg)

    def yellow(self, text: str, bright: bool = False, bg: Optional[ColorType] = None) -> str:
        """Apply yellow color to text."""
        return self.colorize(text, fg=Color.Bright.YELLOW if bright else Color.Normal.YELLOW, bg=bg)

    def magenta(self, text: str, bright: bool = False, bg: Optional[ColorType] = None) -> str:
        """Apply magenta color to text."""
        return self.colorize(
            text, fg=Color.Bright.MAGENTA if bright else Color.Normal.MAGENTA, bg=bg
        )

    def cyan(self, text: str, bright: bool = False, bg: Optional[ColorType] = None) -> str:
        """Apply cyan color to text."""
        return self.colorize(text, fg=Color.Bright.CYAN if bright else Color.Normal.CYAN, bg=bg)

    def white(self, text: str, bright: bool = False, bg: Optional[ColorType] = None) -> str:
        """Apply white color to text."""
        return self.colorize(text, fg=Color.Bright.WHITE if bright else Color.Normal.WHITE, bg=bg)

    def black(self, text: str, bright: bool = False, bg: Optional[ColorType] = None) -> str:
        """Apply black color to text."""
        return self.colorize(text, fg=Color.Bright.BLACK if bright else Color.Normal.BLACK, bg=bg)

    def bold(self, text: str) -> str:
        """Apply bold style to text."""
        return self.colorize(text, None, None, False, Style.BOLD)

    def italic(self, text: str) -> str:
        """Apply italic style to text."""
        return self.colorize(text, None, None, False, Style.ITALIC)

    def underline(self, text: str) -> str:
        """Apply underline style to text."""
        return self.colorize(text, None, None, False, Style.UNDERLINE)

    def rgb(self, text: str, r: int, g: int, b: int) -> str:
        """Apply RGB color to text (24-bit color)."""
        return self.colorize(text, fg=(r, g, b))

    def color256(self, text: str, color_code: int) -> str:
        """Apply 256-color palette color to text."""
        return self.colorize(text, fg=color_code)

    def strip_colors(self, text: str) -> str:
        """Remove all ANSI escape codes from text."""
        return self._ANSI_REGEX.sub("", str(text))
