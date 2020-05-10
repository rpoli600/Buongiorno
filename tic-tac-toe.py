from tkinter import *
root=Tk()
name_frame=Frame()
#name_frame_1=Frame()
def callback(r,c):
    global player,n
    if (player == 'X' and states[r][c] == 0 and stop_game==False):
        b[r][c].configure(text='X', fg='blue', bg='white')
        states[r][c] = 'X'
        player = 'O'
        n=1
    if (player == 'O' and states[r][c] == 0 and stop_game==False):
        b[r][c].configure(text='O', fg='orange', bg='black')
        states[r][c] = 'O'
        player = 'X'
        n=2
    check_for_winner()
    finestra()

def finestra():
    nome1=entry1.get()
    nome2=entry2.get()
    nome_label1.configuration(text='giocatore #1: '.format(nome1))
    nome_label2.configuration(text='giocatore #2: '.format(nome2))

def check_for_winner():
    global stop_game
    #k=i+2
    for i in range(3):
        if states[i][0]==states[i][1]==states[i][2]!=0:
            b[i][0].configure(bg='red')
            b[i][1].configure(bg='red')
            b[i][2].configure(bg='red')
            stop_game = True
    for i in range(3):
        if states[0][i]==states[1][i]==states[2][i]!=0:
            b[0][i].configure(bg='red')
            b[1][i].configure(bg='red')
            b[2][i].configure(bg='red')
            stop_game = True
    if states[0][0]==states[1][1]==states[2][2]!=0:
        b[0][0].configure(bg='red')
        b[1][1].configure(bg='red')
        b[2][2].configure(bg='red')
        stop_game = True
    if states[2][0]==states[1][1]==states[0][2]!=0:
        b[2][0].configure(bg='red')
        b[1][1].configure(bg='red')
        b[0][2].configure(bg='red')
        stop_game = True
    if (stop_game):
        if (n==1):
            entry1.configure(bg='red')
        else:
            entry2.configure(bg='red')
        
        
#root = Tk()

b = [[0,0,0],
        [0,0,0],
        [0,0,0]]
states = [[0,0,0],
        [0,0,0],
        [0,0,0]]
nome_label1=Label(text='Nome del giocatore #1:',
    font=('Verdana', 15))
nome_label2=Label(text='Nome del giocatore #2:',
    font=('Verdana', 15))
entry1 = Entry(font=('Verdana', 15), width=12,bg='white')
entry2 = Entry(font=('Verdana', 15), width=12, bg='white')
nome_label1.grid(row=1, column=0)
nome_label2.grid(row=2,column=0)
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)
#name_frame.grid(row=1,column=0)
for i in range(3):
    for j in range(3):
        b[i][j] = Button(name_frame,font=('Verdana', 56), width=3, bg='yellow',
            command = lambda r=i,c=j: callback(r,c))
        b[i][j].grid(row = i, column = j)
name_frame.grid(row=0,column=0)
#b[0][1]=entry1
#b[1][1]=entry2
#b[0][0]=entry1
#b[1][0]=entry2
player = 'X'
stop_game = False

#root1 = Tk()

#finestra()


mainloop()
