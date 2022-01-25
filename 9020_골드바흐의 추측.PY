import sys
arr = [False, False, True] + [True, False] * 5000
arr[2] = True
for i in range(int(10000**.5)+1):
    if arr[i]:
        j = 2
        while i*j <= 10000:
            arr[i*j] = False
            j += 1
t = int(sys.stdin.readline())
for i in range(t):
    cnt = 0
    n = int(sys.stdin.readline())
    n //= 2
    while arr[n-cnt] == False or arr[n+cnt] == False:
        cnt += 1
    print(n-cnt, n+cnt)