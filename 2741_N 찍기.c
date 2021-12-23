#include <stdio.h>

int main(void) {
	int i;
	scanf("%d", &i);
	for (int j = 1; j <= i;)
	{
		printf("%d\n", j);
		j++;
	}
	return 0;
}