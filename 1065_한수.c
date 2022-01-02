#include <stdio.h>

int getHansu(int i)
{
	int a = i;
	int first, second, distance1, distance2;
	while (1)
	{
		first = i % 10;
		second = (i / 10) % 10;
		distance1 = second - first;
		i /= 10;
		if (i < 10)
		{
			return 1;
			break;
		}
		first = i % 10;
		second = i / 10;
		distance2 = second - first;
		if (distance1 == distance2)
		{
			return 1;
			break;
		}
		else
		{
			return 0;
			break;
		}
	}
}

int main(void)
{
	int n, Check, ans = 0;
	scanf("%d", &n);
	for (int i = 1; i < n + 1; i++)
	{
		Check = getHansu(i);
		if (Check == 1)
		{
			ans++;
		}
	}
	printf("%d", ans);
	return 0;
}