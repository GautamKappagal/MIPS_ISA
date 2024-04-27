#include <stdio.h>

void swap(int *a, int *b){
    int temp;
    temp = *b;
    *b = *a;
    *a = temp;
}

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(&arr[j], &arr[j+1]);
            }
        }
    }
}

int findRank(int arr[], int n, int v){
    for (int i = 0; i < n; i++){
        if (arr[i] == v) return n-i;
    }
    return -1;
}

int main(){
    int n;
    printf ("Enter the number of integers in your array: ");
    scanf("%d",&n);
    int arr[n];
    printf("\n");

    printf("Enter the integers in your array: \n");
    for (int i = 0; i < n; i++){
        scanf("%d",&arr[i]);
    }
    bubbleSort(arr,n);

    printf ("\nSorted array: \n");
    for (int i = 0; i < n; i++){
        printf("%d\n",arr[i]);
    }

    printf("\nEnter the number whose rank you want to find: ");
    int v;
    scanf("%d", &v);
    int result = findRank(arr, n, v);

    if (result == -1){
        printf ("\nNumber not found in the array!\n");
    }
    else{
        printf("\nRank: %d\n",result);
    }

    return 0;
}