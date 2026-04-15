from random import seed, randint
seed(10)
print("🐍Змейка🐍")
print()

#Меню
menu = """w. Вверх ⬆️
s. Вниз ⬇️
d. Вправо ➡️
a. Влев о⬅️
"""
print()
print("Выберите персонажа")
print( """Например:
🐍
🦎
🦖
🐲
🧟
или что-то своё""")
pers = str(input("персонаж: "))
print()
print()
print("Выберите еду")
print( """Например:
🍎
🍓
🍒
🍔
🥩
👶
или что-то своё""")
eat = str(input("еда: "))
print()
print()
print("Выберите фон")
print( """Например:
⬜️
🟩
🟨
🍃
🌱
или что-то своё""")
fon = str(input("фон: "))
print()

# 1. Создание поля
print("Введите размер поля:")
lst = []
n = int(input())
for _ in range(n):
    lst.append([fon for _ in range(n)])

#Яблоко
a_y = randint(0, n-1)
a_x = randint(0, n-1)
lst[a_y][a_x] = eat

#Копия поля
lst_copy = [i.copy() for i in lst]

#Змейка
snake = []
sn_start_h_y = sn_start_h_x = n//2
sn_new_p = [sn_start_h_y, sn_start_h_x]
snake.append(sn_new_p)

for sn_p in snake:
    sn_p_y = sn_p[0]
    sn_p_x = sn_p[1]
    lst_copy[sn_p_y][sn_p_x] = pers

for i in lst_copy:
    print(*i)

#Движение змейки

print(menu)
sn_muve = str(input())
while sn_muve != "0":
    sn_h = snake[0]
    sn_h_y = sn_h[0]
    sn_h_x = sn_h[1]
    if sn_muve == "w":
        sn_h_y -= 1
        
    elif sn_muve == "s":
        sn_h_y +=1
        
    elif sn_muve == "a":
        sn_h_x -=1
        
    elif sn_muve == "d":
        sn_h_x +=1
        
    new_h = [sn_h_y, sn_h_x]
    snake.insert(0, new_h)
    if not(0 <= new_h[0] <= n) or not(0 <= new_h[1] <= n) == True:
        print("Произошло столкновение со стеной! Игра окончена.")
        sn_muve = "0"
    else:
        if lst[sn_h_y][sn_h_x] != eat:
            snake.pop()
        else:
            lst[a_y][a_x] = fon
            a_y = randint(0, n-1)
            a_x = randint(0, n-1)
            lst[a_y][a_x] = eat

        lst_copy = [i.copy() for i in lst]
        for sn_p in snake:
            sn_p_y = sn_p[0]
            sn_p_x = sn_p[1]
            lst_copy[sn_p_y][sn_p_x] = pers


        for i in lst_copy:
            print(*i)
        print(menu)
        sn_muve = str(input())
