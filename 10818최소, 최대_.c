#include <stdio.h>

int main(void)
{
    int n, min, max;
    scanf("%d", &n);
    int arr[n];
    min = 1000001;
    max = -1000001;
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        if (min > arr[i])
        {
            min = arr[i];
        }
        if (max < arr[i])
        {
            max = arr[i];
        }
    }

    printf("%d %d", min, max);
    return 0;
}