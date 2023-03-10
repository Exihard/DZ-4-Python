# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло
# различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического
# сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль
# за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки. | 4 -> 1 2 3 4 9 |

from random import randint
Shrub = list(randint(1, 5) for i in range(int(input('Введите количество кустов: '))))
print(Shrub)
a = int(input('Введите № куста: '))
res = 0
if a == 1:
    res = Shrub[0] + Shrub[1] + Shrub[-1]
elif a == len(Shrub):
    res = Shrub[-2] + Shrub[-1] + Shrub[0]
else:
    res = Shrub[a-1] + Shrub[a-2] + Shrub[a]
if res > 4:   
    print(res, 'ягод')
else:
    print(res, 'ягоды')