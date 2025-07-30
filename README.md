# 🎨 Hex to ANSI Multi-Language Library

Convert hex color codes like `#FF4500` into ANSI escape sequences for 24-bit color terminal output — implemented in **10+ different programming languages**.

This project is a handy reference or starting point for anyone building colorful command-line tools.

## 🌐 Supported Languages

✅ Python  
✅ JavaScript (Node.js)  
✅ Go  
✅ Rust  
✅ C  
✅ C++  
✅ Java  
✅ Ruby  
✅ Bash  
✅ PowerShell  

Each implementation includes a `hexToAnsi` function (or equivalent), and a usage example that prints colored text in the terminal.

## 📦 Folder Structure

hex-to-ansi-multilang/  
├── python/  
│   └── hex_to_ansi.py  
├── javascript/  
│   └── hexToAnsi.js  
├── go/  
│   └── hexToAnsi.go  
├── rust/  
│   └── hex_to_ansi.rs  
├── c/  
│   └── hex_to_ansi.c  
├── cpp/  
│   └── hex_to_ansi.cpp  
├── java/  
│   └── HexToAnsi.java  
├── ruby/  
│   └── hex_to_ansi.rb  
├── bash/  
│   └── hex_to_ansi.sh  
├── powershell/  
│   └── HexToAnsi.ps1  

## 🧪 Example Usage

### Python

print(hex_to_ansi("#FF4500") + "Orange text" + "\033[0m")

### JavaScript (Node.js)

console.log(hexToAnsi("#FF4500") + "Orange text" + "\x1b[0m");

### Bash

./hex_to_ansi.sh

### PowerShell

.\HexToAnsi.ps1

## 🔧 How to Run

You’ll need the appropriate interpreter or compiler for each language. Examples:

# Python  
cd python  
python hex_to_ansi.py

# Node.js  
cd javascript  
node hexToAnsi.js

# Go  
cd go  
go run hexToAnsi.go

# Rust  
cd rust  
rustc hex_to_ansi.rs && ./hex_to_ansi

# C  
cd c  
gcc hex_to_ansi.c -o ansi && ./ansi

# C++  
cd cpp  
g++ hex_to_ansi.cpp -o ansi && ./ansi

# Java  
cd java  
javac HexToAnsi.java && java HexToAnsi

# Ruby  
cd ruby  
ruby hex_to_ansi.rb

# Bash  
cd bash  
bash hex_to_ansi.sh

# PowerShell  
cd powershell  
powershell -ExecutionPolicy Bypass -File HexToAnsi.ps1

## 💻 Terminal Compatibility

This project uses 24-bit (true color) ANSI escape codes, which are supported on most modern terminal emulators, including:

### Windows  
- Windows Terminal (modern Microsoft terminal app)  
- PowerShell (especially in Windows Terminal)  
- ConEmu, Cmder  
- Git Bash (MinGW)  

### Linux / Unix-like  
- GNOME Terminal  
- Konsole (KDE)  
- Alacritty  
- Terminator  
- Kitty  
- XTerm (recent versions)  

### macOS  
- Terminal.app (modern versions)  
- iTerm2  
- Alacritty  
- Kitty  

### Cross-platform / Others  
- Visual Studio Code integrated terminal  
- JetBrains IDE terminals  
- Hyper  

**Note:** Older terminals or default Windows cmd.exe might not fully support 24-bit colors and may show limited colors instead.

If you want to check if your terminal supports true color, look for environment variables like `COLORTERM=truecolor` or try running online true color tests.

---

## 💬 Contributing

Want to add another language or improve an implementation? Pull requests welcome!

## 📝 License

MIT License — free to use, modify, and share.

## Discord

https://discord.gg/MtjxDCcR  
This Discord server is for questions and concerns.
