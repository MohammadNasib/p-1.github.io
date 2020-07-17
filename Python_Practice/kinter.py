from tkinter import *       #   for this i don't need to write tkinter for all time
from tkinter import ttk
from tkinter import messagebox as msg
from PIL import Image,ImageTk
import time


win=Tk()
#  ---------------------------------------------------this is starting  --------------------------------------------------------
#       geometry

win.geometry('900x400') #      ' width x hight'

# win.resizable(0,0)          #this is resizable

# win.minsize(200,100)  #        width,hight

# # win.maxsize(3000,2000)   #        width,hight




#               label


#           important label option

# text---- adds the text
# bd------- background
# fg------- foreground
# font----- all about font
# padx----- x fadding
# padyy----- y padding
# relief---- border styling----> SUNKEN, RAISED, GROOVE, RIDGE

# label1=Label(text='this is label ....',fg='White',bg='red',padx=20,pady=22,font=('agency fb', 30 ,'bold' ,'italic'),borderwidth=3,relief=RIDGE)





#           image

#               for png file

# photo=PhotoImage(file='image/index.png') 

#           for jpg file
# image=Image.open('image/index2.jpg')
# photo=ImageTk.PhotoImage(image)

# image_label=Label(image=photo)
# image_label.pack()




#           Important Pack options

# anchor = 'nw'
# side = 'top', 'bottom', 'left','right'
# fill
# padx
# pady

# label1.pack(anchor='n')
# label1.pack(side='bottom')
# label1.pack(fill=BOTH)




# #                   frame
# f1=Frame(win,borderwidth=5,relief=SUNKEN)
# f1.pack(side=TOP,anchor='center',pady=4)

# l1=Label(f1,text='this is frame',fg='blue',bg='black',font=('agency fb',20,'bold'))
# l1.pack()





#               button
# def func():
#     print('funtion called')

# b1=Button(f1,fg='green',text='print now',font=('agency fb',13,'bold'),command=func).pack()




#               grid
# user=Label(f1,text='user input :',font=('comicsansms '),fg='green')
# user.grid(padx=5,pady=5)

# passw=Label(f1,text='user pass :',font=('comicsansms '),fg='green')
# passw.grid(row=1,padx=5,pady=5)


#                   entry box

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

# uservalue=StringVar()
# passvalue=StringVar()

# userentry=Entry(f1,textvariable=uservalue,bg='light blue').grid(row=0,column=1,padx=5,pady=5)
# userentry=Entry(f1,textvariable=passvalue,bg='light blue').grid(row=1,column=1,padx=5,pady=5)



#           checkbutton
# checkvalue=IntVar()

# check=Checkbutton(f1,text='are u muslim ',variable=checkvalue).grid(row=2,columnspan=3)


#       buttons

# def get():
#     check=checkvalue.get()

#     if check==1:
#         value= 'yes.... i\'m muslim'
#     else:
#         value='no... i\'m not muslim'
#     print (f'{uservalue.get()} , {passvalue.get()} , {value}')

# b1=Button(f1,text='Enter',command=get).grid(row=3,columnspan=2)



# -------------------------------------------------------------------this is ending  ----------------------------------------------------


#   ---------------- canvas starts now -------------------------



#               canvas      tutorial ----> 13

# canvas_width=800
# canvas_height=400

# win.geometry(f'{canvas_width}x{canvas_height}')



# can_widget=Canvas(win,width=canvas_width,height=canvas_height)
# can_widget.pack()


#           canvas line
# can_widget.create_line(0,0,800,400,fill='red')
# can_widget.create_line(0,400,800,0,fill='red')


#               create rectangle
# can_widget.create_rectangle(400,150,200,90,fill= 'black')



#           create text
# can_widget.create_text(400,200,text='this is text ')



#               create oval
# can_widget.create_oval(400,150,200,90,fill='red')


#               create polygon
# points=(250,110,480,200,280,350,250,110,200,330)
# can_widget.create_polygon(points,fill='red')




# ----------------------------------------------------------    canvas ends ---------------------------------------------------




#               events handling

# def nasib(event=None):
#     print(f'you clicked the button at {event.x},{event.y}')


# widget=Button(win,text='click me ')
# widget.pack()

# widget.bind('<Button-1>', nasib)
# widget.bind('<Double-1>', quit)





#                   exersice 2
# width='900'
# height='500'
# win.geometry(f'{width}x{height}')

# f1=ttk.LabelFrame(win)
# f1.place(x=400,y=150)


# #           labels
# l1=Label(f1,text='Width')
# l1.grid(padx=9,pady=9)

# l2=Label(f1,text='Height')
# l2.grid(row=1,column=0,padx=9,pady=9)



#         #   entry box

# w_var=StringVar()
# w_entry=Entry(f1,width=15,textvariable=w_var,bg='grey',fg='white')
# w_entry.grid(row=0,column=1,padx=9,pady=9)
# w_entry.focus()


