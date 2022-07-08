import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dict = {}

for _ in range(n):
    tmp = input().strip()
    dict[tmp] = True

ans = 0
for _ in range(m):
    tmp = input().strip()
    if tmp in dict.keys():
        ans += 1
        
print(dict.keys())