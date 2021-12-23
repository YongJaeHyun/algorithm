#include <stdio.h>

int main(void) {
	int a, b;
	scanf("%d %d", &a, &b);
	if (b - 45 > 0)
	{
		printf("%d %d", a, b - 45);
	}
	else if (a == 0 && b - 45 < 0)
	{
		printf("%d %d", a + 23, b + 15);
	}
	else if (b - 45 < 0)
	{
		printf("%d %d", a - 1, b + 15);
	}
	else
	{
		printf("%d %d", a, 0);
	}

	return 0;
}