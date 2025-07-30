#!/bin/bash
hex_to_ansi() {
    hex="${1#"#"}"
    r=$((16#${hex:0:2}))
    g=$((16#${hex:2:2}))
    b=$((16#${hex:4:2}))
    echo -e "\033[38;2;${r};${g};${b}m"
}

ansi=$(hex_to_ansi "#FF4500")
echo -e "${ansi}Orange text[0m"
