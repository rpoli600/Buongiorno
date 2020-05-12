from random import randint
score=0
for i in range(0,5):
    num=eval(input('indovina il numero tra 1 e 10: ----> '))
    print('  ')
    numero=randint(1,10)
    if (num==numero):
        score=score+10
        print('Hai indovinato!!! ',numero)
    else:
        print('Noooo! il numero e: ',numero)
print('  ')
print('punti finali = ',score)
