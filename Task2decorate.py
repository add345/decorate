
#Дополнительное: Напишите следующие функции: 
# Нахождение корней квадратного уравнения 

import math

print('ax^2+bx+c')

a = int(input('Введите a = '))

b = int(input('Введите b = '))

c = int(input('Введите c = '))

def square_eq(a, b, c):
    
    result = []
    
    D = b ** 2 - 4 * a * c

    if D == 0:
        x = -b / (2 * a)
        print('Дискриминант D равен 0. Имеет один корень:')
        print('x =', x)
        result = [x]

    if D < 0:
        print('Вещественных корней нет')
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print('Дискриминант D больше 0. Имеет два корня:')
        print('x1 =', x1, 'x2 =', x2)
        result = [x1, x2]
        
    return result

square_eq(a, b, c)