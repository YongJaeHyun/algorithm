import math
cnt = []
for i in range(int(input()),int(input())+1):
    count = 0
    if i == 2:
        cnt.append(i)
    if i > 2:
        for j in range(2,math.ceil(math.sqrt(i))+1):
            if i % j == 0:
                count += 1
        if count == 0:
            cnt.append(i)
if cnt != []:
    print(sum(cnt))
    print(min(cnt))
else:
    print(-1)