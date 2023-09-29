import random
karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
pr1uzunluk = int(input("Parolanız kaç karakterden oluşmasını istersiniz?"))

sifre = "" 

for i in range(pr1uzunluk) :
    sifre = sifre+random.choice(karakter)

print (sifre)
