#!/usr/bin/python
# -*-coding:Utf-8 -*

try:
	annee = input("Saississez une annêe en chiffre : ")
	annee = int(annee)
except:
	exit("Erreur lors de la conversion de l'annee")

bissextile = False

if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 != 0):
	print("L'annee est bissextile")
else:
	print("L'annee n'est pas bissextile")

