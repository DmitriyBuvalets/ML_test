# -*- coding: utf-8 -*-
"""Lesson_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vm_uvHk-e8Rht3YytXsxqd4n4kw41j2V

**1. Загрузить данные в Colab**
"""

#Для загрузки с локального диска начните со следующего кода:

from google.colab import files
uploaded = files.upload()

df1 = pd.read_table('dataset.txt', sep =' ')
print(df1)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#df = open("dataset.txt", "r")
dp = pd.read_table('dataset.txt', sep =' ')

print(dp.head())

df = pd.DataFrame(dp)

print(df)

df.columns

"""**2. Построить графики**

**Линейный график**
"""

# color цвет графика
df.plot(x='X', y='Y', color="blue")
plt.grid()
plt.title("Линейный график")
# Изменить фон
ax = plt.axes()
ax.set_facecolor("yellow")
#*************************
plt.show()

"""**Столбчатая диаграмма**"""

#%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.array(df["X"])
y = np.array(df["Y"])

fig, ax = plt.subplots()

ax.bar(x, y)

ax.set_facecolor('yellow')
fig.set_facecolor('floralwhite')
fig.set_figwidth(12)    #  ширина Figure
fig.set_figheight(6)    #  высота Figure
plt.grid()
plt.show()

"""**Stem-график**"""

import numpy as np
import matplotlib.pyplot as plt

x = np.array(df["X"])
y = np.array(df["Y"])
plt.grid()
plt.stem(x, y)
plt.show()

"""**Ступенчатый** **график** """

import numpy as np
import matplotlib.pyplot as plt
 
fig = plt.figure(figsize=(7, 5))
ax = fig.add_subplot()
 
x = np.array(df["X"])
ax.step(x, x)
ax.grid()
 
plt.show()

"""3. Найти максимальное значение"""

x = np.array(df["X"])
y = np.array(df["Y"])

max_number_x = max(x)
max_number_y = max(y)


print("Наибольшее число x & y:", max_number_x," ",max_number_y)

import matplotlib.pyplot as plt
x = np.array(df["X"])
y = np.array(df["Y"])

first_ten = slice(10)
x = np.array(df["X"])
x = x[first_ten]

xd1 = -max(list(x))
xd = max(list(x))
print(xd1, xd)

x = list(range(xd1, xd))
y = [i**2 for i in x]

print(x, y)

plt.annotate('max', xy=(8, 64), xycoords='data',
xytext=(0, 10),
textcoords = 'data',
arrowprops = {"width": 7})
plt.plot(x, y)
plt.show()
#plt.plot(x, marker="o")
#plt.annotate("point", (9,10), (1, 25), size=14, color="red", arrowprops = {"width": 7})
#plt.show()

"""**4. Умножить Y на 2**"""

x = np.array(df["X"])
y = np.array(df["Y"])

y1 = [i**2 for i in y]

print(y1)

"""Для визуализации и читабельности данные Y уможены на 0,5"""

import matplotlib.pyplot as plt

x = np.array(df["X"])
y = np.array(df["Y"])

y1 = [i*0.5 for i in y]
# color цвет графика
plt.plot(x, y, color="blue")
plt.plot(x, y1, color="green")
plt.grid()
plt.title("Линейный график")
# Изменить фон
ax = plt.axes()
ax.set_facecolor("yellow")
#*************************
plt.show()