from sys import stdin
input = stdin.readline
arr = [0] * 20000001
input()
a = list(map(int, input().split()))
for n in a:
    arr[n] = 1
input()
a2 = list(map(int, input().split()))
ans = []
for n in a2:
    ans.append(str(arr[n]))
print(" ".join(ans))
