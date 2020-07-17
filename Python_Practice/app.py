





# # create_app.py  





import tkinter as tk
from tkinter import ttk
from csv import DictWriter
import os

win=tk.Tk()
win.title('GUI') 
#       create labels
name_label=ttk.Label(win,text='Enter ur name:')
name_label.grid(row=0, column=0,sticky=tk.W)  

age_label=ttk.Label(win,text='Enter ur age:')
age_label.grid(row=1, column=0,sticky=tk.W)  


email_label=ttk.Label(win,text='Enter ur email:')
email_label.grid(row=2, column=0,sticky=tk.W) 


gender_label=ttk.Label(win,text='select your gender:')
gender_label.grid(row=3, column=0,sticky=tk.W) 



#           create entry box
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=17,textvariable=name_var)
name_entrybox.grid(row=0,column=1)
name_entrybox.focus()

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=17,textvariable=age_var)
age_entrybox.grid(row=1,column=1)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=17,textvariable=email_var)
email_entrybox.grid(row=2,column=1)



#           combo box
gender_var=tk.StringVar()
gender_combobox=ttk.Combobox(win,width=14,textvariable=gender_var,state='readonly')
gender_combobox['values']=('Male','Female','Others')
gender_combobox.current(0)
gender_combobox.grid(row=3,column=1)



#       radio button
usertype=tk.StringVar()
radiobt1=ttk.Radiobutton(win,text='Student', value='Student', variable=usertype)
radiobt1.grid(row=4,column=0)

radiobt2=ttk.Radiobutton(win,text='Teacher', value='Teacher', variable=usertype)
radiobt2.grid(row=4,column=1)

radiobt3=ttk.Radiobutton(win,text='Other', value='Other', variable=usertype)
radiobt3.grid(row=4,column=2)




#       check button
check_var=tk.IntVar()
checkbtn=ttk.Checkbutton(win,text='check if you want to subscribe our youtube channel',variable=check_var )
checkbtn.grid(row=5,columnspan=3) #  columnspan is to use multiple column without disturbing others



#           create button and print the input and print
# def action():

#     print (f'{name_var.get()} is {age_var.get()} years old and his email is {email_var.get()}')

#     if check_var.get()==0:
#         subscribed='NO'
#     else:
#         subscribed='YES'

#     print(f'{gender_var.get()},{usertype.get()},{subscribed}')
    

#     with open ('app.txt', 'a') as af:
#         af.write(f'{name_var.get()},{age_var.get()},{email_var.get()},{gender_var.get()},{usertype.get()},{subscribed}')


# #           removing the data of entry box after entry
#     name_entrybox.delete(0,tk.END)
#     age_entrybox.delete(0,tk.END)
#     email_entrybox.delete(0,tk.END)
# #       changing the color

#     name_label.configure(foreground='#b3337f')



#           writing in the csv file
def action():
    user_name=name_var.get()
    user_email=email_var.get()
    user_age=age_var.get()
    user_type=usertype.get()

    if check_var.get()==0:
        subscribed='NO'
    else:
        subscribed='YES'

    with open ('app.csv','a',newline='') as cf:
        dict_writer=DictWriter(cf, fieldnames=['UserName','UserEmail','UserAge','UserType','Subscribed'])
        if os.stat('app.csv').st_size==0:
            dict_writer.writeheader()
        dict_writer.writerow({
            'UserName':user_name,
            'UserEmail':user_email,
            'UserAge':user_age,
            'UserType':user_type,
            'Subscribed':subscribed
        })
    
    name_entrybox.delete(0,tk.END)
    age_entrybox.delete(0,tk.END)
    email_entrybox.delete(0,tk.END)



    

submit_button=ttk.Button(win,text='submit', command=action)
submit_button.grid(row=6,column=0)

win.mainloop()  





  





# # create_app2.py  





#   import tkinter as tk
# from tkinter import ttk

# win=tk.Tk()
# win.title('Loop')


# #           loops and doing paddings
# labels=['what is ur name:','what is ur age:', 'what is ur email:']

# for i in range(len(labels)):
#     cur_label='label' + str(i)
#     cur_label=ttk.Label(win, text=labels[i])
#     cur_label.grid(row=i,column=0,sticky=tk.W, padx=10,pady=3) #padx= left and right , pady=top and bottom

# user_info={
#     'name':tk.StringVar(),
#     'age':tk.StringVar(),
#     'email':tk.StringVar()
# }
# counter=0
# for i in user_info:
#     cur_entry='enter' + i
#     cur_entry=ttk.Entry(win, width=17, textvariable= user_info[i])
#     cur_entry.grid(row=counter,column=1,padx=10,pady=3)
#     counter+=1


# def submit():
#     for i in user_info:
#         # print(user_info.get(i).get())
#         print(user_info[i].get())


# submit_btn=ttk.Button(win, text='Submit', command=submit)
# submit_btn.grid(row=4,columnspan=2)


