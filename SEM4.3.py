import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('iris_data.csv')
pl = list(df['PetalLengthCm'])
s = list(df['Species'])
pl1 = [pl[i] for i in range(len(pl)) if pl[i] <= 1.2]
pl2 = [pl[i] for i in range(len(pl)) if pl[i] > 1.2]
d = 1
c = []
name = []
for i in range(len(s)):
    if s[i-1] == s[i]  and i != len(s)-1:
        d += 1
    else:
        name.append(s[i])
        if i == len(s)-1:
            c.append(d+1) 
        else:
            c.append(d)
            d = 1
c.pop(0)
name.pop(-1)
c = np.array(c)
c =list(map(float, c/len(s)))
c = [round(c[i], 3) for i in range(len(c))]
f = plt.figure(figsize=(3,4), dpi = 200)
g1 = f.add_subplot(211)
g2 = f.add_subplot(212)
g1.pie([len(pl1)/len(pl),len(pl2)/len(pl)],labels =['PetalLengthCm <= 1.2','PetalLengthCm > 1.2'] )
g2.pie(c, labels = name)
plt.show()
