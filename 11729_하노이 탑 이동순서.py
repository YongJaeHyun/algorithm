def hanoi(n, start, end, extra):
    if n == 1:
        print(start, end)
        return
    hanoi(n-1, start, extra, end)
    print(start, end)
    hanoi(n-1, extra, end, start)


n = int(input())
print(n**2+1)
hanoi(n, 1, 3, 2)
