import math
n = int(input())
cnt = 0
for i in map(int,input().split()):
    count = 0
    if i == 2 or i == 3:
        cnt += 1
    if i > 4:
        for j in range(2,math.ceil(math.sqrt(i))+1):
            if i % j == 0:
                count += 1
        if count == 0:
            cnt += 1
print(cnt)