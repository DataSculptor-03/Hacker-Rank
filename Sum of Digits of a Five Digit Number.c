#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n;
    scanf("%d", &n);
    int s=0;
    int rem;
    //Complete the code to calculate the sum of the five digits on n.
    if(n>=10000 && n<=99999){
        while(n!=0){
            rem=n%10;
            s+=rem;
            n=n/10;
        }
    }
    printf("%d",s);
    return 0;
}
