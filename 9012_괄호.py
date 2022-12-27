n = int(input())
arr = [input() for _ in range(n)]
for stream in arr:    
    prev_stream = ''
    while True:
        if prev_stream == stream:
            break
        prev_stream = stream
        stream = stream.replace('()','')
    if stream == '':
        print('YES')
    else: print('NO')