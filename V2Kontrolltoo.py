#V2
#1
while True:
    try:
        n=int(input("Sisesta number 1-9: "))
        if 1<=n<=9:
            break
        else:
            print("Palun sisesta number 1-9.")
    except:
        print("Palun sisesta kehtiv number.")
for i in range(n):
            print("(\_/)")
            print("(o o)")
            print("/ | \\*")
            print()

#2
while True:
    try:
        n=int(input("Sisesta number: "))
        if n<0:
            print("Sisesta positiivne arv")
        else:
            kõik=0
            for i in range(n+1):
                kõik+=i
            print(kõik)
            break
    except:
        print("Sisesta täisarv!")

#3
import random
number=random.randint(0, 100)
katsed=0

for k in range(10):
    while True:
        try:
            arvan=int(input("Sisesta number 0-100: "))
            if number<arvan:
                print("Number on vähem!")
            if number>arvan:
                print("Number on suurem!")
            if number==arvan:
                print("See on õigus")
            katsed+=1
            if katsed==10:
                print(f"Arvasid valesti! Õige vastus on {number}")
            break
        except:
            print("Viga!")

#4
a=3486
b=0
while a>0:
    number=a%10
    a=a//10
    b=b*10
    b+=number
print(b)

#5 EI OLNUD MINU TEHTUD

number = int(input("Sisesta täisarv: "))

summ = 0
korrutis = 1
stringArv = str(number)

for i in range(len(stringArv)):
    iArv = int(stringArv[i])
    print(iArv)
    summ += iArv
    korrutis *= iArv

print(f"Summa on {summ}, korruts on {korrutis}")





