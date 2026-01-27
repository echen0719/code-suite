// this is just like Java
// I don't see much difference honestly

#include <stdio.h>
#include <stdlib.h>

void funnyMsg(int n) {
    for(int i = 1; i <= n; i++) {
        printf("I pissed my pants %d time(s).\n", i);
    }
    
    printf("\nHere is a 3x3 wall for you: \n");
    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
            printf("#");
        }
        printf("\n");
    }
}

int main(void) {
    // don't do this: printf("Hello world! " + "I am a program\n");
    printf("Hello world! %s", "I am a program\n"); // do this

    int num1 = rand() % 10 + 1;
    int num2 = rand() % 10 + 1;

    if (num1 > num2) {
        printf("\nObviously, %d is greater than %d\n\n", num1, num2);
    }
    else if (num1 < num2) {
        printf("Obviously, %d is less than %d\n\n", num1, num2);
    }
    else {
        printf("Yo, %d and %d are the same. You lucky boy\n\n", num1, num2);
    }

    funnyMsg(5);
 }