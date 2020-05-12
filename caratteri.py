stri=input('scrivi una frase o stringa di caratteri: ')
l=len(stri)
k=stri[0]
ls=stri[-1]
c=''
for i in range(1,4):
    c=c+stri[-4+i]
rts=''
for i in range(1,len(stri)+1):
    rts=rts+stri[-i]
sette=stri[6]
st=''
for i in  range(1,len(stri)-1):
    st=st+stri[i]
CAP=stri.upper()
stru=stri
cc='a'
stra=stri+'\n'
stru=stru.replace(cc,'e')        
print('lunghezza di stri: ',l)
print(stra*10)
print('primo carattere di stri: ',k)
print('ultimo carattere di stri: ',ls)
print('ultimi tre carattere di stri: ',c)
print('stri all\'inverso: ',rts)
print('settimo carattere: ',sette)
print('stri con primo e ultimo carattere tolti: ',st)
print('stri in maiuscola: ',CAP)
print('stri con e in posto di a: ',stru)
      
