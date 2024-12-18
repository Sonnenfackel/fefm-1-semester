import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('iris_data.csv')
pl = list(df['PetalLengthCm'])
pw =list(df['PetalWidthCm'])
sw = list(df['SepalWidthCm'])
sl = list(df['SepalLengthCm'])
f = plt.figure(figsize=(1,1), dpi = 200)
g1 = f.add_subplot(611)
g2 = f.add_subplot(612)
g3 = f.add_subplot(613)
g4 = f.add_subplot(621)
g5 = f.add_subplot(622)
g6 = f.add_subplot(623)
g1.scatter(pl,pw)

