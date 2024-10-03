a = input().split()
b = int(round(int(a[0])/2+0.1))
for i in range (b+1):
  print(i * a[1])
if int(a[0]) % 2 == 0: 
  for i in range(b+1):
    print((b - i) * a[1])
else:
  for i in range(b):
    print((b - i - 1) * a[1])
  
