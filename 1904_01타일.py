arr = [0] * 1000001
arr[1] = 1
arr[2] = 2
n = int(input())
for i in range(1, n-1):
    arr[i+2] = arr[i+1]+arr[i]
    if arr[i+2] >= 15746:
        arr[i+2] %= 15746
print(arr[n])
