#include <stdio.h>
int main(void)
{
    int arr[10] = { 0, };
    scanf("%d %d %d %d %d %d %d %d %d %d", &arr[0], &arr[1], &arr[2], &arr[3],
        &arr[4], &arr[5], &arr[6], &arr[7], &arr[8], &arr[9]);
    int count = 0;
    for (int i = 0; i < 10; i++)
    {
        arr[i] %= 42;
    }
    for (int j = 0; j < 10; j++)
    {
        for (int k = j; k < 10; k++)
        {
            if (arr[j] == arr[k + 1])
            {
                arr[j] = -1;
            }
        }
    }
    for (int h = 0; h < 10; h++)
    {
        if (arr[h] != -1)
        {
            count++;
        }
    }

    printf("%d", count);
    return 0;
}