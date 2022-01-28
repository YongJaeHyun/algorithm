T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**.5
    if r1 == r2 and distance == 0:
        print(-1)
    elif distance == r2 + r1 or distance == abs(r2 - r1):
        print(1)
    elif abs(r2 - r1) < distance < r2 + r1:
        print(2)
    else:
        print(0)
