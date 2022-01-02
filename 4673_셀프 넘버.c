#include <stdio.h>

int getNonSelfNum(int n)
{
    int sum = n;
    while (n > 0)
    {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}
int main(void)
{
    int ans[10001], arr;
    for (int i = 1; i < 10001; i++)
    {
        arr = getNonSelfNum(i);
        if (arr < 10001)
        {
            ans[arr] = 1;
        }
    }
    for (int j = 1; j < 10001; j++)
    {
        if (ans[j] != 1)
        {
            printf("%d\n", j);
        }
    }
    return 0;
}
