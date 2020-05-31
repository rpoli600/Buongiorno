numero=eval(input('scrive un numero intiero: '))
lista=[]
#j=1
quadrato=False
maxi=numero//2+1
for i in range(2,maxi):
    if (numero%i==0):
        lista.append(i)
        #j=j+1
    k=i*i
    if (numero%k==0):
        print('numero is not squarefree: ',k,' is a divisor')
        quadrato=True
if (quadrato==False):
    print(numero,' is squarefree')
print('list of divisors of ',numero,' is: ', lista)

