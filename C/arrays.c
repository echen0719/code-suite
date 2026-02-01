#include <stdio.h>
#include <string.h>
#include <ctype.h>

// easy, default function
double average(int num[], int length) {
    int sum = 0;
    for (int i = 0; i < length; i++) {
        sum += num[i];
    }
    return sum / (double) length;
}

int charToInt(char character) {
    return (int) character;
}

// argc for number of arguments
// argv for the actual arguments

int main(int argc, char* argv[]) {
    const int LENGTH = 5;
    int answers[LENGTH]; // Java would be var = new int[length];
    for(int i = 0; i < LENGTH; i++) { // why no in-built .length()?
        printf("Your #%d favorite integer: ", i + 1);
        scanf("%d", &answers[i]); // new line
    }

    printf("\nYour favorite numbers are: ");
    for(int i = 0; i < LENGTH; i++) {
        printf("%d ", answers[i]); // loops and prints
    }

    printf("\nAverage of these values is: %0.5f", average(answers, LENGTH));

    // C casting char --> int
    printf("\n\nAside from that: A is %d and a is %d", charToInt('A'), charToInt('a'));

    char msg[] = "String is a just a polymer"; // string arr
    for (int i = 0; i < strlen(msg); i++) {
        msg[i] = toupper(msg[i]);
    } // string toUpperCase

    printf("\nAlso, the phrase \"%s\" has %d characters.", msg, strlen(msg));
    printf("\n\nFile name is: %s", argv[0]);
}