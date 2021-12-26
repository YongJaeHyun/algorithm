#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int n = 0;
    float* arr;
    float max = -1;
    float sum = 0;
    scanf("%d", &n);
    arr = (float*)malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
    }
    for (int j = 0; j < n; j++)
    {
        if (arr[j] > max)
        {
            max = arr[j];
        }
    }
    for (int k = 0; k < n; k++)
    {
        arr[k] = arr[k] / max * 100;
        sum = sum + arr[k];
    }
    sum /= n;
    printf("%.6f", sum);
    return 0;
}