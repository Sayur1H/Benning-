import random

chracthers="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
remenber = int(input("Qual tamanho da sua senha?"))
lock = ""

for i in range(remenber):
    lock += random.choice(chracthers)

print(lock)
