while 1:
    list1 = list(map(int, input().split()))
    c = list1.pop(list1.index(max(list1)))
    a, b = list1
    if a**2 + b**2 == c**2 and a > 0 and b > 0:
        print("right")
    elif sum(list1) == 0:
        break
    else:
        print("wrong")
