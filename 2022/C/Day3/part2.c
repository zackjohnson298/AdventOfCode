#include <stdio.h>
#include <string.h>

#define ELF_COUNT 3
#define ARR_SIZE 1000


int charInString(char c, char* str, int strLength) {
    for (int i = 0; i < strLength; i++) {
        if (str[i] == c) {
            return 1;
        }
    }
    return 0;
}

int getScore(char c) {
    int score = (int)c - (int)'a' + 1;
    if (score > 0) {
        return score;
    }
    score = (int)c - (int)'A' + 27;
    return score;
}

void printString(char* str, int length) {
    for (int i = 0; i < length; i++) {
        printf("%c", str[i]);
    }
    printf("\n");
}

char findBadge(char* elf1, char* elf2, char* elf3, int len1, int len2, int len3) {
    for (int i = 0; i < len1; i++) {
        char c = elf1[i];
        if (charInString(c, elf2, len2) && charInString(c, elf3, len3)) {
            return c;
        }
    }
    return '\0';
}

int main() {
    FILE *file = fopen("input.txt", "r");

    if (file == NULL) {
        perror("Failed to open the file");
        return 1;
    }
    char elfArray[3][1000];
    int lengths[3] = {0, 0, 0};
    int done = 0;
    int currentElf = 0;
    int total = 0;
    while (!done) {
        char c = getc(file);
        if (c != '\n' && c != EOF) {
            elfArray[currentElf][lengths[currentElf]] = c;
            lengths[currentElf]++;
        } 
        else {
            currentElf++;
            if (currentElf == 3) {
                currentElf = 0;
                char badge = findBadge(elfArray[0], elfArray[1], elfArray[2], lengths[0], lengths[1], lengths[2]);
                if (badge == '\0') {
                    printf("Could not find badge");
                    return 1;
                }
                total += getScore(badge);
            }
            lengths[currentElf] = 0;
            if (c == EOF) {
                done = 1;
            }
        }
    }
    printf("%d", total);
    fclose(file);
    return 0;
}