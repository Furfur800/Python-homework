#!/usr/bin/python
#-*- coding: utf-8 -*-

import sys

# Для работы в версии 2 и 3
if sys.version_info[0] == 3:
    input_func = input
else:
    input_func = raw_input

def banner():
    print("\n"*50)
    print("+" + "-" * 63 + "+")
    print("|" + " " * 63 + "|")
    print("|" + " " * 15 + u">>> Python-Викторина ver.0.0.0.1 <<<" + " " * 12 + "|")
    print("|     ____        __  __                               _ _____  |")
    print("|    / __ \__  __/ /_/ /_  ____  ____     ____ ___  __(_)__  /  |")
    print("|   / /_/ / / / / __/ __ \/ __ \/ __ \   / __ `/ / / / /  / /   |")
    print("|  / ____/ /_/ / /_/ / / / /_/ / / / /  / /_/ / /_/ / /  / /__  |")
    print("| /_/    \__, /\__/_/ /_/\____/_/ /_/   \__, /\__,_/_/  /____/  |")
    print("|       /____/   >>> Relizeng by 0x67     /_/                   |")
    print(u"|   >>> Greetings to: 0x66, 0x68 (вы всегда рядом, пацаны)      |")
    print("|" + " " * 63 + "|")
    print("+" + "-" * 63 + "+\n")

def stat(right, wrong, narko):
    print(" "*3+"*"* 33)
    print(" "*3+u"***  Правильных ответов: %4d ***" % right)
    print(" "*3+u"***  Неправильных ответов: %2d ***" % wrong)
    print(" "*3+u"***  Наркоманских ответов: %2d ***" % narko)
    print(" "*3+"*"*33+"\n")

def rules():
    print(u" Правила чрезвычайно просты (до безумия). Читаете вопрос.\n Выбираете правильный ответ. Вводите его число (только число!) и жмете Enter.\n Числа меньше 1, числа большие чем количество ответов и любые другие символы будут считаться наркоманией.\n В отношение нарушителей будут введены санкции (укол галоперидола внутримышечно).\n")

def question(some,num):
    print (">>")
    if sys.version_info[0] == 3:
        print (u">> Вопрос №"+ str(num) +" "+some[0])
    else:
        print (u">> Вопрос №"+ str(num) +" "+some[0].decode('utf8'))
    print (">>\n")
    i=1
    while(i<len(some)-1):
        if sys.version_info[0] == 3:
            print (u"\t "+ str(i) + u". " + str(some[i]))
        else:
            print (u"\t "+ str(i) + u". " + str(some[i]).decode('utf8'))
        i+=1

right = wrong = narko = i = 0

#Массив вопросов и ответов.
#Первый элемент - вопрос, далее - варианты ответа, последний элемент - номер правильного ответа
qa_array = \
    ["Вы прочитали и усвоили правила?","Да","Нет","Мне нужен укол галоперидола...",1],\
    ["Как зовут основателя языка Питон?","Книга и Опоссум","Гвидо ван Россум","Гиви иван Русский","мл. науч. сотрудник Пуговкин Михаил Маргаритович",2],\
    ["Что выведет этот код?\n>>\n>>\tFilm = True\n>>\tprint(Film + Film + Film)","True","True True True","1","Будет выведена ошибка","3","42",5],\
    ["В честь кого (или чего) был назван язык Питон?","В честь змеи","В честь юмористической передачи Е.В.Петросяна","В честь английской юмористической передачи","В челюсть",3],\
    ["Что выведет этот код?\n>>\n>>\tbe = False\n>>\tto = False\n>>\tquestion = be or not to + be\n>>\tprint(question)","True","False","None","Будет выведена ошибка",1],\
    ["Для чего нужен синтаксический сахар?","Сабж + синтаксические дрожжи = синтаксический самогон","Чтобы человеку было удобнее программировать","Чтобы завернуть умную фразу перед друзьями в Старбаксе",2],\
    ["Что выведет этот код?\n>>\n>>\tprint(str(bool(str(False)[0]))[0])","0","1","False","True","F","r","T",7],\
    ["Сколько отступов должно быть перед блоком кода?","1","4","8","1488","Отступов может быть сколько угодно, важно чтобы их количество было одинаковым",5],\
    ["Есть два ноутбука. На одном Python 2.7 включенный, на втором Python 3.4 запущённый. \n>> Какой код какому Python'у отправишь? \n>>\t 1. print 'Hello world'\n>>\t 2. print(u'Hello world')","Первый - на 2.7, Второй - на 3.4","Первый - на 3.4, Второй - на 2.7","Оба кода отправлю на 2.7","Оба кода отправлю на 3.4",3],\

while(True):
    banner()
    if (i==0):
        rules()
    if (i > len(qa_array)-1):
        stat(right,wrong,narko)
        if(sys.platform == 'win32'):
        	print("   Game Over...   ")
        else:
        	# Цветной вывод - https://habrahabr.ru/post/119436/
        	print("  \033[41m   Game over...  \033[0m\n\n")
        break
    question(qa_array[i],i)
    answer = input_func("\n>>")
    try:
        if (int(answer) == qa_array[i][-1]):
            right +=1
            i +=1
        elif(int(answer)>len(qa_array[i]) or int(answer)<1):
            narko +=1
        else:
            wrong +=1
    except ValueError:
        narko +=1