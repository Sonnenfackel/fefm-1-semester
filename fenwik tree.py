
def fen(a, i):
    t = sum(a[(i & (i-1))+1:i+1])
    return t
def F(x):
    f = x - (x & (x-1))
    return f

class Fenwik:
    def __init__(self,a):
        c = a.copy()
        c.insert(0,0)
        k = 1
        while k < len(a)-1:
            k = k*2
        b = [0]*(k+1)
        self.array = b
        
    def modify(self,n,x):
        i = n
        while i <= len(self.array) - 1:
            self.array[i] = self.array[i] + x
            i = i + F(i)

    def caunt(self,n):
        res = 0
        i = n
        while i > 0:
            res = res + self.array[i]
            i = i - F(i)
        return res
def stair(a):
    b = Fenwik(a)
    res = 0
    for i in a:
        k = b.caunt(i-1)
        res += k
        b.modify(i-1,i-1)
    return res

t = int(input())
for i in range(t):
    l = int(input())
    num = list(map(int, input().split()))
    res = stair(num)
    print(*res, sep = " ")