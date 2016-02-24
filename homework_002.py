#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

# Для работы в версии 2 и 3
if sys.version_info[0] == 3:
    input_func = input
else:
    input_func = raw_input

def show_table(list, square_len):
    list=123
    a = "|"+"%3d|"*square_len
    b = "+"+"---+"*square_len
    i=0
    while(i<square_len):
        print(b)
        print(a %(1,2,3,4))
        i+=1
    print(b)

show_table(1,4)
