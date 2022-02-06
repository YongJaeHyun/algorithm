import sys
n = [list(map(int, sys.stdin.readline().split()))
     for _ in range(int(sys.stdin.readline()))]
n.sort()
for i in range(len(n)):
    print(n[i][0], end=' ')
    print(n[i][1])
