#include <stdio.h>

#define NUM_STACKS 3
#define STARTING_HEIGHT 3
#define MAX_HEIGHT 100


int main() {
    FILE *file = fopen("testInput.txt", "r");

    if (file == NULL) {
        perror("Failed to open the file");
        return 1;
    }
    char stacks[NUM_STACKS][MAX_HEIGHT];
    int done  = 0;
    int index = 1;
    
    while (!done) {
        char c = getc(file);
        if ((index % 4 - 2) == 0) {
            printf("%c", c);
        }
        index++;
        if (index == 100) {
            done = 1;
        }
    }
    fclose(file);
    return 0;
}