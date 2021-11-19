#this is the first verion of number game

#import

import random
import time

#functions


def rInt (x, y):
	return random.randint(x, y)

#vars

#random number
CPUnumber = rInt(0, 10)

#none = null
PLAYERnumber = None

#numbers

numbers = [CPUnumber, PLAYERnumber]

#console

while (True):
	PLAYERinputOne = input("(1).Comecar o jogo\n(2).Sobre\n(3).Sair\nDigite: ")

	if (PLAYERinputOne == "1"):
		numbers[1] = int(input("Digite o numero: "))
		print("Sera?")
		time.sleep(3)

		if (numbers[1] == numbers[0]):
			print("\nAcertou!")
		else:
			print("\nErrou! O numero e {}".format(numbers[0]))

	if (PLAYERinputOne == "2"):
		print("\nEste e um jogo de adivinhacao, onde voce tem que imaginar um numero de 1 a 10\n")

	if (PLAYERinputOne == "3"):
		break
