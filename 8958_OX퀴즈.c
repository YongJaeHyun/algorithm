#include <stdio.h>
#include <string.h>

int main(void)
{
    int n, score, count;
    scanf("%d", &n);
    char str[80];
    for (int i = 0; i < n; i++)
    {
        scanf("%s", str);
        score = 0;
        count = 1;
        for (int j = 0; j < strlen(str); j++)
        {
            if (str[j] == 'O')
            {
                score += count;
                count++;
            }
            if (str[j] == 'X')
            {
                count = 1;
            }
        }
        printf("%d\n", score);
    }
    return 0;
}