# Практическая работа №1. Вариант 1


# Задание №1

from math import *
x= float(input("Введите x: "))
y= float(input("Введите y: "))
z= float(input("Введите z: "))

t = (2*float(cos(x-(pi/6))))/(0.5+float(pow(float(sin(y)),2)))*(1+float((pow(z,2))/(3-float((pow(z,2)/5)))))
print(t)

# Задание №2

num1 = int(input("Введите число: "))
num2 = int(input("Введите число: "))
num3 = int(input("Введите число: "))
numbers=[num1,num2,num3]
for num in numbers:
    if num >=1 and num <= 3:
        print("Число",num, "принадлежит интервалу [1,3]")
    else:
        print("")

# Задание №3
price = float(input("Введите число: "))
for i in range(1,10):
    print("Цена за",i,"килограмм конфет=", i*price)


count = int(input("Введите количество чисел: "))
i = 0
sum=0
numbers = []
# Задание 3.2
while i < count:
    num = int(input("Введите число: "))
    if num %10==0:
        numbers.append(num)
        sum+=num
    else:
        print("Число должно быть кратно 10 ")
    i+=1

print("\n Сумма чисел:", sum,"\n Количество чисел: ", len(numbers))