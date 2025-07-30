package main

import (
    "fmt"
    "strconv"
    "strings"
)

func hexToAnsi(hex string) string {
    hex = strings.TrimPrefix(hex, "#")
    r, _ := strconv.ParseInt(hex[0:2], 16, 64)
    g, _ := strconv.ParseInt(hex[2:4], 16, 64)
    b, _ := strconv.ParseInt(hex[4:6], 16, 64)
    return fmt.Sprintf("\033[38;2;%d;%d;%dm", r, g, b)
}

func main() {
    fmt.Println(hexToAnsi("#FF4500") + "Orange text" + "\033[0m")
}
