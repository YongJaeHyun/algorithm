n = int(input())
count = 0
for i in range(n):
    st_count = 0
    st = list(input())
    for char in st:
        total_char = st.count(char)
        b = st[st.index(char)]*total_char
        c = ''.join(st[st.index(char):st.index(char)+total_char])
        if b==c:
            st_count += 1
        if st_count == len(st):
            count += 1
        else: pass
print(count)