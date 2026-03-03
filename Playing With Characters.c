#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{
    char ch;
    char ch1[100], ch2[100];

    scanf("%c", &ch);        // read single character
    getchar();               // consume newline left by scanf

    scanf("%s", ch1);        // read a word
    getchar();               // consume newline left by scanf

    scanf("%[^\n]", ch2);    // read full line (with spaces)

    printf("%c\n", ch);
    printf("%s\n", ch1);
    printf("%s\n", ch2);

    return 0;
}
