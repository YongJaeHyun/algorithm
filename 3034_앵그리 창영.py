import math

n, w, h = map(int, input().split())
for _ in range(n):
    length = int(input())
    max_length = math.sqrt(w**2 + h**2)
    if length <= max_length:
        print("DA")
    else:
        print("NE")
