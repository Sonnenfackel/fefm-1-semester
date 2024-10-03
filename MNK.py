import numpy as np
x = np.array([list(map(float, input().split()))])
y = np.array([list(map(float, input().split()))])
b = ((np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x ** 2) - (np.mean(x)) ** 2))
eb = (1/(len(x) ** (1/2)))*((((np.mean(y ** 2) - (np.mean(y)) ** 2)/(np.mean(x ** 2) - (np.mean(x)) ** 2)) - b ** 2) ** (1/2))
a = np.mean(y) - b*np.mean(x)
ea = eb*((np.mean(x ** 2) - (np.mean(x)) ** 2) ** (1/2))
print('a =', a, '\n',"b =",b, '\n','Погрешность а =', ea, '\n','Погрешность b =', eb )