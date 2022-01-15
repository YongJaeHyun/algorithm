T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    listN = list(range(1,n+1))
    if k == 1:
        print(sum(range(n+1)))
    elif k == 0:
        print(listN[n])
    elif n == 1:
        print(n)
    else:   
        k_count = 1
        ans1 = [1]
        while k != k_count:
            a = 1
            ans = [1]
            for i in range(1,n):
                b = a + listN[i]
                listN[i] = b
                ans.append(b)
                a = b
            k_count += 1 
        print(sum(ans[:n+1]))