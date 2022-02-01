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
                print(count*2-1)
                break
            if count**2 - count < length:
                print(count*2-1)
                break
            else:
                print(count*2-2)
                break