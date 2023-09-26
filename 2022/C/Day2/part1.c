#include <stdio.h>

int getScoreForLine(char playerA, char playerB) {
    if (playerA == 'A' && playerB == 'X') {
        return 1 + 3;
    }
    if (playerA == 'A' && playerB == 'Y') {
        return 2 + 6;
    }
    if (playerA == 'A' && playerB == 'Z') {
        return 3 + 0;
    }

    if (playerA == 'B' && playerB == 'X') {
        return 1 + 0;
    }
    if (playerA == 'B' && playerB == 'Y') {
        return 2 + 3;
    }
    if (playerA == 'B' && playerB == 'Z') {
        return 3 + 6;
    }

    if (playerA == 'C' && playerB == 'X') {
        return 1 + 6;
    }
    if (playerA == 'C' && playerB == 'Y') {
        return 2 + 0;
    }
    if (playerA == 'C' && playerB == 'Z') {
        return 3 + 3;
    }
    return -1;
}

int main() {
    FILE *file = fopen("input.txt", "r");

    if (file == NULL) {
        perror("Failed to open the file");
        return 1;
    }

    char lineString[4];
    int currentScore = 0;
    int totalScore = 0;
    while (fgets(lineString, sizeof(lineString), file) != NULL) {
        if (lineString[0] == '\n') {
            continue;;
        }
        currentScore = getScoreForLine(lineString[0], lineString[2]);
        if (currentScore == -1) {
            printf("Unhandled case: %s\n", lineString);
            return 1;
        }
        totalScore += currentScore;
        // printf("%d, %s\n", currentScore, lineString);
    }
    fclose(file);
    printf("%d", totalScore);
    return 0;
}