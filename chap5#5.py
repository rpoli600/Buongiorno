sum1=0
n = eval(input('écrit un numéro entre 10 et 10000: '))
maxi=int(n/2)+1
for i in range(1,maxi):
    if (n%i==0):
        sum1=sum1+i
sumt=sum1+n
sumd=sum1-1
print('somma incluso 1: ',sum1)
print('somma incluso tutto: ',sumt)
print('somma escluso 1 e se stesso: ',sumd)
