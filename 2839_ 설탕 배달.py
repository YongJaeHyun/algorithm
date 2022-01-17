n = int(input())
div8, mod8 = divmod(n,8)
div5, mod5 = divmod(mod8,5)
div3, mod3 = divmod(mod8,3)
if mod8 == 0:
    print(div8*2)
elif mod5 == 0:
    div5, mod5 = divmod(n,5)
    div3, mod3 = divmod(n,3)
    print(div8*2 + div5)
elif mod3 == 0:
    print(div8*2 + div3)
else:
    div5, mod5 = divmod(n,5)
    div3, mod3 = divmod(n,3)
    if mod5 == 0:
        print(div5)
    elif mod3 == 0:
        print(div3)
    else: print(-1)
