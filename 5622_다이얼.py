a = input()
for i in a:
    if i in ['A','B','C']:
        a[a.index(i)] = 3
    elif i in ['D','E','F']:
        a[a.index(i)] = 4
    elif i in ['G','H','I']:
        a[a.index(i)] = 5
    elif i in ['J','K','L']:
        a[a.index(i)] = 6
    elif i in ['M','N','O']:
        a[a.index(i)] = 7
    elif i in ['P','Q','R','S']:
        a[a.index(i)] = 8
    elif i in ['T','U','V']:
        a[a.index(i)] = 9
    else: a[a.index(i)] = 10
print(sum(a))
    