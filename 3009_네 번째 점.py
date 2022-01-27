import collections
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
ansX = collections.Counter([x1, x2, x3])
ansY = collections.Counter([y1, y2, y3])
print(ansX.most_common(2)[1][0], ansY.most_common(2)[1][0])
