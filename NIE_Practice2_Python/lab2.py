from random import randint
import math
import xlsxwriter
import time

#СОРТИРОВКА ПУЗЫРЬКОМ

def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True
    return nums

#СОРТИРОВКА ВЫБОРКОЙ

def selection_sort(nums): #сортировка выборкой
    # Значение i соответствует кол-ву отсортированных значений
    for i in range(len(nums)):
        # Исходно считаем наименьшим первый элемент
        lowest_value_index = i
        # Этот цикл перебирает несортированные элементы
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Самый маленький элемент меняем с первым в списке
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums


#СОРТИРОВКА ВСТАВКАМИ

def insertion_sort(nums):
    # Сортировку начинаем со второго элемента, т.к. считается, что первый элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # Сохраняем ссылку на индекс предыдущего элемента
        j = i - 1
        # Элементы отсортированного сегмента перемещаем вперёд, если они больше
        # элемента для вставки
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Вставляем элемент
        nums[j + 1] = item_to_insert
    return nums

#Сортировка Шелла

def shellSort(array):
    n = len(array)
    k = int(math.log2(n))
    interval = 2**k -1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k -1
    return array

#БЫСТРАЯ СОРТИРОВКА

def partition(nums, low, high):
    # Выбираем средний элемент в качестве опорного
    # Также возможен выбор первого, последнего
    # или произвольного элементов в качестве опорного
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Если элемент с индексом i (слева от опорного) больше, чем
        # элемент с индексом j (справа от опорного), меняем их местами
        nums[i], nums[j] = nums[j], nums[i]

def quick_sort(nums):
    # Создадим вспомогательную функцию, которая вызывается рекурсивно
    def _quick_sort(items, low, high):
        if low < high:
            # This is the index after the pivot, where our lists are split
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)
    return nums

data = []
with open("result.txt") as f:
    for line in f:
        data.append([int(x) for x in line.split()])

file = ("sorted.xlsx")
book = xlsxwriter.Workbook(file)
sheet = book.add_worksheet()
sheet.set_column('A:K', 30)
bold = book.add_format({'bold': True})

sheet.write('A1', "Исходный массив", bold)
sheet.write('B1', "Пузырек", bold)
sheet.write('C1', "Время сортировки", bold)

sheet.write('D1', "Выборка", bold)
sheet.write('E1', "Время сортировки", bold)

sheet.write('F1', "Сортировка вставками", bold)
sheet.write('G1', "Время сортировки", bold)

sheet.write('H1', "Сортировка Шелла", bold)
sheet.write('I1', "Время сортировки", bold)

sheet.write('J1', "Быстрая сортировка", bold)
sheet.write('K1', "Время сортировки", bold)

for i in range(len(data)):
    for j in range(len(data[i])):
        sheet.write('A' + str(i + 2), str(data[i][j]))

key = 1

while key == 1:
    print(" Сортировка пузырьком - 1 \n Сортировка выборкой - 2 \n Сортировка вставками - 3 \n Сортировка Шелла - 4 \n Быстрая сортировка - 5 \n")
    method = int(input("Выберите вид сортировки: "))
    if(method == 1):
        try:
            ''' Сортировка данных '''
            sort_start = time.perf_counter()
            bubble_sort(data)
            sort_end = time.perf_counter()
            ''' Конец сортировки '''

            for i in range(len(data)):
                for j in range(len(data[i])):
                    sheet.write('B'+str(i+2),str(data[i][j]))

            sheet.write('C2',f"{sort_end - sort_start:0.4f} с")

            print("End of bubble sort")
        except:
            print("Произошли технические неполадки")

    elif (method == 2):
        try:
            sorted1 = []
            with open("result.txt") as f:
                for line in f:
                    sorted1.append([int(x) for x in line.split()])

            ''' Сортировка данных'''
            sort_start = time.perf_counter()
            selection_sort(sorted1)
            sort_end = time.perf_counter()
            ''' Конец сортировки '''

            for i in range(len(sorted1)):
                for j in range(len(sorted1[i])):
                    sheet.write('D'+str(i+2),str(sorted1[i][j]))

            sheet.write('E2', f"{sort_end - sort_start:0.4f} с")

            print("End of selection sort")
        except:
            print("Произошли технические неполадки")
    elif (method == 3):
        try:
            sorted2 = []
            with open("result.txt") as f:
                for line in f:
                    sorted2.append([int(x) for x in line.split()])

            ''' Сортировка данных '''
            sort_start = time.perf_counter()
            insertion_sort(sorted2)
            sort_end = time.perf_counter()
            ''' Конец сортировки '''

            for i in range(len(sorted2)):
                for j in range(len(sorted2[i])):
                    sheet.write('F'+str(i+2),str(sorted2[i][j]))

            sheet.write('G2', f"{sort_end - sort_start:0.4f} с")
            print("End of insertion sort")
        except:
            print("Произошли технические неполадки")
    elif (method == 4):
        try:
            sorted3 = []

            with open("result.txt") as f:
                for line in f:
                    sorted3.append([int(x) for x in line.split()])

            ''' Сортировка данных '''
            sort_start = time.perf_counter()
            shellSort(sorted3)
            sort_end = time.perf_counter()
            ''' Конец сортировки '''

            for i in range(len(sorted3)):
                for j in range(len(sorted3[i])):
                    sheet.write('H' + str(i + 2), str(sorted3[i][j]))

            sheet.write('I2', f"{sort_end - sort_start:0.4f} с")
            print("End of shell sort")
        except:
            print("Произошли технические неполадки")
    elif (method == 5):
        try:
            sorted4 = []

            with open("result.txt") as f:
                for line in f:
                    sorted4.append([int(x) for x in line.split()])

            ''' Сортировка данных '''
            sort_start = time.perf_counter()
            quick_sort(sorted4)
            sort_end = time.perf_counter()
            ''' Конец сортировки '''

            for i in range(len(sorted4)):
                for j in range(len(sorted4[i])):
                    sheet.write('J' + str(i + 2), str(sorted4[i][j]))

            sheet.write('K2', f"{sort_end - sort_start:0.4f} с")

            print("End of quick sort")
        except:
            print("Произошли технические неполадки")
    else:
        print("Неправильно указан метод сортировки")
        break

    key = int(input("Введите 1 для продолжения: "))
book.close()
print("Посмотрите результат в созданным xlsx файле")