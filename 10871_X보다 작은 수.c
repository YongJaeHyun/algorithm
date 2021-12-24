#include <stdio.h>
int main(void)
{
    int x, n;
    int arr[x];
    scanf("%d %d", &x, &n);
    for (int i = 0; i < x; i++)
    {
        scanf("%d", &arr[i]);
        if (arr[i] < n)
            printf("%d ", arr[i]);
    }
    return 0;
}