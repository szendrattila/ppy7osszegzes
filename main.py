#1.1 Feladat

"""Készíts egy programot, amely [1;10] intervallumon generál 5 darab véletlen egész számot, és ezeket tárolja el egy listában! A program adja össze a lista elemeit, írja ki a képernyőre az összegüket és a lista elemeit"""
"""import random
szamok = []
for i in range(5):
    szamok.append(random.randint(1, 10))
print(f"A lista elemei: {szamok}")
print(f"a lista összege: {sum(szamok)}")"""

#---------------------------------

#1.2

"""
1.2 Feladat
Módosítsd úgy a fenti programot, hogy a program csak a páros számokat adja össze!
"""

"""
import random
szamok = []
parosszamok= []
for i in range(5):
    szamok.append(random.randint(1, 10))
print(f"A lista elemei: {szamok}")
for i in szamok:
    if i % 2 == 0:
        parosszamok.append(i)
print(f"A páros számok összege: {sum(parosszamok)}")
"""

#----------------------------------------

#2.

"""
2. Feladat
Írj egy programot, amely a felhasználótól kér be egész számokat [-5;5] intervallumban. A bekérés akkor fejeződjön be, amikor a felhasználó intervallumon kívüli értéket ad meg! A program írja ki a megadott intervallumba eső számokat és az összegüket!
"""
lista = []
while True:
    szam = int(input("Kérek egy számot [-5;5] : "))
    
    if szam >= -5 and szam <= 5:
        lista.append(szam)
    if szam < -5 or szam > 5:
        break
print(f"A bekért számok: {lista}")
print(f"A bekért számok összege : {sum(lista)}")

#--------------------------------------