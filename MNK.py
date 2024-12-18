import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



f = open('1.4.8.txt') # открываем файл с данными. данные в формате: 1,2 строка - соответственно знаечния х и у, 3,4 строка - соответсвенно погрешности х и у 
#(если их нет, введи через пробел столько же нулей, сколько и значений соответствующей переменной)
x = list(map(float, f.readline().split()))
y = list(map(float, f.readline().split()))
 # вводим переменные и их погрешности

xer = list(map(float, f.readline().split()))
yer = list(map(float, f.readline().split()))# вводим переменные и их погрешности
x = np.array(x)
plt.figure(figsize=(8,5), dpi=100)
plt.scatter(x,y,marker= '.')
plt.errorbar(x,y,xerr=xer,yerr=yer,color='k', linestyle='None') #ставим кресты погрешностей
y = np.array(y)
b = ((np.mean(x*y) - np.mean(x)*np.mean(y))/(np.mean(x ** 2) - (np.mean(x)) ** 2))
eb = (1/(len(x) ** (1/2)))*((((np.mean(y ** 2) - (np.mean(y)) ** 2)/(np.mean(x ** 2) - (np.mean(x)) ** 2)) - b ** 2) ** (1/2))
a = np.mean(y) - b*np.mean(x)
ea = eb*((np.mean(x ** 2) - (np.mean(x)) ** 2) ** (1/2)) #считаем коэфициенты и их погрешности
print('a =', a, '\n',"b =",b, '\n','Погрешность а =', ea, '\n','Погрешность b =', eb ) #выводим
xr = np.round(np.min(x))
XR = np.round(np.max(x))
yr = np.round(np.min(y)) 
YR = np.round(np.max(y))#определяем массив значений для функции (по факту это длина аппроксимационной прямой, у меня это минимальное и максимальное значения переменных, но можно свои) 
x2 = np.arange(xr, XR, 0.05) 
plt.plot(x2, b*x2 + a, color ='gray', label = f'{ 'b = ',round(float(b),2),'a=',round(float(a),2)}')#задаем график прямой и строим его
plt.title('Название графика', fontdict={'fontname': 'Times New Roman', 'fontsize': 20}) #называем график
plt.xlabel('писать сюда')
plt.ylabel('писать сюда') #называем оси
plt.xticks(np.arange(xr,XR, float(input())))
plt.yticks(np.arange(yr,YR, float(input()))) #наводим красоту :) а именно задаем сетку по осям Х и У 
plt.grid()
plt.legend()
plt.show() #выводим график
