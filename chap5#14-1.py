from random import randint
print('THERE ARE 4 DOORS. BEHIND ONE OF THESE DOORS THERE IS A PRIZE')
print('OF ONE MILLION DOLLARS. I WILL TELL YOU ONE OF THE DOORS THAT DOES NOT')
print('CONTAIN THE PRIZE. YOU MUST SELECT ONE OF THE OTHER THREE')
print('THERE ARE 10 TRIALS')
print('GOOD LUCK!!!!')
win=0
lost=0
for j in range(1,10):
    porta=[0,0,0,0,0]
    i=randint(1,4)
    porta[i]=100
    if (i==4):
        k=i-3
        i1=i
        i2=3
        i3=2
    elif (i==3):
        k=i-1
        i1=1
        i2=i
        i3=4
    elif(i==2):
        k=i+1
        i3=4
        i2=1
        i1=i
    else:
        k=i+1
        i2=4
        i1=3
        i3=i
    #print('i =',i,'k = ',k)
    #print('door ',k,' = ',porta[k])
    print('door ',i1,' door ',i2,' or door ',i3,' contains the prize',' door ',k,' does NOT contain it')
    num=eval(input('choose one of these other three doors:'))
    while(num==k):
        print('choose either ',i1,' or ',i2,' or ',i3)
        num=eval(input('choose one of these other three doors:'))
    if (porta[num]==100):
        print('You chose correctly!!!!')
        win=win+1
    else:
        lost=lost+1
print('you chose correctly ',win,' of the 10 times')

