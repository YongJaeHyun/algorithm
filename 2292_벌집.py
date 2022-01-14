n= int(input())
i = 1
j = 1
while 1:
    if n <= i:
        print(j)
        break
    i += 6*j
    j += 1  