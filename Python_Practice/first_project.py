import tkinter as tk
from tkinter import ttk
from tkinter import filedialog,messagebox,colorchooser,font
import os

win=tk.Tk()
win.title('First Project')
win.geometry('1300x700+0+0')

# label frame
labelframe=ttk.LabelFrame(win,text='User Details')
labelframe.place(x=500,y=200)


#       labels
useremail=ttk.Label(labelframe,text='Enter ur email :')
useremail.grid(row=0,column=0,padx=11,pady=11)

password=ttk.Label(labelframe,text='Enter ur password :')
password.grid(row=1,column=0,padx=11,pady=11)


#               entry box
email_var=tk.StringVar()
emailentry=ttk.Entry(labelframe,width=17,textvariable=email_var,font=('Agency fb',20,'bold'))
emailentry.grid(row=0,column=1,padx=5)
emailentry.focus()

pass_var=tk.StringVar()
passwordentry=ttk.Entry(labelframe,width=17,textvariable=pass_var,font=('Agency fb',20,'bold'))
passwordentry.grid(row=1,column=1,padx=5)


#       check button

#               functionality
url=''

def save_data(event=None):
    content=email_var.get()
    content2=pass_var.get()
    with open ('file.txt','a',encoding='utf-8') as fa:
        fa.write(f'email is {content} and password is {content2} ' + '\n')
        


log_in=ttk.Button(labelframe,text='Log In',command=save_data)
log_in.grid(row=3,columnspan=3)


win.mainloop()