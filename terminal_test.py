def supports_ansi():
    print("Testing ANSI support:\n")
    print("\033[31mRed\033[0m \033[32mGreen\033[0m \033[34mBlue\033[0m")
    print("\033[1mBold\033[0m \033[4mUnderline\033[0m \033[7mInverse\033[0m")
    print("✅ ANSI escape codes seem to work (if you saw color & styles above).")

def show_truecolor_gradient():
    print("\nTesting 24-bit True Color (RGB) Gradient:\n")
    for i in range(0, 256, 4):
        r = 255 - i
        g = i
        b = 128
        print(f"\033[48;2;{r};{g};{b}m ", end="")
    print("\033[0m\n")

def main():
    print("🎨 Terminal Compatibility Test\n")
    supports_ansi()
    show_truecolor_gradient()
    print("If you saw a smooth color gradient bar above, ✅ your terminal supports 24-bit True Color.")
    print("If it looked blocky or gray, ❌ your terminal might only support 16/256 colors.")

if __name__ == "__main__":
    main()
