from sys import stdin
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
plus, minus, mul, div = map(int, stdin.readline().split())
maximum = -10**9
minimum = 10**9


def func(num, total, plus, minus, mul, div):
    global maximum, minimum
    if num == n:
        maximum = max(maximum, total)
        minimum = min(minimum, total)

    if plus:
        func(num+1, total+arr[num], plus-1, minus, mul, div)
    if minus:
        func(num+1, total-arr[num], plus, minus-1, mul, div)
    if mul:
        func(num+1, total*arr[num], plus, minus, mul-1, div)
    if div:
        func(num+1, int(total/arr[num]), plus, minus, mul, div-1)


func(1, arr[0], plus, minus, mul, div)
print(maximum)
print(minimum)
