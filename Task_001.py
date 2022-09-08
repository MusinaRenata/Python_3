# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-2) + fibonacci(i-1)

for x in range(6):
    print(fibonacci(x))