# win.mainloop()  





  





# # create_app3.py  





#   import tkinter as tk
# from tkinter import ttk

# win=tk.Tk()
# win.title('Label frame')

# label_frame=ttk.LabelFrame(win, text='Enter ur details')
# label_frame.grid(row=0,column=0,padx=50)

# labels=['what is ur name:','what is ur age:', 'what is ur email:']

# for i in range(len(labels)):
#     cur_label=ttk.Label(label_frame, text=labels[i])
#     cur_label.grid(row=i,column=0,sticky=tk.W,padx=2,pady=2)


# user_info={
#     'name':tk.StringVar(),
#     'age':tk.StringVar(),
#     'email':tk.StringVar()
# }
# counter=0
# for i in user_info:
#     cur_entry=ttk.Entry(label_frame,width=17,textvariable=user_info[i])
#     cur_entry.grid(row=counter,column=1)
#     counter+=1


# def submit():
#     for i in user_info:
#         print(user_info[i].get())

# submit_btn=ttk.Button(label_frame, text='Submit', command= submit)
# submit_btn.grid(row=4,columnspan=2)


# win.mainloop()  





  





# # create_app4.py  





#   import tkinter as tk
# from tkinter import ttk

# win= tk.Tk()
# win.title('Tab control')

# nb=ttk.Notebook(win)
# p1=ttk.Frame(nb)
# p2=ttk.Frame(nb)
# nb.add(p1, text= 'ONE')
# nb.add(p2, text= 'TWO')
# # nb.grid(row=0,column=0)
# nb.pack(expand=True,fill='both')        #   its best for the labels

# label1=ttk.Label(p1,text='this is page 1')
# label1.grid(row=0,column=0)

# p1_var=tk.StringVar()
# entry1=ttk.Entry(p1,width=17,textvariable=p1_var)
# entry1.grid(row=0,column=1)

# label2=ttk.Label(p2,text='this is page 2')
# label2.grid(row=0,column=0)

# win.mainloop()  





  





# # create_app5.py  





#   import tkinter as tk
# from tkinter import ttk

# win= tk.Tk()
# win.title('Menu bar')


# def func():
#     print('function called ')

# # menubar=tk.Menu(win)
# #       -------------  simple menubar-----------
# # menubar.add_command(label='Save',command=save_func)
# # menubar.add_command(label='Paste',command=save_func)
# # menubar.add_command(label='Copy',command=save_func)


# #   -------------  menu under menu ///// nested menu-----------
# main_menu=tk.Menu(win)
# file_menu=tk.Menu(main_menu,tearoff=0)
# file_menu.add_command(label='New file', command=func)
# file_menu.add_command(label='New window', command=func)
# file_menu.add_separator()
# recent_menu=tk.Menu(file_menu,tearoff=0)
# recent_menu.add_command(label='Recent file',command=func)
# recent_menu.add_command(label='Recent window',command=func)
# file_menu.add_command(label='Copy', command=func)
# file_menu.add_command(label='Paste', command=func)

# edit_menu=tk.Menu(main_menu,tearoff=0)
# edit_menu.add_command(label='Undo',command=func)
# edit_menu.add_command(label='Redo',command=func)


# main_menu.add_cascade(label='File', menu=file_menu)
# main_menu.add_cascade(label='Edit',menu=edit_menu)
# file_menu.add_cascade(label='Recent',menu=recent_menu)


# win.config(menu=main_menu)

# win.mainloop()  





  





# # create_app6.py  





#   import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox as m_box

# win=tk.Tk()
# win.title('message box')

# label_frame=ttk.LabelFrame(win,text='User details')
# label_frame.grid(row=0,column=0,padx=50)

# label1=ttk.Label(label_frame,text='what is ur name:',font=('Helvetica',10,'bold'))
# label1.grid(row=0,column=0)

# label2=ttk.Label(label_frame,text='what is ur age:',font=('Helvetice',10,'bold'))
# label2.grid(row=0,column=2)

# name_var=tk.StringVar()
# entry1=ttk.Entry(label_frame,width=17,textvariable=name_var)
# entry1.grid(row=1,column=0,padx=50)

# age_var=tk.StringVar()
# entry2=ttk.Entry(label_frame,width=17,textvariable=age_var)
# entry2.grid(row=1,column=2,padx=50)


# def submit():
#     name=name_var.get()
#     age=age_var.get()
#     if name=='' or age=='':
#         m_box.showerror('Error','Please fill both boxes')
#     else:
#         try:
#             age=int(age)
#         except ValueError:
#             m_box.showerror('Error','Only digits are allowed in age field')
#         else:
#             if age<18:
#                 m_box.showwarning('Error','You are not 18')
#             else:
#                 print(f'{name} is {age} years old')

# submit_btn=ttk.Button(win,text='Submit',command=submit)
# submit_btn.grid(row=3,columnspan=2,padx=50)


# win.mainloop()  





  