A, B, C = input().split()
A, B, C = int(A), int(B), int(C)
n = 1
if B >= C: print(-1)
else: print(A // (C - B)+ 1)