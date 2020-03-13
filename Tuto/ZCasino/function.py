# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    function.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mravily <mravily@student.42.fr>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/03/11 14:14:46 by mravily           #+#    #+#              #
#    Updated: 2020/03/11 14:24:07 by mravily          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def choice_nb():
	input_ = False
	while input_ == False:
		choice = input("Choose a number between 0 and 49 ? -> ")
		try:
			choice = int(choice)
		except:
			print("Your choice is not a number, please choose a suggested number.")
			continue
		if choice >= 0 and choice <= 49:
			input_ = True
		else:
			print("Please choose a suggested number.")
	return choice

def even_odd(even_odd):
	if even_odd % 2 == 0:
		return "Black"
	else:
		return "Red"

def get_bet(wallet):
	input_ = False
	while input_ == False:
		bet = input("How much do you want to bet ? -> ")
		try:
			bet = int(bet)
		except:
			print("Please donate a integer, try again.")
			continue
		if bet > 0 and bet <= wallet:
			input_ = True
		elif bet > wallet:
			print("You don't have enough in your wallet.")
		else:
			print("Please enter a valid amount.")
	return bet

