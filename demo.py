from terminal_colors import TerminalColors

if __name__ == "__main__":
    print("=== Terminal Colors Demo ===\n")
    tc = TerminalColors(auto_reset=True)

    # Basic colors
    print("Basic Colors:")
    print(f"{tc.red('Red text')} | {tc.green('Green text')} | {tc.blue('Blue text')}")
    print(f"{tc.yellow('Yellow')} | {tc.magenta('Magenta')} | {tc.cyan('Cyan')}")

    # Bright colors
    print("\nBright Colors:")
    print(f"{tc.red('Bright Red', bright=True)} | {tc.green('Bright Green', bright=True)}")

    # Background colors
    print("\nBackground Colors:")
    print(tc.white("White on Red", bg="red"))
    print(tc.black("Black on Yellow", bg="yellow"))

    # Styles
    print("\nText Styles:")
    print(f"{tc.bold('Bold')} | {tc.italic('Italic')} | {tc.underline('Underlined')}")

    # Combined styles and colors
    print(f"\nCombined: {tc.bold(tc.red('Bold Red Text'))}")

    # RGB colors (if terminal supports it)
    print(f"\nRGB Colors: {tc.rgb('Custom Pink', 255, 192, 203)}")

    # 256 colors (if terminal supports it)
    print(f"256 Color: {tc.color256('Orange-ish', 208)}")

    # Nested colors
    nested = tc.red(f"Red text with {tc.blue('blue')} and {tc.green('green')} inside")
    print(f"\nNested Colors: {nested}")

    # Strip colors
    print(f"\nOriginal: {tc.red('Colored text')}")
    print(f"Stripped: {tc.strip_colors(tc.red('Colored text'))}")
