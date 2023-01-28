
n = int(input('Введите трехзначное число: '))
if n <= 999 and n > 99:
    a = n // 100
    b = n % 100 // 10
    c = n % 10
    s = (a+b+c)
    print(s)
else:
    print('Это не трехзначное число: ')





