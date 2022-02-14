import sys


def fibonacci_count(n):
    fibonacci_count_0 = [1, 0, 1]
    fibonacci_count_1 = [0, 1, 1]
    if n > 2:
        for i in range(3, n+1):
            fibonacci_count_0.append(
                fibonacci_count_0[i-1] + fibonacci_count_0[i-2])
            fibonacci_count_1.append(
                fibonacci_count_1[i-1] + fibonacci_count_1[i-2])
    print(fibonacci_count_0)
    print(fibonacci_count_1)
    print(f'{fibonacci_count_0[n]} {fibonacci_count_1[n]}')


for i in range(int(sys.stdin.readline())):
    fibonacci_count(int(sys.stdin.readline()))
