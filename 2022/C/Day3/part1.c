#include <stdio.h>
#include <string.h>

int charInString(char c, char* str, int strLength) {
    for (int i = 0; i < strLength; i++) {
        if (str[i] == c) {
            return 1;
        }
    }
    return 0;
}

char findDuplicate(char* str, int strLength) {
    int length = strLength >> 1;
    char c1String[length+1];
    char c2String[length+1];
    strncpy(c1String, str, length);
    c1String[length] = '\0';
    strncpy(c2String, str + length, length);
    c2String[length] = '\0';
    for (int i = 0; i < length; i++) {
        char c = c1String[i];
        if (charInString(c, c2String, length)) {
            return c;
        }
    }
    return '\0';
}

int getScore(char c) {
    int score = (int)c - (int)'a' + 1;
    if (score > 0) {
        return score;
    }
    score = (int)c - (int)'A' + 27;
    return score;
}

int main() {
    FILE *file = fopen("input.txt", "r");

    if (file == NULL) {
        perror("Failed to open the file");
        return 1;
    }
    char lineString[1000];
    int length = 0;
    int done = 0;
    int total = 0;
    while (!done) {
        char c = getc(file);
        if (c == '\n' || c == EOF) {
            char duplicated = findDuplicate(lineString, length);
            total += getScore(duplicated);
            length = 0;
            if (c == EOF) {
                done = 1;
            }
        } 
        else {
            lineString[length] = c;
            length++;
        }

    }
    fclose(file);
    printf("%d", total);
    return 0;
}