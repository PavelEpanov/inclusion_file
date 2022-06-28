my_list = [1, 2, 3, 4, 5]
a = [x ** 2 for x in my_list] # Генератор значения

###

def func(x):
    return x ** 2

b = list(map(func, my_list)) # map Использует функцию, НЕ ВЫРАЖЕНИЕ
c = list(map(lambda x: x ** 2, my_list)) # То же самое,что и b
print(a)
print(b)
print(c)

k = [x ** x for x in range(10)]
print(k)

###

m = [x for x in range(1, 11) if x % 2 == 0] # if после for заместо filter И MAP И FILTER В ОДНОМ ВЫРАЖЕНИИ
print(m)

M = list(filter(lambda x: x % 2 == 0, range(1, 11))) # то же самое, что и m
print(M)

resolution = []
for x in range(1, 11):
    if x % 2 == 0:
        resolution.append(x)
print(resolution) # То же самое что и m M

g = [x ** 2 for x in range(1, 11) if x % 2 == 0] # Пропускает все числа кратные 2 и возводит в 2 степень
print(g)

###

G = [x + y for x in [1, 2, 3] for y in [100, 200, 300]] # Сначала находится x и y, а позже происходит вычисление
print(G)

res = [] # То же самое что и G, но разложено по for
for x in [1, 2, 3]:
    for y in [100, 200 ,300]:
        res.append(x + y)
print(res)

low = []
high = []
for x in "абвгдеёжзийклмнопрстуфхцчшщъыьэюя":
    low.append(x)
for x in "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ":
    high.append(x)
l = [x + y for x in low for y in high]
print(l)

o = [x + y for x in "spam" if x in "sm" for y in "SPAM" if y in ("P", "A")] # Если x == s or m and if y == P or A
print(o)

t = [(x, y) for x in range(10) if x % 2 == 0 for y in range(10) if y % 2 == 1]
print(t)

###

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
natrix = [
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]

ale = [i[1] for i in matrix] # i - здесь номер списка в списке
print(ale)

aleba = [matrix[i][1] for i in (0, 1, 2)] # i - здесь тоже номер списка в списке
print(aleba)

diag_one = [matrix[i][i] for i  in range(len(matrix))] # Нахождение диагонали
print(diag_one)
diag_two = [matrix[i][len(matrix) -1 - i] for i in range(len(matrix))] # Нахождение диагонали
print(diag_two)

lem = [col + 10 for i in matrix for col in i] # i - это все значения в матрице, col - присваевается i, происходит выражение col + 10 ТО ЕСТЬ ДОСТАЛИ ВСЕ ЧИСЛА ИЗ МАТРИЦЫ И ПРИБАВЛИ 10
print(lem)

lem2 = [[col + 10 for col in row] for row in matrix]
print(lem2)

resm = []
for i in matrix:
    tmp = []
    for col in i:
        tmp.append(col + 10)
    resm.append(tmp)
print(resm)

# natrix = [
#     [2, 2, 2],
#     [3, 3, 3],
#     [4, 4, 4]
# ]

mech = [[matrix[row][col] * natrix[row][col] for col in range(3)] for row in range(3)]
print(mech)

mech2 = []
for row in range(3):
    tmp2 = []
    for col in range(3):
        tmp2.append(matrix[row][col] * natrix[row][col])
    mech2.append(tmp2)
print(mech2)



