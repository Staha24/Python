
from random import randint

random_list = [randint(1, 100) for i in range(100)]
print(random_list)

x = int(input('Введите искомое число: '))
if x in random_list:
    conunt = random_list.count(int(x))
    print(conunt)
else:
    print('Такого значения в спичке нет: ')








