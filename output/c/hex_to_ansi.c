#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void hex_to_ansi(const char *hex, char *out) {
    unsigned int r, g, b;
    sscanf(hex+1, "%02x%02x%02x", &r, &g, &b);
    sprintf(out, "\033[38;2;%u;%u;%um", r, g, b);
}

int main() {
    char ansi[20];
    hex_to_ansi("#FF4500", ansi);
    printf("%sOrange text\033[0m\n", ansi);
    return 0;
}