# h_var=StringVar()
# h_entry=Entry(f1,width=15,textvariable=h_var,bg='grey',fg='white')
# h_entry.grid(row=1,column=1,padx=9,pady=9)


# # #               button
# def apply():
#     win.geometry(f'{w_var.get()}x{h_var.get()}')

# b1=Button(f1,text='Apply',command=apply)
# b1.grid(row=3,columnspan=4)


# ------------------------------   exersice 2 ends --------------------------------


#               menu var
# def myfunc():
#     print('Function called')



#           these are important for a non dropdownbox menu

# mymenu=Menu(win)
# mymenu.add_command(label='File',command=myfunc)
# mymenu.add_command(label='Exit',command=quit)
# win.config(menu=mymenu)



#                   for dropdown box

# mymenu=Menu(win)
# m1=Menu(mymenu,tearoff=0)
# m1.add_command(label='New File',command=myfunc)
# m1.add_separator()
# m1.add_command(label='Save',command=myfunc)
# m1.add_command(label='Save as',command=myfunc)

# win.config(menu=mymenu)

# mymenu.add_cascade(label='File',menu=m1)


#                   message box

# def help():
#     print('Insha allah ALLAH will help me ')
#     a=msg.showinfo('Help', 'Insha allah i will help you ')
#     # print(a)        #   return value


# m2=Menu(mymenu,tearoff=0)
# m2.add_command(label='help',command=help)
# win.config(menu=mymenu)
# mymenu.add_cascade(label='help',menu=m2)




#           sliders
# myslider=Scale(win,from_=0,to=500)
# myslider.pack()



# Label(win,text='How much dollar do u need ?',font=('lucida',20)).pack()

# myslider2=Scale(win,from_=1,to=100,orient=HORIZONTAL,tickinterval=20)
# myslider2.set(35)
# myslider2.pack()

# def get():
#     msg.showinfo('Ammount credited',f'We have credited {myslider2.get()} dollars in ur account')

# Button(win,text='Get dollars',command=get).pack(pady=15)




#                   radio button
# def order():
#     msg.showinfo('Order Confirmation',F'We have recieved ur order for {var.get()}........THANK YOU')

# var=StringVar()
# var.set('Samusa')
# Label(win,text='What would u like to have ? ',font=('lucida',23,'bold')).pack()

# name=['Samusa','Pharata','Tea']

# for i in name:
#     Radiobutton(win,text=i,variable=var,value=i,font=30).pack(anchor='w',padx=70)


# Button(win,text='Order Now',command=order).pack(anchor=CENTER,pady=10)





#               ListBox



# i=1
# lbx=Listbox(win)
# lbx.pack()
# lbx.insert(END,'This is first item')

# def add():
#     global i
#     lbx.insert(ACTIVE,i)
#     i+=1

# Button(win,text='Add items',command=add).pack(pady=10)



#                           Scroll Bar


# For connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2.scrollbar.config(command=widget.yview)

# scroll_bar=Scrollbar(win)
# scroll_bar.pack(side=RIGHT,fill=Y)



#               scroll bar with listbox

# lbox=Listbox(win,yscrollcommand=scroll_bar.set)
# for i in range(355):
#     lbox.insert(END,i)

# lbox.pack(fill=BOTH,padx=15)
# scroll_bar.config(command=lbox.yview)



#               scroll bar with text editor

#                       this is an easy way to create text editor       

# text=Text(win,yscrollcommand=scroll_bar.set)
# text.pack(fill=BOTH,padx=10,pady=9)
# scroll_bar.config(command=text.yview)




#               status bar
# statusvar=StringVar()
# statusvar.set('Status Bar')

# def update():
#     statusvar.set('Busy...')
#     sbar.update()
#     time.sleep(3)
#     statusvar.set('Ready Now')

# sbar=Label(win,textvariable=statusvar,relief=RAISED,font=('agency fb',15,'bold'),anchor='w',bg='light grey')
# sbar.pack(side=BOTTOM,fill=X)

# Button(win,text='Upload',command=update).pack()



# win.mainloop()




#                       classes and objects in tkinter

# class GUI(Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry('1000x400')

#     def status(self):
#         self.var=StringVar()
#         self.var.set('Ready')
#         self.status_bar=Label(self,textvar=self.var,relief=RAISED,bg='light grey')
#         self.status_bar.pack(side=BOTTOM,fill=X)



#     def click(self):
#         print('Button clicked')




#     def create_button(self,inputtext):
#         Button(text=inputtext,command=self.click).pack()



# if __name__ == "__main__":
#     win=GUI()
#     win.status()
#     win.create_button('Apply')



#     win.mainloop()


#               more aboute tkinter
w=win.winfo_screenwidth()
h=win.winfo_screenheight()

print(f'{w}x{h}')

win.mainloop()
