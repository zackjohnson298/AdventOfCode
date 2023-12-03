#include <stdio.h>

int main() {
    FILE *file = fopen("input.txt", "r");

    if (file == NULL) {
        perror("Failed to open the file");
        return 1;
    }
    char line[100];
    int i = 0;
    char c;
    int total = 0;
    while (!feof(file)) {
        char c = getc(file);
        if (c == '\n' || c == EOF) {
            line[i] = '\0';
            i = 0;
            int a, b, c, d;
            if (sscanf(line, "%d-%d,%d-%d", &a, &b, &c, &d) == 4) {
                // printf("%d %d %d %d\n", a, b, c, d);
                if ((a >= c && b <= d) || (c >= a && d <= b)) {
                    total++;
                }
            }
            else {
                printf("Failed to parse line: %s", line);
                return 1;
            }
        } 
        else {
            line[i] = c;
            i++;
        }

    }
    printf("%d", total);
    fclose(file);
    return 0;
}