fn hex_to_ansi(hex: &str) -> String {
    let hex = hex.trim_start_matches('#');
    let r = u8::from_str_radix(&hex[0..2], 16).unwrap();
    let g = u8::from_str_radix(&hex[2..4], 16).unwrap();
    let b = u8::from_str_radix(&hex[4..6], 16).unwrap();
    format!("\x1b[38;2;{};{};{}m", r, g, b)
}

fn main() {
    println!("{}Orange text[0m", hex_to_ansi("#FF4500"));
}
