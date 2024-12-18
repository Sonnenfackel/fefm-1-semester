num = list(map(float, input().split))
s = 1
for i in num:
    s = s*i
print(s**len(num))