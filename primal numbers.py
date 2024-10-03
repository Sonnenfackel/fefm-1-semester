n  = int(input())
de = [] 
for i in range(1, n):
    if n % i == 0:
        de.append(n/i)
a = []
pr = []
for i in range (len(de)):
    for k in range(1, int(de[i])+1):
        if de[i] % k == 0:
            a.append(de[i]/k)
            if k == int(de[i]):
                if len(a) == 2:
                    pr.append(de[i])
                    a = []
                else: a = []
d = 0
k = n
for i in range(len(pr)):
    while k % pr[i] == 0 and k/pr[i] != pr[i]:
        d = d+1
        k = k/pr[i]
        if k/pr[i] == pr[i]:
            d = d+1
    print(int(pr[i]),'^', d, sep="")
    d = 0
    k = n
