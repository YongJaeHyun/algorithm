#include <stdio.h>

int main(void) {
	int i;
	scanf("%d", &i);
	for (int j = 1; j <= i; j++)
	{
		for (int k = 1; k <= j;)
		{
			printf("*");
			k++;
		}
		printf("\n");
	}
	return 0;
}