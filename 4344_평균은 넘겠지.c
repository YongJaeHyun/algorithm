#include <stdio.h>

int main(void)
{
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        float aver_up_student = 0;
        float sum = 0;
        float average = 0;
        float student;
        int score[1000];
        scanf("%f", &student);
        for (int j = 0; j < student; j++)
        {
            scanf("%d", &score[j]);
            sum += score[j];
        }
        average = (float)sum / student;
        for (int k = 0; k < student; k++)
        {
            if (score[k] > average)
            {
                aver_up_student++;
            }
        }
        printf("%.3f%%\n", aver_up_student / student * 100);
    }
    return 0;
}