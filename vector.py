class vector:
    def __init__(self,x,y,z):   
        if type(x) == int:
            x = float(x)
        if type(y) == int:
            y = float(y)
        if type(z) == int:
            z = float(z)
        if type(x)==float and type(y) ==  float and type(z) == float:
            self.x = x
            self.y = y
            self.z = z
    def __str__(self):
        return (f'({self.x},{self.y},{self.z})')
    def __abs__(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    def __add__ (self,other):
        if type(other) == vector:
            return vector(self.x + other.x ,self.y + other.y ,self.z + other.z)
        return vector
    def __sub__ (self,other):
        if type(other) == vector:   
            return vector(self.x - other.x ,self.y - other.y ,self.z - other.z)   
    def __mul__ (self,other):
        if type(other) == vector:    
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == float or type(other) == int:
            return vector(self.x * other,self.y * other,self.z * other)
    def __rmul__ (self,other):
        if type(other) == vector:    
            return self.x * other.x + self.y * other.y + self.z * other.z
        elif type(other) == float or type(other) == int:
            return vector(self.x * other,self.y * other,self.z * other)
# #1.1       
# m = list(map(float,input().split()))
# x = list(map(float,input().split()))
# y = list(map(float,input().split()))
# z = list(map(float,input().split()))
# r = []
# for i in range(len(x)):
#     r.append(m[i]*vector(x[i],y[i],z[i]))
# rsum = vector(0,0,0)
# for i in range(len(r)):
#     rsum += r[i]
# print(rsum*(1/sum(m)))
#1.2
x = list(map(float,input().split()))
y = list(map(float,input().split()))
z = list(map(float,input().split()))
r = []
a = 0
def area(a,b,c):
    if abs(a-b) == 0 or abs(b-c)==0:
        return 0
    else:  
        cos = ((a-b)*(b-c))/(abs(a-b)*abs(b-c))
        sin = 1 - cos**2
        if sin == 0 or sin == 1:
            return 0
        else:
            ar = 0.5*abs(a)*abs(a)*sin
            return(ar)

for i in range(len(x)):
    r.append(vector(x[i],y[i],z[i]))
for i in r:
    for j in r:
        for k in r:
            b = area(i,j,k)
            if b > a:
                a = b
print(a)