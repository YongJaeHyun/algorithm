#include <stdio.h>

int main(void) {
	int i;
	scanf("%d", &i);
	for (int j = 0; j < i; j++)
	{
		int a, b;
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d + %d = %d\n", j + 1, a, b, a + b);
	}
	return 0;
}