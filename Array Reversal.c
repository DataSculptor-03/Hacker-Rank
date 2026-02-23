#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num, *arr, *rev, i;
    scanf("%d", &num);

    arr = (int*) malloc(num * sizeof(int));
    rev = (int*) malloc(num * sizeof(int));  // Allocate memory for reversed array

    for(i = 0; i < num; i++) {
        scanf("%d", &arr[i]);
    }

    // Reverse into a temporary array
    for(i = 0; i < num; i++) {
        rev[i] = arr[num - i - 1];
    }

    // Copy back to original array if required
    for(i = 0; i < num; i++) {
        arr[i] = rev[i];
    }

    for(i = 0; i < num; i++) {
        printf("%d ", arr[i]);
    }

    free(arr);
    free(rev);
    return 0;
}
