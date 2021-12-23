#include <stdio.h>

int main(void) {
	int i;
	int sum = 0;
	scanf("%d", &i);
	for (int j = 0; j < i; j++)
	{
		int a = 0;
		int	b = 0;
		scanf("%d %d", &a, &b);
		printf("%d\n", a + b);
	}
	return 0;
}