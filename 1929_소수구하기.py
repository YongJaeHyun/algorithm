a, b = map(int, input().split())
arr = ([False]+[True])*(b+1//2+1)
arr[1], arr[2] = False, True
for i in range(3, int(b**.5)+1):
    if arr[i] == True:
        j = 2
        while i*j < b+1:
            arr[i*j] = False
            j += 1
    else:
        pass
for i in range(a, b+1):
    if arr[i]:
        print(i)
