#include <stdio.h>

int main(void)
{
    int A, B, C;
    scanf("%d %d %d", &A, &B, &C);
    int ans = A * B * C;
    int arr[10] = { 0, };
    while (ans > 0)
    {
        int num = ans % 10;
        arr[num]++;
        ans /= 10;
    }
    for (int i = 0; i < 10; i++)
    {
        printf("%d\n", arr[i]);
    }
}