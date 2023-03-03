#!/usr/bin/env python
# coding: utf-8

# # Numpy

# Материалы:
# * Макрушин С.В. "Лекция 1: Библиотека Numpy"
# * https://numpy.org/doc/stable/user/index.html
# * https://numpy.org/doc/stable/reference/index.html

# ## Задачи для совместного разбора

# 1. Сгенерировать двухмерный массив `arr` размерности (4, 7), состоящий из случайных действительных чисел, равномерно распределенных в диапазоне от 0 до 20. Нормализовать значения массива с помощью преобразования вида  $𝑎𝑥+𝑏$  так, что после нормализации максимальный элемент масcива будет равен 1.0, минимальный 0.0

# In[1]:


import numpy as np


# In[2]:


x = np.random.uniform(0,20,size = (4,7))
x


# 2. Создать матрицу 8 на 10 из случайных целых (используя модуль `numpy.random`) чисел из диапозона от 0 до 10 и найти в ней строку (ее индекс и вывести саму строку), в которой сумма значений минимальна.

# In[3]:


x = np.random.randint(0,10, size = (8,10))
print(x)
a = np.sum(x,axis = 1 )
print(a)
np.argmin(a)


# 3. Найти евклидово расстояние между двумя одномерными векторами одинаковой размерности.

# In[4]:


a,b = np.random.randint(0, 15, size = (1,3)), np.random.randint(0, 15, size = (1,3))
distance = np.linalg.norm(a-b)
distance


# 4. Решить матричное уравнение `A*X*B=-C` - найти матрицу `X`. Где `A = [[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]]`, `B=[[3, -1], [2, 1]]`, `C=[[7, 21], [11, 8], [8, 4]]`.

# In[5]:


a = np.array([[-1, 2, 4], [-3, 1, 2], [-3, 0, 1]])
b = np.array([[3, -1], [2, 1]])
c = np.array([[7, 21], [11, 8], [8, 4]])
c_neg = c*(-1)
x = np.dot(np.linalg.inv(a), c_neg)
x_final = np.dot(x,  np.linalg.inv(b))
np.trunc(x_final)


# ## Лабораторная работа №1

# Замечание: при решении данных задач не подразумевается использования циклов или генераторов Python, если в задании не сказано обратного. Решение должно опираться на использования функционала библиотеки `numpy`.

# 1. Файл `minutes_n_ingredients.csv` содержит информацию об идентификаторе рецепта, времени его выполнения в минутах и количестве необходимых ингредиентов. Считайте данные из этого файла в виде массива `numpy` типа `int32`, используя `np.loadtxt`. Выведите на экран первые 5 строк массива.

# In[4]:


import numpy as np


# In[5]:


a = np.loadtxt('minutes_n_ingredients.csv',dtype=int, delimiter=',', skiprows=1)
a[0:5,]


#  2. Вычислите среднее значение, минимум, максимум и медиану по каждому из столбцов, кроме первого.

# In[6]:


column1 = a[:,0]
column2 = a[:,1] 
column3 = a[:,2]


# In[7]:


#for 2nd column
avg_column2 = np.average(column2)
min_column2 = np.min(column2)
max_column2 = np.max(column2)
median_column2 = np.median(column2)
print('Среднее значение для второго столбца = ', avg_column2, '\nМинимум для второго столбца =', min_column2, '\nМаксимум для второго столбца = ', max_column2, '\nМедиана для второго столбца = ', median_column2)
avg_column2, min_column2, max_column2, median_column2


# In[8]:


#for 3rd column
avg_column3 = np.average(column3)
min_column3 = np.min(column3)
max_column3 = np.max(column3)
median_column3 = np.median(column3)
print('Среднее значение для третьего столбца = ', avg_column3, '\nМинимум для третьего столбца =', min_column3, '\nМаксимум для третьего столбца = ', max_column3, '\nМедиана для третьего столбца = ', median_column3)


# 3. Ограничьте сверху значения продолжительности выполнения рецепта значением квантиля $q_{0.75}$. 

# In[9]:


q = np.quantile(column2, 0.75)
a[:,1] = np.clip(column2, 0, int(q))
column2


# 4. Посчитайте, для скольких рецептов указана продолжительность, равная нулю. Замените для таких строк значение в данном столбце на 1.

