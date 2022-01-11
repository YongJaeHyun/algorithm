n = int(input())
for i in range(n):
    start, end = map(int,input().split())
    count = 1
    while 1:
        length = end - start
        if length == 1 or length == 2 or length == 3:
            print(length)
            break
        else:
        
            while length > count**2: count += 1
            if (length == count**2):
                print((count)*2-1)
                break
            if count**2 - count <= length:
                print(count*2-1)
                break
            else:
                print(count*2-2)
                break
    
# 0, 25// 1,2,3,4,5,4,3,2,1
# 0, 24// 1,2,3,4,4,4,3,2,1
# 0, 23// 1,2,3,4,3,4,3,2,1
# 0, 22// 1,2,3,4,3,3,3,2,1
# 0, 21// 1,2,3,4,3,3,2,2,1
# 0, 20// 1,2,3,4,3,3,2,1,1
# 0, 19// 1,2,3,4,3,3,2,1
# 0, 18// 1,2,3,4,3,3,