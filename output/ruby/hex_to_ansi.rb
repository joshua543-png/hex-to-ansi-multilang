def hex_to_ansi(hex)
  hex = hex.delete('#')
  r = hex[0..1].to_i(16)
  g = hex[2..3].to_i(16)
  b = hex[4..5].to_i(16)
  "\e[38;2;#{r};#{g};#{b}m"
end

puts "#{hex_to_ansi('#FF4500')}Orange text\e[0m"
