from sys import stdin, stdout
stdin.readline()
arr = list(map(int, stdin.readline().split()))
arr1 = sorted(set(arr))
dic = {arr1[i]: str(i) for i in range(len(arr1))}
for i in arr:
    stdout.write(dic[i] + ' ')
