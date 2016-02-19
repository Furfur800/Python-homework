#-*- coding: utf-8 -*-

import sys


# Для работы в версии 2 и 3
if sys.version_info[0] == 3:
	input_func = input
else:
	input_func = raw_input

def show_banner():
	print("\n"*10)
	print("+" + "-" * 50 + "+")
	print("|" + " " * 50 + "|")
	print("|" + " " * 5 + "..:: Чудо-Чудо-Викторина! ::.." + " " * 5 + "|")
	print("|" + " " * 50 + "|")
	print("+" + "-" * 50 + "+")

#arr_qa = [[["123"]['12']], [["222"]['333']], [["333"]['123']]]
#print (arr_qa[0][0])

show_banner()