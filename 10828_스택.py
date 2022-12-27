import sys

input = sys.stdin.readline
n = int(input())
arr = [input().rstrip() for _ in range(n)]
ans = []
for command in arr:
    if command == 'pop':
        print(ans.pop() if ans else -1)
    elif command == 'size':
        print(len(ans))
    elif command == 'empty':
        print(1 if not ans else 0)
    elif command == 'top':
        print(ans[-1] if ans else -1)
    else:
        _, num = command.split()
        ans.append(num)
