import random #Импорт модуля random 
size = random.randint(4, 8) #Генерация размера матрицы
values = [-3, -5, -2, -12, 0, 15, 4, 7, 2] #Создание списка с допустимыми значениями
matriс = [[random.choice(values) for i in range(size)] for i in range(size)] #Создаем матрицы
for i in matriс: #Используем цикл for
    print(" ".join(f"{elem:>3}" for elem in i)) #Выводим матрицу
suma = sum(elem for row in matriс for elem in row if elem < 0) #Cуммирование отрицательных чисел
print(f"Сумма отрицательных элементов: {suma}") #Вывод суммы отрицательных чисел