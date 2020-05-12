anno = eval(input('scrive l"'"anno che t"'"interessa: '))
if (anno%4==0):
    if(anno%100==0 and anno%400>0):
        print(anno,' non e bisestile')
    else:
        print(anno,' e bisestile')
else:
    print(anno,' non e bisestile')
