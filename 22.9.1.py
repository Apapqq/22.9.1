def increasing(array):       # сортировка выбором
    for i in range(len(array) - 1):
        num1 = i
        num2 = i + 1
        while num2 < len(array):
            if array[num2] < array[num1]:
                num1 = num2
            num2 = num2 + 1
        array[i], array[num1] = array[num1], array[i]

def binary_search(array, num, left, right): 
    if left > right: # если левая граница превысила правую,
        return False # значит элемент отсутствует
    
    middle = (right+left) // 2 # находимо середину
    if array[middle] == num: # если элемент в середине,
        return middle # возвращаем этот индекс
    elif num < array[middle]: # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, num, left, middle-1)
    else: # иначе в правой
        return binary_search(array, num, middle+1, right)


    

numbers = [int(i) for i in input('Введите последовательность чисел, через пробел: ').split()]
num_min = min(numbers)
num_max = max(numbers)
num = int(input('Введите второе число: '))
if num_min > num:   # проверка числа
    print('Введите число больше или равное %s: ' % num_min)
    num = int(input('Введите второе число: '))
    increasing(numbers)
    print('Ваши отсортированные числа:',*numbers)          # сортировка выбором, вывод массива
    array = numbers    
    print('Индекс вашего числа: ',binary_search(array, num, 0, len(array)))
elif num_max < num:
    print('Введите число меньше или равное %s: ' % num_max)
    num = int(input('Введите второе число: '))
    increasing(numbers)
    print('Ваши отсортированные числа:',*numbers)          # сортировка выбором, вывод массива
    array = numbers    
    print('Индекс вашего числа: ',binary_search(array, num, 0, len(array)))
else:
    increasing(numbers)
    print('Ваши отсортированные числа:',*numbers)          # сортировка выбором, вывод массива
    array = numbers    
    print('Индекс вашего числа: ',binary_search(array, num, 0, len(array)))
    

