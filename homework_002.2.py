# -*- coding: utf-8 -*-

import random  # see https://docs.python.org/2/library/random.html
import sys

EMPTY_MARK = ' '

# Для работы в версии 2 и 3
if sys.version_info[0] == 3:
    input_func = input
    range_func = range
else:
    input_func = raw_input
    range_func = xrange

def shuffle_field():
    field = list(range_func(15))
    field.append(EMPTY_MARK)
    random.shuffle(field)
    return field


def print_field(field):
    formatter_line = "   |"+"%3s|"*4
    line = "   +"+"---+"*4
    i=0
    while(i<16):
        print(line)
        print(formatter_line % (tuple(field[i:i+4])))
        i+=4
    print(line + "\n")
    return None


def is_game_finished(field):
    finish_field = list(range_func(15))
    finish_field.append(EMPTY_MARK)
    return (finish_field == field)

def perform_move(field, key):
    x = field.index(EMPTY_MARK)
    if key == 'a':
        if ( x - 1 >= 0 and (x-1) not in (7,11,15)):
            field[x],field[x-1] = field[x-1],field[x]
        else:
            raise IndexError()
    elif key == 's':
        if (x + 4 <= 16):
            field[x],field[x+4] = field[x+4],field[x]
        else:
            raise IndexError()
    elif key == 'w':
        if (x - 4 >= 0):
            field[x],field[x-4] = field[x-4],field[x]
        else:
            raise IndexError()
    elif key == 'd':
        if (x + 1 <= 16 and (x+1) not in (4,8,12)):
            field[x],field[x+1] = field[x+1],field[x]
        else:
            raise IndexError()
    return field


def handle_user_input():
    while True:
        movement = input_func(">>>")
        if movement in ('w','s','a','d'):
            return movement
        else:
            print (u"Куда жмешь?!")

def show_rules():
    print(u" Все очень просто. Двигая пустую клетку, надо собрать такую же таблицу:\n")
    field_f = list(range_func(15))
    field_f.append(EMPTY_MARK) 
    # Разбить лист на N частей. Магия из справочника Python.
    print_field(field_f)
    print(u"\n Как соберете - так и выиграете.\n А если не соберете - тогда вас съест Путин.")

def show_banner():
    print("\n"*80)
    print(" "*3 + "*"*50)
    print(" "*3 + "**" + " "*46 + "**")
    print(" "*3 + "**" + " "*5 + " Super-Puper-Mega-Pyatnashki ver.0.2 " + " "*4+ "**")
    print(" "*3 + "**" + " "*46 + "**")
    print(" "*3 + "*"*50)

def show_movement_rules():
    print(" "*10 + "="*30)
    print(" "*20 + "Like in GTA 5 :-) ")
    print(" "*10 + u"   w - Движение вверх")
    print(" "*10 + u"   s - Движение вниз")
    print(" "*10 + u"   a - Движение влево")
    print(" "*10 + u"   d - Движение вправо")
    print(" "*10 + "="*30)

def nice_print(matrix):
    show_banner()
    show_movement_rules()
    print_field(matrix)

def main():
    show_banner()
    show_rules()
    print(u"\n Для продолжения нажмите Enter...")
    input_func(">>>")
    matrix = shuffle_field()

    nice_print(matrix)
    print(" ") # Для выравнивания
    while True:
        movement = handle_user_input()
        try:
            matrix = perform_move(matrix, movement)
            nice_print(matrix)
        except IndexError:
            nice_print(matrix)
            print(u" ДЕРЖИТЕ НАРКОМАНА!!! Так ходить нельзя.")
        else:
            print(" ") # Тоже, для выравнивания
        if is_game_finished(matrix):
            print(u" А вот и победитель!\n ..:: Game Over ::..")
            break
    return None

# see http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__': 
    main()
