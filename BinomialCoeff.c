#include <stdio.h>

int factorial (int n){
    int result = 1;

    for (int i = 1; i <= n; i++){
        result *= i;
    }

    return result;
}

int* fillingArray (int arr[], int n){
    int r, num = factorial(n), denom;
    for (r = 0; r < n+1; r++){
        denom = factorial(r) * factorial(n-r);
        arr[r] = num / denom;
    }
}

int main(){
    int n;
    printf("Enter n: ");
    scanf("%d",&n);
    int arr[n+1];

    fillingArray(arr, n);

    printf("The Binomial expansion of (1 + x)^%d: ",n );
    for (int i = 0; i <= n; i++){
        if (i == n) printf ("%dx^%d\n",arr[i],i);
        else{
            printf ("%dx^%d + ",arr[i],i);
        }
    }

}
