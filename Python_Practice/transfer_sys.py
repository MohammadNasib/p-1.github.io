import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg


class transfer(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('900x500')


    def main(self):

        f1=LabelFrame(self,bg='light blue')
        f1.place(x=300,y=150)

        l1=Label(f1,text='Change directry',font=('agencyfb',15))
        l1.grid(padx=11,pady=11,sticky=W)

        dir_var=StringVar()
        e1=Entry(f1,textvariable=dir_var)
        e1.grid(row=0,column=1,padx=11,pady=11)


        l2=Label(f1,text='New File',font=('agencyfb',15))
        l2.grid(row=1,column=0,padx=11,pady=11,sticky=W)


        new_var=StringVar()
        e2=Entry(f1,textvariable=new_var)
        e2.grid(row=1,column=1,padx=11,pady=11)

       
        l3=Label(f1,text='File Name',font=('agencyfb',15))
        l3.grid(row=2,column=0,padx=11,pady=11,sticky=W)

        entry_var=StringVar()
        e3=Entry(f1,width=19,textvariable=entry_var)
        e3.grid(row=2,column=1,padx=11,pady=11)

#                   submit button
        def transfer_func():
            dir=dir_var.get()
            new=new_var.get()
            file=entry_var.get()

            os.chdir(dir)
            with open (f'{file}','r') as rf:
                r=rf.read()
                with open(f'{new}','a') as af:
                    af.write(f'\n\n\n\n\n\n{file}  \n\n\n\n\n\n  {r}  \n\n\n\n\n\n  ')
                    
        b1=Button(f1,text='Transfer',command=transfer_func)
        b1.grid(row=5,columnspan=5)

#   help button
        def help_func():
            a=msg.showinfo('Help',f'In the change directry enter ur file location.\n EX--C:\\Users\\Lenovo\\practice1')
       
        h=Button(f1,text='Need help to use this system ?',font=('agencyfb',10,'bold'),command=help_func)
        h.grid(row=6,column=3)


if __name__ == "__main__":
    win=transfer()
    win.main()

    win.mainloop()