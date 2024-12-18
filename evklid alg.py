n = input().split()
a = int(n[0])
b = int(n[1])
a1 = a
b1 = b
while b1 != 0 and a1 != 0:
    if a1>b1:
        a1 = a1%b1
    else:
        b1 = b1%a1
c = a1+b1
print(c)
x=0
y=0
a1 = int(a/c)
b1 = int(b/c)
print(a1)
print(b1)
if a == b:
    x=1
    print(x, y, c)
else:
    while x*a+y*b != c :
        if b>a:
            x = x+1
            y = (1-b1*x)/a1
        else:
            x = x-1
            y = (1-b1*x)/a1
    print(x,y,c)