arr = []
arr.extend([1,1,1,2,2,3,4,5,7,9])
for i in range(10,101):
    arr.append(arr[i-5]+arr[i-1])
for _ in range(int(input())):
    print(arr[int(input())-1])