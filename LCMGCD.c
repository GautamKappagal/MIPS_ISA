#include <stdio.h>

int gcd (int a, int b){
  if (b == 0) return a;
  return gcd (b, a%b); 
}

int lcm (int a, int b, int gcd){
    return (a*b)/gcd;
}

int main(){
    int num1, num2;
    printf("Enter the first number: ");
    scanf("%d",&num1);
    printf("Enter the second number: ");
    scanf("%d",&num2);
    printf("\n");

    int gcd_op = gcd (num1, num2);
    int lcm_op = lcm (num1, num2, gcd_op);

    printf ("GCD of %d and %d: %d\n",num1, num2, gcd_op);
    printf ("LCM of %d and %d: %d\n",num1, num2, lcm_op);
}
