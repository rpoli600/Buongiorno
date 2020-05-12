import math
anno=eval(input('Pasqua di quale anno? '))
C=anno//100
x="nn"
y="nn"
m=(15+C-C//4-(8*C + 13)//25)%30
if(m==2 or m==5 or m==10 or m==13 or m==16 or m==2 or m==24 or m==39):
    x="yy"
n=(4+C-C//4)%7
a=anno%4
b=anno%7
c=anno%19
d=(19*c+m)%30
e=(2*a+4*b+6*d+n)%7
print('m = ',m,' n = ',n,' d = ',d,' e = ',e,' x = ',x,' y = ',y) 
if(d==29 and e==6):
    y="yy"
if (y== "nn"):
    data1=22+d+e
    data2=d+e-9
    print('data di Pasqua per anno: ',anno,' = Marzo: ',data1,' oppure Aprile: ',data2)
elif(x=="nn" and y=="yy"):
    data3=19
    print('data di Pasqua per anno: ',anno,' = Aprile: ',data3)
elif(d==28 and e==6 and x=="yy" and y=="nn"):
    data4=18
    print('data di Pasqua per anno: ',anno,' = Aprile: ',data4)
else:
    print("Non trovo la data di Pasqua")
