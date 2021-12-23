#include <stdio.h>

int main(void) {
	int a, b;
	scanf("%d %d", &a, &b);
	int A, B, C;
	A = a * (b % 10);
	B = a * ((b % 100) / 10);
	C = a * (b / 100);
	printf("%d\n", A);
	printf("%d\n", B);
	printf("%d\n", C);
	printf("%d\n", A + 10 * B + 100 * C);
	return 0;
}