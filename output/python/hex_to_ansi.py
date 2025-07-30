def hex_to_ansi(hex_code):
    hex_code = hex_code.lstrip('#')
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return f"\033[38;2;{r};{g};{b}m"

if __name__ == "__main__":
    print(hex_to_ansi("#FF4500") + "Orange text" + "\033[0m")
