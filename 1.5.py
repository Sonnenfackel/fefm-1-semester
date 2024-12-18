num = list(map(int, input().split()))
ref = str(num[0])
b = num[1]
c = num[2]
n = 0
for i in range(len(ref)):
    n += int(ref[i]) * (b**(len(ref)-1-i))
k = 1
h = 1
while h < n:
    h *= c
    k+=1
a = ''
for i in range(k-1,0,-1):
    m = c**(i+1)
    a+=str(n//m)
    n = n % m
print(int(a))


    