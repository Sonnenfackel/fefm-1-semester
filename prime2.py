n = int(input())
prdiv = []
for i in range(2, round(n/2)):
    t = 0
    if n % i > 0:
        continue
    for j in prdiv:
        if i % j == 0:
            t = 1
    if t == 1:
        continue
    prdiv.append(i)
power = [0]*len(prdiv)
for y in range(len(prdiv)):
    while n%prdiv[y] == 0:
        n//=prdiv[y]
        power[y]+=1
for i in range(len(prdiv)):
    print(prdiv[i],'^',power[i], sep='')





