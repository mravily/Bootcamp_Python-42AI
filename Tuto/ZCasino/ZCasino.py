from random import randrange
from math import ceil
from function import *

wallet = 100
input_ = False
print("Welcome to the ZCasino")
while input_ == False:
	answer = input("Would you like to play roulette ? (yes) or (no) -> ")
	try:
		answer = int(anwser)
	except:
		if answer == "yes" or answer == "y":
			input_ = True
		elif answer == "no" or answer == "n":
			exit("Too bad, thanks, and see you soon at the ZCasino.")
		else:
			print("That's not the answer we're looking for.")
print("\nTake a seat, here's a wallet with $", wallet ,"that you can bet, ENJOY !")
while wallet != 0:
	choice = choice_nb()
	even_odd = choice
	if even_odd % 2 == 0:
		even_odd = "Black"
	else:
		even_odd = "Red"
	print("\nYou have chosen the number", choice, "which is placed on the color", even_odd, ".")
	bet = get_bet(wallet)
	print("\nYou just bet $", bet, "on the number", choice, "in", even_odd, ".", "Place your bets, no more bets\n")
	wallet -= bet
	roulette = randrange(50)
	even_odd_roulette = roulette
	if even_odd_roulette % 2 == 0:
		even_odd_roulette = "Black"
	else:
		even_odd_roulette = "Red"
	print("\nThe winning number is", roulette , even_odd_roulette, ".")
	if roulette == choice:
		print("Congratulations! You just won 3 times your bet, or $", 3 * bet, ".")
		wallet += bet * 3
	elif even_odd_roulette == even_odd:
		print("\nToo bad, you didn't pick the right winning number, but you have the same color.")
		print("You get 50% of your bet (+$",ceil(bet / 2),")")
		wallet += ceil(bet / 2)
	else:
		print("\nToo bad you didn't win anything, you'll have better luck next time.")
	input_ = False
	while input_ == False:
		if wallet != 0:
			answer = input("\nWould you like to play again ? (yes) or (no) -> ")
		else:
			exit("\nYou don't have any money left to play at the roulette table. Goodbye LOOSER !")
		try:
			answer = int(anwser)
		except:
			if answer == "yes" or answer == "y":
				input_ = True
			elif answer == "no" or answer == "n":
				exit("Too bad, thanks, and see you soon at the ZCasino.")
			else:
				print("That's not the answer we're looking for.")
	print("\nHappy to count you among us, you have $", wallet, "in your wallet.")
	continue

