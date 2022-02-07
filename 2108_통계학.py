import sys
from collections import Counter
ans = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
print(round(sum(ans)/len(ans)))
ans.sort()
print(ans[len(ans)//2])
mode = Counter(ans)
if len(ans) > 1 and mode.most_common(2)[0][1] == mode.most_common(2)[1][1]:
    print(mode.most_common(2)[1][0])
else:
    print(mode.most_common(1)[0][0])
print(max(ans)-min(ans))
