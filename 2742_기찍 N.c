#include <stdio.h>

int main(void) {
	int i;
	scanf("%d", &i);
	for (int j = 0; j < i; j++)
	{
		printf("%d\n", i - j);
	}
	return 0;
}