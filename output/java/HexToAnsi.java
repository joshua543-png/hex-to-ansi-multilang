public class HexToAnsi {
    public static String hexToAnsi(String hex) {
        hex = hex.replace("#", "");
        int r = Integer.parseInt(hex.substring(0, 2), 16);
        int g = Integer.parseInt(hex.substring(2, 4), 16);
        int b = Integer.parseInt(hex.substring(4, 6), 16);
        return String.format("\033[38;2;%d;%d;%dm", r, g, b);
    }

    public static void main(String[] args) {
        System.out.println(hexToAnsi("#FF4500") + "Orange text" + "\033[0m");
    }
}
