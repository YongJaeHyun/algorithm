num = int(input())
cnt = 0
for i in range(num):
    if num == i + sum(map(int, str(i))):
        print(i)
        cnt = 1
        break
if cnt == 0:
    print(0)
