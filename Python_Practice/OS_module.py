#           os module 1
import os
# print(os.getcwd())  ---> get current working dictionary
# print(os.path.exists('chapter19.py'))     ---> checking the existance of file or folder
# os.mkdir('first_project.py')----> making folder
# os.rmdir('first_project.py')---. removing folder but it removes empty folder

#   folder under folder
# os.makedirs('new/file')

#   best way to create a file or folder
# if os.path.exists('chapter1.py'):
#     print('already exits')
# else:
#     os.mkdir('chapter1.py')


#       best way to create file
# open('first_project.py','a').close()


#   making in another drive 

# os.mkdir(r'e:\new_file')


#       listdir---> it makes a list of exist file and folder
# print(os.listdir())


#       Collecting the path 
# for path in os.listdir():
#     print(os.path.join(os.getcwd(),path))




#       os module 2
#                   deep search

import os
# fileiter = os.walk(r'e:\\')
# for current_path,folder_name,file_name in fileiter:
#     print(f'current_path {current_path}')
#     print(f'folder_name {folder_name}')
#     print(f'file_name {file_name}')



#       deleting the folder where has something

import shutil
# shutil.rmtree('new')

# os.rmdir('chapter1.py') #   ---> this is to delete empty folder

#       copying from one to another
# shutil.copytree('New_file','chapter1.py/New_file')  #   for folder
# shutil.copy('file2.txt','New_file/file2.txt')       #   for file

#       move with rename
# shutil.move('new_file','chapter1.py/new2')