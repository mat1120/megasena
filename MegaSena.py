from random import randint
from time import sleep
lista = []
jogos = []
print("-" * 30)
print("     JOGA NA MEGA SENA")
c = 0
print("-" * 30)
jogo = int(input("Quantos jogos voce quer sortear? "))
tot = 1
while tot <= jogo:
    c = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            c += 1
        if c >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos):
    print("jogo {}:{}".format(i + 1, l))
    sleep(1)