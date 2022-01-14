import math 
A, B, C = map(int,input().split())
if A >= C:
    print(1)
elif C/2 <= A-B:
    print(2)
else:
    print(math.ceil((C-A)/(A-B)+1))