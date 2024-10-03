a = [1, 1]
n = int(input()) - 1
for i in range(1, n):
    a.append(a[i - 1] + a[i])
print(a[n])
    
