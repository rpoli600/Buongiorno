from tkinter import *
def calculate():
    temp=float(entry.get())
    temp =9/5*temp+32
    output_label.configure(text='Convertita a °F: {:.1f}'.format(temp))
   # entry.delete(0,END)
root=Tk()
message_label=Label(text='Temperatura in °C = ',font=('Verdana' ,16), fg='red',
                    bg='white')
message_label1=Label(text='Tutto fatto', font=('Ebrima', 16, 'bold'), fg='blue', bg='white')
output_label=Label(font=('Verdana',16))
entry=Entry(font=('Verdana',16), width=4)
calc_button=Button(text='ok',font=('Verdana', 16), command = calculate)
message_label.grid(row=0, column=0)
entry.grid(row=0, column=1)
calc_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)
message_label1.grid(row=2, column=0)
mainloop()
