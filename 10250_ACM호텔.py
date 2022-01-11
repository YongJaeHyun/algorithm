T = int(input())
for i in range(T):
    H, W, N = map(int,input().split())
    a, b = divmod(N,H)
    if b == 0:
        print(H*100+a)
    else:
        print(b*100+a+1)