# In[10]:


num_zeros = (column2 == 0).sum()
a[:,1] = np.clip(column2, 1, int(q))
num_zeros, column2


# 5. Посчитайте, сколько уникальных рецептов находится в датасете.

# In[11]:


unique = np.unique(a, axis=1)
len(unique)           


# 6. Сколько и каких различных значений кол-ва ингредиентов присутвует в рецептах из датасета?

# In[12]:


lst = list(column3.copy())
unique = list(set(lst))
frequency = {}
for item in unique:
    frequency[item] = lst.count(item)
print("Всего различных значений кол-ва ингридиентов = ", len(unique),"\nСколько раз встречаются различные значения кол-ва ингридиентов = ", frequency)


# 7. Создайте версию массива, содержащую информацию только о рецептах, состоящих не более чем из 5 ингредиентов.

# In[13]:


not_greater_5 = []
for k in range(0,len(a)):
    if column3[k] <= 5:
        not_greater_5.append(a[k])
not_greater_5 = np.array(not_greater_5)
not_greater_5


# 8. Для каждого рецепта посчитайте, сколько в среднем ингредиентов приходится на одну минуту рецепта. Найдите максимальное значение этой величины для всего датасета

# In[14]:


ratio = []
for k in range(1, len(a)):
    ratio.append(column3[k]/column2[k])
print('Максимальное значение = ',max(ratio),'\nСреднее количество ингредиентов на одну минуту для каждого рецепта:',*ratio, sep="\n", end="\n\n")


# 9. Вычислите среднее количество ингредиентов для топ-100 рецептов с наибольшей продолжительностью

# In[15]:


top_100 = a.copy()
top_100 = top_100[top_100[:, 1].argsort()[::-1]][:100]
average_100 = np.average(top_100[:,2])
average_100


# 10. Выберите случайным образом и выведите информацию о 10 различных рецептах

# In[16]:


print('   ID     Timing    N_Ingridients')
for m in range(1,11):
    index = np.where(a[:,0] == np.random.choice(column1))
    print(a[index])


# 11. Выведите процент рецептов, кол-во ингредиентов в которых меньше среднего.

# In[17]:


l = 0
for i in range(1,len(a)):
    if column3[i]<avg_column3:
        l+=1
print((l/len(a))*100,'%', sep='')


# 12. Назовем "простым" такой рецепт, длительность выполнения которого не больше 20 минут и кол-во ингредиентов в котором не больше 5. Создайте версию датасета с дополнительным столбцом, значениями которого являются 1, если рецепт простой, и 0 в противном случае.

# In[18]:


k=0
c = []
simple = a.copy()
for m in range(0, len(a)):
    if simple[m,1] <= 20 and simple[m,2] <=5:
        c.append(1)
        k+=1
    else:
        c.append(0)
simple = np.column_stack((simple,c))
simple


# 13. Выведите процент "простых" рецептов в датасете

# In[19]:


print(k/len(a)*100,'%', sep='')


# 14. Разделим рецепты на группы по следующему правилу. Назовем рецепты короткими, если их продолжительность составляет менее 10 минут; стандартными, если их продолжительность составляет более 10, но менее 20 минут; и длинными, если их продолжительность составляет не менее 20 минут. Создайте трехмерный массив, где нулевая ось отвечает за номер группы (короткий, стандартный или длинный рецепт), первая ось - за сам рецепт и вторая ось - за характеристики рецепта. Выберите максимальное количество рецептов из каждой группы таким образом, чтобы было возможно сформировать трехмерный массив. Выведите форму полученного массива.


# In[37]:
# 0 axis: 0 - short, 1 - standart, 2 - long
# 1 axis: index of recipie
# 2 axis: id, time, n_ingrid
# In[59]:
short = []
standart = []
long = []
for i in range(0, len(a)):
    if a[i,1] < 10:
        short.append(a[i])
    elif a[i,1] >= 10 and a[i,1] < 20:
        standart.append(a[i])
    elif a[i,1] >= 20:
        long.append(a[i])
m = min(len(short), len(standart), len(long))
standart = standart[:m]
short = short[:m]
long = long[:m]
d3 = np.stack((short,standart,long), axis=0)
d3[2,2,0], long[:5]
