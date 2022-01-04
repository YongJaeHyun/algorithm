i = 0
j = 0
T = int(input())
while i < T:
    Input = input( )
    R = int(Input[:1])
    S = [*Input[2:]]
    while j < len(S):
       print(S[j]*R, end='')
       j += 1   
    if j == len(S):
           j = 0
    i += 1
    print("")