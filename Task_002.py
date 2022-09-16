# Задача 2. В файле находятся названия фруктов. 
# Выведите все фрукты, названия которых начинаются 
# на заданную букву.


letter = 'а'
with open('fruit.txt', encoding="UTF-8") as file:
    read = file.readlines()
    read_str = ''.join(read).lower()
    splited = read_str.split()
    for i in splited:
        if letter in i:
            print(i)
    
    
    
