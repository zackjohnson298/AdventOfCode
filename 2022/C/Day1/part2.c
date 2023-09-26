#include <stdio.h>
#include <string.h>

int stringToInt(char* str) {
    int num;
    if (sscanf(str, "%d", &num) == 1) {
        return num;
    }
    return -1;
}

void updateMaxes(int currentValue, int* max1, int* max2, int* max3) {
    if (*max3 <= currentValue && *max2 > currentValue) {
        *max3 = currentValue;
    }
    else if (*max2 <= currentValue && *max1 > currentValue) {
        *max3 = *max2;
        *max2 = currentValue;
    }
    else if (*max1 <= currentValue) {
        *max3 = *max2;
        *max2 = *max1;
        *max1 = currentValue;
    }
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
    int maxTotal1 = 0;
    int maxTotal2 = 0;
    int maxTotal3 = 0;
    int count = 1;
    while (fgets(lineString, sizeof(lineString), file) != NULL) {
        if (sscanf(lineString, "%d", &lineInt) == 1) {
            currentTotal += lineInt;
        } else {
            printf("Elf %d total: %d\n", count, currentTotal);
            count++;
            updateMaxes(currentTotal, &maxTotal1, &maxTotal2, &maxTotal3);
            currentTotal = 0;
        }
        char lineString[100] = "";
    }
    fclose(file);
    printf("Elf %d total: %d\n", count, currentTotal);
    count++;
    updateMaxes(currentTotal, &maxTotal1, &maxTotal2, &maxTotal3);
    printf("%d, %d, %d;  %d", maxTotal1, maxTotal2, maxTotal3, maxTotal1 + maxTotal2 + maxTotal3);
    return 0;
}