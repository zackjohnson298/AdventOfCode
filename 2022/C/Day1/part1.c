#include <stdio.h>
#include <string.h>

int stringToInt(char* str) {
    int num;
    if (sscanf(str, "%d", &num) == 1) {
        return num;
    }
    return -1;
}

int main() {
    FILE *file = fopen("input.txt", "r");

    if (file == NULL) {
        perror("Failed to open the file");
        return 1;
    }

    char lineString[100] = "";
    int lineInt;
    int currentTotal = 0;
    int maxTotal = 0;
    while (fgets(lineString, sizeof(lineString), file) != NULL) {
        if (sscanf(lineString, "%d", &lineInt) == 1) {
            currentTotal += lineInt;
        } else {
            if (maxTotal < currentTotal) {
                maxTotal = currentTotal;
            }
            currentTotal = 0;
        }
        char lineString[100] = "";
    }
    fclose(file);
    printf("%d", maxTotal);
    return 0;
}