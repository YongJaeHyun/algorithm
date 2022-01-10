X = int(input())
count = 0
while X > 0:
    count += 1
    X -= count
if X == 0:
    if count % 2 == 0: print(f"{count}/1")
    else: print(f"1/{count}")
elif count % 2 == 0: print(f"{count+X}/{1-X}")
else: print(f"{1-X}/{count+X}")