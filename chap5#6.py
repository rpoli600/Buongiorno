sum1=0
for j in range(1,1000):
    maxi=int(j/2)+1
    for i in range(1,maxi):
        if (j%i==0):
            sum1=sum1+i
            #print('j = ',j,'sum1 = ',sum1)
    if (sum1==j):
        print(sum1,'is a perfect number')
    sum1=0
    sumt=sum1+j
    sumd=sum1-1
    #print('somma incluso 1: ',sum1)
    #print('somma incluso tutto: ',sumt)
    #print('somma escluso 1 e se stesso: ',sumd)
