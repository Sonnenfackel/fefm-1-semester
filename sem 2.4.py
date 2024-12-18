num = input().split()
for i in range(0,len(num)-1,2):
    num[i],num[i+1] = num[i+1],num[i]
print(num)