hour, minute = map(int, input().split())
plus_minute = int(input())
minute += plus_minute
plus_hour, minute = divmod(minute, 60)
hour += plus_hour
hour %= 24
print(f"{hour} {minute}")
