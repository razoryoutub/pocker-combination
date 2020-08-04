import os
import colorama
from colorama import init
from colorama import Fore
from colorama import Back
import time
os.system('cls')
init(autoreset=True)
cards = ['tuz_ch','two_ch','three_ch','four_ch','five_ch','six_ch','seven_ch','eight_ch','nine_ch','ten_ch','jack_ch','queen_ch','king_ch','tuz_bu','two_bu','three_bu','four_bu','five_bu','six_bu','seven_bu','eight_bu','nine_bu','ten_bu','jack_bu','queen_bu','king_bu','tuz_kr','two_kr','three_kr','four_kr','five_kr','six_kr','seven_kr','eight_kr','nine_kr','ten_kr','jack_kr','queen_kr','king_kr','tuz_pi','two_pi','three_pi','four_pi','five_pi','six_pi','seven_pi','eight_pi','nine_pi','ten_pi','jack_pi','queen_pi','king_pi',]
card_num = [0,0,0,0,0,0,0,0,0,0,0,0,0]
par_count = 0
set_count = 0
for i in range(0,13):
	print(Fore.RED + Back.WHITE + str(i+1) + ')' + cards[i])
for i in range(13,26):
	print(Fore.WHITE + Back.RED + str(i+1) + ')' + cards[i])
for i in range(26,39):
	print(Fore.BLACK + Back.WHITE + str(i+1) + ')' + cards[i])
for i in range(39,52):
	print(Fore.WHITE + Back.BLACK + str(i+1) + ')' + cards[i])

a = [0,0,0,0,0,0,0]
for i in range(0,7):
	try:
		a[i] = int(int(input(':'))-1)
		print(cards[a[i]])
	except ValueError:
			os.system('cls')
			print("нужно было число...")
			exit()
os.system('cls')
ch = 0
bu = 0
kr = 0
pi = 0
max = -1
p_count = 0
p_max = -1
for i in range(0,7):
	if a[i]<13:
		card_num[a[i]]+=1
		if a[i]>max:
			max = a[i]
	if (a[i]>=13) and ((a[i]<26)):
		card_num[a[i]-13]+=1
		if a[i]-13>max:
			max = a[i]-13
	if (a[i]>=26) and ((a[i]<39)):
		card_num[a[i]-26]+=1
		if a[i]-26>max:
			max = a[i]-26
	if a[i]>=39:
		card_num[a[i]-39]+=1
		if a[i]-39>max:
			max = a[i]-39
	if (str(cards[a[i]])[-2:]) == 'ch':
		ch+=1
	elif (str(cards[a[i]])[-2:]) == 'bu':
		bu+=1
	elif (str(cards[a[i]])[-2:]) == 'kr':
		kr+=1
	elif (str(cards[a[i]])[-2:]) == 'pi':
		pi+=1
if (ch >= 5) or (bu >= 5) or (kr >= 5) or (pi >= 5):
	print('Флеш')
print('Старшая - ' + cards[max])
for i in range(0,7):
	if card_num[i] != 0:
		p_count+=1
	else:
		if p_count > p_max:
			p_max = p_count
		p_count = 0
	if card_num[i] == 4:
		print("Каре")
	elif card_num[i] == 2:
		par_count+=1
	if card_num[i] == 3:
		print("Сет (тройка)")
		set_count+=1
if p_count > p_max:
			p_max = p_count
if (par_count == 1) and (set_count == 1):
	print("Фулл хаус")
elif par_count == 2:
	print("Две пары")
elif par_count == 1:
	print("Пара")
if p_max >= 5:
	print('Стрит')
if (p_max >= 5) and ((ch >= 5) or (bu >= 5) or (kr >= 5) or (pi >= 5)):
	print('Стрит Флеш')
if ((card_num[0] != 0) and (card_num[9] != 0) and (card_num[10] != 0) and (card_num[11] != 0) and (card_num[12] != 0)):
	print('Флеш Рояль!!!')
"""
print('\n-------developinfo-------')
print('количество карт(туз-кароль):')
print(card_num)
print('количество пар: ' + str(par_count))
print('количество троек: ' + str(set_count))
print('черви: {0}\nбуби: {1}\nкрести: {2}\nпики: {3}'.format(ch,bu,kr,pi))
print('максимум карт: ' + str(p_max))
"""