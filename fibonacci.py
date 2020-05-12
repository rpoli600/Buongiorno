numero=eval(input('quanti numeri di Fibonacci vuoi: '))
F1=1
F2=2
print(1,F1,sep=' -- > ')
print(2,F2,sep=' -- > ')
for i in range(3,numero+1):
    F3=F1+F2
    F1=F2
    F2=F3
    print(i,F3,sep = ' -- > ')
print('numero di Fibonacci = ',numero)
