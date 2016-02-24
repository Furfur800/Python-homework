#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys
import random

# Для работы в версии 2 и 3
if sys.version_info[0] == 3:
    input_func = input
    range_func = range
else:
    input_func = raw_input
    range_func = xrange

EMPTY_MARK = " "

def matrix_gen(num=4, final=False):
    matrix = list(range_func(num**2))
    matrix.pop(0)
    matrix.append(EMPTY_MARK) 
    if final == False:
        random.shuffle(matrix)
    # Разбить лист на N частей. Магия из справочника Python.
    matrix = zip(*[iter(matrix)] * num) 
    for x in matrix[:]:
        matrix.remove(x)
        matrix.append(list(x))
    return matrix

def show_table(matrix, square_len=4):
    #matrix
    a = "|"+"%3s|"*square_len
    b = "+"+"---+"*square_len
    i=0
    while(i<square_len):
        print(b)
        print (a % (tuple(matrix[i])))
        i+=1
    print(b)

def show_rules():
    pass

def coords(matrix):
    for i,line in enumerate(matrix):
        if EMPTY_MARK in line:
            y = line.index(EMPTY_MARK)
            x = i
    return x, y

def move(matrix, move_char):
    x, y = coords(matrix)
    if move_char == 'h' or move_char == 'a':
        if (y - 1 >= 0):
            matrix[x][y],matrix[x][y-1] = matrix[x][y-1],matrix[x][y]
        else:
            raise IndexError()
    elif move_char == 'j' or move_char == 's':
        matrix[x][y],matrix[x+1][y] = matrix[x+1][y],matrix[x][y]
    elif move_char == 'k' or move_char == 'w':
        if (x - 1 >= 0):
            matrix[x][y],matrix[x-1][y] = matrix[x-1][y],matrix[x][y]
        else:
            raise IndexError()
    elif move_char == 'l' or move_char == 'd':
        matrix[x][y],matrix[x][y+1] = matrix[x][y+1],matrix[x][y]
    elif move_char == 'q':
        print(u"Сдался, слабак?")
        exit()
    else:
        print(u"Нет такой клавиши!")
    return matrix


print (u"Введите длину поля (2 - 15)")
try:
    num = int(input_func(">>>"))
    if num > 15 or num < 2:
        num = 4
except ValueError:
    num = 4
matrix = matrix_gen(num)
show_table(matrix, num)

while True:
    movement = input_func(">>>")
    try:
        matrix = move(matrix,movement)
    except IndexError:
        print(u"ДЕРЖИ НАРКОМАНА!!! (Так ходить нельзя.)")
    show_table(matrix,num)
    if (matrix == matrix_gen(num, True)):
        print(u"А вот и победитель!!!!!")

# # Задача: реализовать игру Пятнашки
# Условия задачи:
# В начале игры создается поле размером 4 на 4, в каждом квадрате которого - число (15 суммарно), плюс один квадрат - пустой. В начале игры квадраты перемешаны в случайном порядке.
# Пользователь может двигать пустой квадрат вверх, вниз, вправо и влево. Если двигать пустой квадрат нельзя по причине границы поля - пользователю нужно выдать сообщение об ошибке.
# Игра считается завершенной, когда все квадраты стоят по порядку, пустой квадрат стоит в правом нижнем углу.
# Технические требования:
# Программа должна реализовывать предоставленный интерфейс и проходить тесты, которое к нему написаны.
# Задачи на усложнение:
# Код должен проходить проверку PEP8