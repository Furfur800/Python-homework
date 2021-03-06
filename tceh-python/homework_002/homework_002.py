#!/usr/bin/python
#-*- coding: utf-8 -*-

# Tested on:
# MacOS - Python 2.7, 3.4
# Win - Python 2.7

import sys
import random

# Для работы в версии 2 и 3
if sys.version_info[0] == 3:
    input_func = input
    range_func = range
else:
    input_func = raw_input
    range_func = xrange

EMPTY_MARK = error = " "

def matrix_gen(num=4, final=False):
    matrix = list(range_func(num**2))
    matrix.pop(0)
    matrix.append(EMPTY_MARK) 
    if final == False:
        random.shuffle(matrix)
    # Разбить лист на N частей. Магия из справочника Python.
    matrix = list(zip(*[iter(matrix)] * num))
    for x in matrix[:]:
        matrix.remove(x)
        matrix.append(list(x))
    return matrix

def show_table(matrix, square_len=4):
    formatter_line = "   |"+"%3s|"*square_len
    line = "   +"+"---+"*square_len
    i=0
    while(i<square_len):
        print(line)
        print(formatter_line % (tuple(matrix[i])))
        i+=1
    print(line + "\n")

def show_rules(num):
    print(u" Все очень просто. Двигая пустую клетку, надо собрать такую же таблицу:\n")
    show_table(matrix_gen(num, True),num)
    print(u"\n Как соберете - так и выиграете.\n А если не соберете - тогда вас съест Путин.")

def show_movement_rules():
    print(" "*10 + "="*30)
    print(" "*20 + "games & vim")
    print(" "*10 + u"   w, k - Движение вверх")
    print(" "*10 + u"   s, j - Движение вниз")
    print(" "*10 + u"   a, h - Движение влево")
    print(" "*10 + u"   d, l - Движение вправо")
    print(" "*10 + u"      q - Сдаться")
    print(" "*10 + "="*30)

def show_banner():
    print("\n"*80)
    print(" "*3 + "*"*50)
    print(" "*3 + "**" + " "*46 + "**")
    print(" "*3 + "**" + " "*5 + " Super-Puper-Mega-Pyatnashki ver.0.2 " + " "*4+ "**")
    print(" "*3 + "**" + " "*46 + "**")
    print(" "*3 + "*"*50)

def coords(matrix):
    for i,line in enumerate(matrix):
        if EMPTY_MARK in line:
            y = line.index(EMPTY_MARK)
            x = i
    return x, y

def move(matrix, move_char):
    global error
    x, y = coords(matrix)
    if move_char in ('h','a'):
        if (y - 1 >= 0):
            matrix[x][y],matrix[x][y-1] = matrix[x][y-1],matrix[x][y]
        else:
            raise IndexError()
    elif move_char in ('j', 's'):
        matrix[x][y],matrix[x+1][y] = matrix[x+1][y],matrix[x][y]
    elif move_char in ('k', 'w'):
        if (x - 1 >= 0):
            matrix[x][y],matrix[x-1][y] = matrix[x-1][y],matrix[x][y]
        else:
            raise IndexError()
    elif move_char in ('l','d'):
        matrix[x][y],matrix[x][y+1] = matrix[x][y+1],matrix[x][y]
    elif move_char == 'q':
        print(u" Сдался, слабак? Сдался...\n Напиши об этом в ЖЖ.")
        exit()
    elif move_char =='666':
        #Чит-код для выигрыша
        matrix = matrix_gen(len(matrix),True)
    else:
        error=u" НАРКОМАН, по клавишам не попадаешь?"
    return matrix

#Выбор уровня сложности
show_banner()
print (u" Введите длину поля (от 2 до 10, Enter/Anykey+Enter - 4):")
try:
    num = int(input_func(">>>"))
    if num > 15 or num < 2:
        num = 4
except ValueError:
    num = 4
show_rules(num)
matrix = matrix_gen(num)
print(u"\n Для продолжения нажмите Enter...")
input_func(">>>")

#Основной цикл
while True:
    show_banner()
    show_movement_rules()
    if (matrix == matrix_gen(num, True)):
        show_table(matrix, num)
        print(u" А вот и победитель!\n ..:: Game Over ::..")
        break
    show_table(matrix, num)
    if (error != ""):
        print(error)
        error = ""
    else:
        print(" ")
    movement = input_func(">>>")
    try:
        matrix = move(matrix, movement)
    except IndexError:
        error=u" НАРКОМАН, краев не видишь?"
