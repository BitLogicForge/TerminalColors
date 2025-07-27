from terminal_colors import TerminalColors

if __name__ == "__main__":
    print("=== Terminal Colors Demo ===\n")
    colors = TerminalColors(auto_reset=True)

    # Basic colors
    print("Basic Colors:")
    print(f"{colors.red('Red text')} | {colors.green('Green text')} | {colors.blue('Blue text')}")
    print(f"{colors.yellow('Yellow')} | {colors.magenta('Magenta')} | {colors.cyan('Cyan')}")

    # Bright colors
    print("\nBright Colors:")
    print(f"{colors.red('Bright Red', bright=True)} | {colors.green('Bright Green', bright=True)}")

    # Background colors
    print("\nBackground Colors:")
    print(f"{colors.white('White on Red')} ")
    print(f"{colors.black('Black on Yellow')}")

    # Styles
    print("\nText Styles:")
    print(f"{colors.bold('Bold')} | {colors.italic('Italic')} | {colors.underline('Underlined')}")

    # Combined styles and colors
    print(f"\nCombined: {colors.bold(colors.red('Bold Red Text'))}")

    # RGB colors (if terminal supports it)
    print(f"\nRGB Colors: {colors.rgb('Custom Pink', 255, 192, 203)}")

    # 256 colors (if terminal supports it)
    print(f"256 Color: {colors.color256('Orange-ish', 208)}")

    # Nested colors
    nested = colors.red(f"Red text with {colors.blue('blue')} and {colors.green('green')} inside")
    print(f"\nNested Colors: {nested}")

    # Strip colors
    print(f"\nOriginal: {colors.red('Colored text')}")
    print(f"Stripped: {colors.strip_colors(colors.red('Colored text'))}")
