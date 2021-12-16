# -*- coding: utf-8 -*-
"""Lessons_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15FRdhLvlSIqtzY7VUtxUTarH9fMhjxW1

1)вычисляет значения функций f 1 (x) = x/(x+100) и f 2 (x) = 1/x при изме-
нении x в диапазоне от 5 до 90 с шагом 1.
"""

def f1(x):
  x in range(5, 91, 1)
  return x/(x+100)

def f2(x):
  x in range(5, 91, 1)
  return 1/x

print(f1(8))
print(f2(8))

"""2) вычисляет значение функций f 3 (x) = 20*(f 1 (x) + f 2 (x))/x.

"""

def f3(x):
  x in range(5, 91, 1)
  return 20*(f1(x)+f2(x))/x

print(f3(9))

"""3) представляет результат в виде словаря следующего вида*: {x 1 : [f 1 (x 1 ),
f 2 (x 1 ), f 3 (x 1 )], x 2 : [f 1 (x 2 ), f 2 (x 2 ), f 3 (x 2 )], …};

"""

import pandas as pd
x1 = 8
x2 = 9
D = {x1:[f1(x1), f2(x1), f3(x1)],
     x2:[f1(x2), f2(x2), f3(x2)]}

df1 = pd.DataFrame(D)


print(df1)

"""4) сохраняет результат вычислений в CSV-файл, заголовком (столбцами)
которого являются значения x, f 1 (x), f 2 (x), f 3 (x);

"""

import openpyxl

book = openpyxl.Workbook()
sheet = book.active
book.save('C:\\Python_ML\\Lesson_3\\my_book.xlsx')
book.close()