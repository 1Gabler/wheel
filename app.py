from pywebio import start_server
from pywebio.input import *
from pywebio.output import *
from pywebio.session import defer_call, info as session_info, run_async, run_js
from functools import partial
from random import randint
from time import sleep
from os import system, name

def main():
	Wallet = 1000
	user = 0
	while Wallet != 0:
		put_markdown("# 🎰 Добро пожаловать в Wheel, друг)\nМы дали тебе косарь, постарайся преумножить его!!")
		put_markdown("`1 - зеленый (шанс 1/36)`\n`2 - черный (шанс 1/2)`\n`3 - красный (шанс 1/2)`")
		put_text('*при вводе ставки, если вы ошиблись цветом введите 0').style('font-family: Consolas; color: #b3b2d7;')
		put_markdown('	Баланс: ' + str(Wallet)).style('font-weight: bold;')

		while user != 'зеленый' or user != 'черный' or user != 'красный':
			user = input('Ведите цвет')
			if user == '1':
				user = 'зеленый'
				break
			elif user == '2':
				user = 'черный'
				break
			elif user == '3':
				user = 'красный'
				break
			else:
				toast('Неверное значение. Попробуйте снова')
				user = 0

		while True:
			money = input('Введите ставку')
			if money.isdigit() == True:
				money = int(money)
				if money == 0:
					break
				elif money <= Wallet:
					Wallet -= money
					break
				else:
					toast('у тебя столько нет в кошельке, давай другую сумму')
			else:
				toast('Неверное значение. Попробуйте снова')

		a = randint(0, 36)
		if a == 0:
			casino = 'зеленый'
		elif 1 <= a <= 10 or 19 <= a <= 28:
			if a % 2 == 0:
				casino = 'черный'
			else:
				casino = 'красный'
		elif 11 <= a <= 18 or 29 <= a <= 36:
			if a % 2 == 0:
				casino = 'красный'
			else:
				casino = 'черный'
		if money == 0:
			sleep(0.001)  
			clear()
			continue
		elif casino == user:
			if casino == 'зеленый':
				money = money * 36
				Wallet += money
				toast('	большой выйгрыш ура!) +' + str(money) + ' 👽')  #.style('color: green; font-size: 20px')
			elif casino == 'черный' or casino == 'красный':
				money = money * 2
				Wallet += money
				toast('	нормик выйгрыш)  +' + str(money) + ' 🤑')  #.style('background: #eafff2; color: green; font-size: 15px')  
		else:
			toast('	ты проиграл. надо было ставить на ' + casino + ' -' + str(money) + ' 😢')  #.style('background: #ffebeb; color: red; font-size: 15px')
		sleep(0.001)  
		clear()
	put_markdown('	GAME OVER (ты все проебал)💔').style('margin-top: 100px;background: #202020; color: #ffffff; font-size: 30px; text-align: center;')

start_server(main, port=8080, debug=True, websocket_ping_interval=30)