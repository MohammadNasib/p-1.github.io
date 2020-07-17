# #           chapter6

# #       tuple
# # tupleib','tansir')     #   touples are imutable means not changable
# # print(touple)                   
# #methods    count,index,len function,slicing


# #   looping with tuples


# #       tuple with one elements
# # name = ('nasib',)
# # print(type(name))


# #   tuple without parantheses
# # name = 'nasib','tansir'
# # print(type(name))


# #   tuple unpacking 
# # name = 'nasib','tansir'
# # name1,name2=name
# # print(name1)
# # print(name2)


# # list inside of tuple
# # name='nasib',['tansir','hasib']     we can do evertthing with list even inside of tuple
# # name[1][0]='nasib'
# # print(name)

# #       video 114 is important


# #       touple with range function 
# # nums = tuple(range(1,11))
# # print(nums)



# #       converting tuple to list
# # nums =list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# # print(nums)
    



#     #      converting tuple to string
# # nums =str((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# # print(type(nums))






# #                   chapter 7


# #       dictionary


# #       first method to creat dictionary
# # user1 ={'name':'nasib','age':17}
# # print(user1)


# #       dict method to creat dictionary
# # user2 =dict(name='nasib',age=17)
# # print(user2)


# #       accessing to dictionary
# # user2 =dict(name='nasib',age=17)        as dict has no index
# # print(user2['age'])


#      # making dict.in more than 1 line
# # user1 ={
# #     'name':'nasib',         # clean syntex
# #     'age': 17,
# #     'fav_songs' : ['allah_allah','tme_j_dener_chobi']
# # }
# # print(user1)



# #       adding data in dict
# # user2={}
# # user2['name'] = 'nasib'
# # user2['age'] = 17
# # print(user2)



#       #  in keyword
# # user = {
# #     'name' : 'nasib',
# #     'age': 17,
# #     'fav_names' : ['abdullah','abdur rahman'],
# #     'brothers' : ['hasib','tancir']
# # }
# # print(user)
# # if 'box' in user:
# #     print('true')
# # else:
# #     print('false')


# #       in keyword for vlues
# # user = {
# #     'name' : 'nasib',
# #     'age': 17,
# #     'fav_names' : ['abdullah','abdur rahman'],
# #     'brothers' : ['hasib','tancir']
# # }
# # if ['abdullah','abdur rahman'] in user.values():        #this is for checking values
# #     print('true')                                     
# # else:
# #     print('false')


# #           looping in the dictionary
# # user = {
# #     'name' : 'nasib',
# #     'age': 17,
# #     'fav_names' : ['abdullah','abdur rahman'],
# #     'brothers' : ['hasib','tancir']
# # }
# # for i in user:
# #       print(i)


# #     looping for values
# # user = {
# #     'name' : 'nasib',
# #     'age': 17,
# #     'fav_names' : ['abdullah','abdur rahman'],
# #     'brothers' : ['hasib','tancir']
# # }
#             # for i in user.values():     or
# # for i in user:
# #       print(user[i])



# #           dict values
# # user = {
# #     'name' : 'nasib',
# #     'age': 17,
# #     'fav_names' : ['abdullah','abdur rahman'],
# #     'brothers' : ['hasib','tancir']
# # }
# # values=user.values()
# # print(values)


# #           dict keys 
# # user = {
# #     'name' : 'nasib',
# #     'age': 17,
# #     'fav_names' : ['abdullah','abdur rahman'],
# #     'brothers' : ['hasib','tancir']
# # }
# # keys = user.keys()
# # print(keys)


# #           items method
# # user = {
# #     'name' : 'nasib',
# #     'age': 17,
# #     'fav_names' : ['abdullah','abdur rahman'],
# #     'brothers' : [ 'hasib','tancir']
# # }
# # dict_items = user.items()
# # print(dict_items)
# # for key,value in user.items():
# #       print(f'  key is {key} and value is {value}')


# #           how to add data in dict
# # user['fav']=['song1','song2']
# # print(user)

# #           how to pop data
# # popped = user.pop('fav_names')
# # print(popped)
# # print(user)


# #           pop by randomly
# # popped = user.popitem()
# # print(user)
# # print(type(popped))



# #           update dictionary
# # more_info = {'name':'naeemul abrar nasib','city': "cox'sbazar" , 'country': 'bangladesh'} # if i input a same key then i won't be take as another one rather it'll update old one
# # user.update(more_info)
# # print(user)


# #           from keys
# # a = dict.fromkeys(['name','age'],'unknown')
# # a = dict.fromkeys(('name','age'),'unknown')
# # print(a)


# #       get method
# a = {'name': 'nasib','age':17}
# print(a['name'])
# print(a.get('name'))  #its better
# if 'name' in a:
#     print('true')
# else:
#     print('false')

# # if a.get('name'):     its better
# #     print('present')
# # else:
# #     print('not present')

# #   clear method 
# # a.clear()
# # print(a)


# #       copy method
# # a1 = a.copy()
# # print(a1)


# #            more about get
# #       how to return anyhting except none
# # a = {'name': 'nasib','age':17}
# # print(a.get('names','not found!'))




# #           exersice 1......cube finder
# # def cube_finder (n):
# #     cubes = {}
# #     for i in range(1,n+1):
# #         cubes[i] = i**3
# #     return cubes
# # print(cube_finder(int(input ('enter a number:'))))


# #       word count in dictionary
# # def word_counter(s):
# #     character = {}
# #     for char in s:
# #         character[char] = s.count(char)
# #     return character
# # print(word_counter(input('enter a word:')))



# #       exersice 2...........taking input and printing 
# # user= {}
# # user['name'] = input('enter ur name:')
# # user['age'] =int(input('enter ur age:'))
# # for key,value in user.items():
# #     print(f'{key}:{value}')  





# #                        chapter8.py 
 
#  #       set = unordered  collection of unique items 
#  # set is also created as dictitonary but there has no key and value pair
# # s = {1,2,3,2} 
# # print(s)


# #       converting a list to set
# # l = [1,2,3,3,3,5,5,5,6]     #   remove duplicate
# # l2 =list(set(l))    #   converted a list to set then again converted in list only to remove duplicate
# # print(l2)


#             # adding data in sets
# # s = {1,2,3,2}
# # s.add(4)
# # print(s)


# #       remove from sets
# # s.remove(8)
# # print(s)



# #       discard method 
# # s.discard(11)
# # print(s)


# #       clear method 
# # s.clear()
# # print(s)


# #       copy method
# # e=s.copy()
# # print(e)


# #       what can i store in sets........>i can't store list and dictionary in set
# # s = {1,1.1,'nasib'}
# # print(s)



# #           in keyword
# # s ={'a','v','b','d'}
# # if 'g' in s:
# #     print('true')
# # else:
# #     print('false')


# #       for loop
# # for i in s:
# #     print(i)



# #       set maths ......> we can do only 'union' and 'intersection'
# #       union.......it combines the sets
# s ={1,3,2,5,7}
# f={2,5,7,4}
# g ={3,5,2,6,7,8}
# # union = s|f|g
# # print(union)


# #       intersection 
# # inter= s & f & g
# # print(inter)  
  





# #    chapter9.py  


#   #               list comprehension  (lc)

# #       create a list of square of 1 to 10
# # squares = []
# # for i in range (1,11):
# #     squares.append(i**2)
# # print(squares)


# # squares2 = [i**2 for i in range(1,11)]  #   this is list comprehension 
# # print(squares2)


# #   squares of negative num. -1 to -10 by lc 
# # negative_squares =[-i**2 for i in range (1,11)]
# # print(negative_squares)


# #   practice
# # list = ['nasib','hasib','tansir']
# # list2 =[i[0] for i in list]
# # for i in list:
# #     list2.append(i[0])
# # print(list2)



# #       exersice 1 .....>reverse of strings
# # def reverse_string (l):
# #     return[i[::-1] for i in l]
#     # list = []
#     # for i in l:
#     #     list.append(i[::-1])
#     # return (list)


# # name = ['nasib','tansir','hasib',]
# # u = reverse_string(name)
# # print(u)




# #       list comprehension with if statement
# # even = [i for i in range(1,11) if i%2==0]
# # odd = [i for i in range(1,11) if i%2 != 0]
# # print(even)
# # print(odd)



# #       esxersice 2 ......changing of type
# # def num_to_string (l):
# #     return[str(i) for i in l if type(i) == int or type(i)== float]
# # print(num_to_string(['nasib','tansir',1,1.0,2.3]))



# #       lc with if else
# # nums=[i*2 if i%2==0 else -i for i in range(1,11)]
# # print(nums)



# #       nested lc........nested means list under list
# # l=[]
# # for i in range(3):
# #     l.append([1,2,3])
# # print(l)

# # new_list =[[i for i in range(1,4)] for j in range(3)]
# # print(new_list)  







# #          chapter10.py  
#   #           Dictionary comprehension (dc)
# # square = {f'square of {num} is':num**2 for num in range(1,11)}

# # for k,v in square.items():
# #     print(f'{k}:{v}')


# #        word counting
# # name = 'nasib'
# # counter = {char:name.count(char) for char in name}
# # print(counter)



# #           odd or even number 
# # odd_even = {num:'even' if num%2==0 else 'odd' for num in range(1,11) }
# # for k,v in odd_even.items():
# #     print(f'{k}:{v}')



# #                set comprehension (sc).......> its rare
# # square = {i**2 for i in range(1,11) }
# # print(square)  




# # chapter11.py  
#   #       make flexible function 


# #       *operator or *args ..> args gather as a touple


# #               by *args we can remove the limitation of input..we can input as much as we can by this *args




# # def all_total(*args):
# #     total = 0
# #     for i in args:
# #         total+=i
# #     return total
# # print(all_total(1,2,3,4))


# #           args with normal parameter...video---->145



# #           unpacking the elements in args
# # def multiply(*args):
# #     total = 1
# #     # print(args)
# #     for i in args:
# #         total *= i
# #     return total
# # num = [2,3,4]
# # print(multiply(*num))       # to unpack the elements of a list or touple in args give a star before list or touple's name




# #       exersice 1------> 
# # def making_power (num,*args):
# #     list=[]
# #     for i in args:
# #         list.append(i**num)
# #     return list
# # num=[1,2,3]
# # num2=3
# # print(making_power(num2,*num))

#     #  solution by lc
# # def making_power2(num,*args):
# #     if args:
# #         return [i**num for i in args]
# #     else:
# #         return "u didn't pass any args"
# # num=[1,2,3]
# # print(making_power(3,*num))





# #       kwargs ------> **kwargs



# #   kwargs as a parameter---->kwargs gahter as a dictionary
# # def gather(**kwargs):
# #     for k,v in kwargs.items():
# #         print(f'{k}:{v}')
# # gather(first_name = 'naeemul',last_name = 'abrar')


# #       dc unpacking
# # d ={'name' : 'nasib', 'age':17}
# # gather(**d)



# #   to use parameter,*args,default parameter and **kwargs joinly
# #   we have to maintain the serial which is parameter,*args,default parameter and **kwargs


# #       exersice..2......151
# #                       we use get() method to get the value of a dictionary  




     
# #               chapter12.py  



#   #       lambda expression (anonymous function)

# # add=lambda a,b:a+b
# # print(add(576947544,8579758545))


# #       lambda practice
# # is_even= lambda a:a%2==0
# # print(is_even(6))

# # last_char=lambda s: s[-1]
# # print(last_char('nasib'))


# bigger= lambda s :True if len (s) >= 5 else False
# print(bigger('nasib'))  
     





# #               chapter13.py  





#   #   enumerate fuction
# #           without enumerate function
# names= ['nasib','tansir','hasib']
# # pos=0
# # for i in names:
# #     print(f'{pos}----->{i}')
# #     pos+=1

# #       with enumerate fuction
# # for pos,name in enumerate(names):
# #     print(f'{pos}----->{name}')



# #       exersice
# # def find_pos(l,target):
# #     for pos,name in enumerate(l):
# #         if name==target:
# #             return pos
# #     return -1
# # print(find_pos(names,'tansir'))



#   map fucntion
# # num= [1,2,3,4,5]
# #       map with lambda
# # print(list(map(lambda a:a**2,num)))  

# #  map with def func.
# # def square (a):
# #     return a**2
# # print(list(map(square,num)))  with def function

# #   map with lc
# # print([a**2 for a in num]) -->  lc


# #       filter funtion
# # numbers= [1,2,3,4,5,6,7,8,9,10]
# # print(list(filter(lambda a:a%2==0,numbers)))
# # #   filter with lc
# # print([a for a in numbers if a%2==0])

# #   iterator vs iterable

# # iterable=string and tuple 

# #       process of working a for loop
# # call iter function
# # iter(numbers).....> iterator 
# # next(iter(numbers))

# #   working proccess of for loop in practicle
# # numbers=[1,2,3]
# # number_iter=iter(numbers)
# # print(next(number_iter))
# # print(next(number_iter))
# # print(next(number_iter))
# # print(iter(numbers))



# #       zip function 
# # user_id = ['user1','user2']
# # names=['nasib','tancir']
# # title=['elder brother','younger brother']
# # print(list(zip(user_id,names,title))) # we can change it to list and tuple also..if we give 3 argument we can't change it to dict



# #       reversing the zip function

# #       *operator with zip
# # l=[(1,2),(3,4),(5,6)]
# # l1,l2=(list(zip(*l)))
# # print(l1)
# # print(l2)

# #       uses of zip
# # l1=[1,3,5]
# # l2=[2,4,6]
# # l3=[]
# # for pair in zip(l1,l2):
# #     l3.append(max(pair))
# # print(l3)


# #       challenge
# # def avr_finder(*args):
# #     average=[]
# #     for pair in zip(*args):
# #         average.append(sum(pair)/len(pair))
# #     return average
# # l=[1,2,3],[4,5,6],[7,8,9]
# # print(avr_finder(*l))



# #   with lambda
# # average_finder=(lambda *args:[sum(pair)/len(pair) for pair in zip(*args)])
# # print(average_finder([1,2,3,],[4,5,6],[7,8,9]))



# #       all function 
# # num1=[2,4,6]
# # num2=[1,9,5]
# # print(all(num%2==0 for num in num1))

# #       any function
# # print(any(num%2==0 for num in num2))


# #       any and all practice
# # def my_sum(*args):
# #     if all([(type(arg)== int or type(arg)==float) for arg in args]):
# #         total=0
# #         for i in args:
# #             total+=i
# #         return total
# #     else:
# #         return'wrong input'
# # num=(1,2,3,4,['nasib'],'tansir')
# # print(my_sum(*num))



# #          adv. min and max function


# #       finding the biggest lenght
# # names=['tansir','nasib','ab','naeemul abrar','n']
# # print(min(names,key=lambda i:len(i)))


# #       practice 2
# # player=[
# #     {'name':'nasib','roll':1,'score':90},
# #     {'name':'tansir','roll':18,'score':70},
# #     {'name':'hasib','roll':5,'score':80},
# # ]
# # print(min(player,key=lambda i: i.get('score'))['name'])


# #       practice 3
# # studens={
# #     'nasib':{'score':65,'age':17},
# #     'tancir':{'score':80,'age':12}
# # }
# # print(max(studens,key=lambda item:studens[item]['score']))



# #       sort and sorted method  #   basic
# # list1=['grapes','mango','apple']
# # print(sorted(list1))
# # tuple1=('grapes','orange','apple')
# # print(sorted(tuple1))


# #       advance sorted
# # bike=[
# #     {'name': 'yamaha','price':5000},
# #     {'name':'avenger','price':10000}
# # ]
# # print(sorted(bike,key=lambda d:d['price'],reverse=True))


# #       doc strings---->it gives us a message to understand the proccess..
# # def add(a,b):
# #     '''this func.takes 2 input and return the sum of them'''
# #     return a+b
# # print(add(1,2))
# # print(add.__doc__)


# # print(help(sum))          we can use help func.also  





  





# # chapter14.py  





#   #       decorators


# #       concept before knowing decorators

# #   first class function / closures

# # l=[5,6]
# # print(list(map(lambda a:a**2,l)))

# #    creating my map func.
# # def my_map(func,l):
# #     return [func(i) for i in l]
# # l=[1,2,3]
# # print(my_map(lambda a: a**2,l))



# #           func.returning the func. is called first class func. or clouser
# # def outer_fun():
# #     def inner_func():
# #         print('inside inner func')
# #     return inner_func()

# # var=outer_fun()
# # var()


# # def outer_func2(msg):
# #     def inner_func2():
# #         print(f'message is {msg}')
# #     return inner_func2

# # var=outer_func2('Hi')
# # var()


# #       practice of clouser
# # def to_power(n,x):
# #     return n**x
# # print(to_power(2,3))

# # def power(p):
# #     def number(n):
# #         return n**p
# #     return number

# # cube=power(3)
# # print(cube(2))

# # square=power(2)
# # print(square(8))


# #               decorators...enhance the functionality of other function
# # def decorators_fun(any_fun):
# #     def inner_fun():
# #         print('this is decorators')
# #         return any_fun()              # to write return is better in this line
# #     return inner_fun

# # @decorators_fun     #   this is short cut
# # def fun1():
# #     print('this is fun.1 ')

# # fun1()

# # @decorators_fun 
# # def fun2():
# #    print('this is fun.2 ')

# # fun2()

# # fun1=decorators_fun(fun1)     # this is long proccess
# # fun1()  


# #       2 problems in previous decorators

# #           1st pr. is for *args and 2nd is for return 
# # def decorators_fun(any_fun):
# #     def inner_fun(*args):
# #         print('this is decorators')
# #         return any_fun(*args)
# #     return inner_fun

# # @decorators_fun
# # def add(a,b):
# #     return(a+b)
# # print(add(2,3))


# #       calculation of time in python 

# #       ex...1
# # from functools import wraps
# # import time
# # def calc_time(func):
# #     @wraps(func)
# #     def fun(*args):
# #         print(f'u r executing {func.__name__} function')
# #         t1=time.time()
# #         re_v=func(*args)
# #         t2=time.time()
# #         total=t2-t1
# #         print (f'this takes {total} seconds')
# #         return re_v
# #     return fun

# # @calc_time
# # def square(n):
# #     return [i**2 for i in range(1,n)]

# # square(10000)


# #       decorators practice
# # from functools import wraps
# # def only_int(function):
# #     @wraps(function)
# #     def inner_fun(*args):
# #         if all([type(arg)==int for arg in args]):
# #              return function(*args)
# #         else:
# #             return 'invalid input'


#         # for arg in args:
#         #     data_type.append(type(arg)==int)
#         # if all(data_type):
#         #     return function(*args)
#         # else:
#         #     return'invalid input'


#     # return inner_fun

# # @only_int
# # def fun(*args):
# #     total=0
# #     for i in args:
# #         total+=i
# #     return total

# # print(fun(1,2,3,4,[1],5))



# # #           decorators with argument.....

# # from functools import wraps
# # def only_data_type_allow(data_type):
# #     def decorators(function):
# #         @wraps(function)
# #         def inner_func(*args):
# #             if all([type(arg)==data_type for arg in args]):
# #                 return function(*args)
# #             else:
# #                 return 'invalid input'
# #         return inner_func
# #     return decorators

# # @only_data_type_allow(str)
# # def str_join(*args):
# #     string=''
# #     for i in args:
# #         string+=i
# #     return string
# # print(str_join('naeemul' 'abrar' 'nasib'))  





  





# # chapter15.py  





#   #       generators.....-----> iterators
# #       generators generate one number at a time

# # def nums(n):
# #     for i in range(1,n+1):
# #         yield i
# # num=nums(10)
# # for i in num:
# #     print(i)

# # num=list(nums(10))
# # print(num)


# #       ex..1 
# # def even(a):
# #     for i in range(1,a+1):
# #         if i%2==0:
# #             yield i
# # def even(a):
# #     for i in range(2,a+1,2):
# #         yield i
# # a=even(10)
# # for i in a:
# #     print(i)



# #       generator comprehinsion...gc
# # square=(i**2 for i in range(1,11))
# # for i in square:
# #     print(i)  





  





# # chapter16.py  





#   #       object oriented programming // oop

# # class Person:
# #     def __init__(self,first_name,last_name,age):
# #         self.first_name=first_name
# #         self.last_name=last_name
# #         self.age=age

# # p1=Person('naeemul abrar','nasib',17)
# # p2=Person('tansir oj','jaman',12)

# # print(p1.first_name)
# # print(p2.last_name)
# # print(p1.age)

# #       

# #       ex.1
# # class Laptop:         # attributes
# #     def __init__(self,name,model,price):
#             #   instance variable
# #         self.price=price
# #         self.model=model
# #         self.name=name
# #         self.laptop_name=name+ ' ' + model        # we can use more 'instance variables' than our 'attributes' 
# # .                                                   #   but its value should be in attributes
# # l1=Laptop('lenovo','ideapad 330',25500)
# # l2=Laptop('samsung','j15',35500)
# # print(l1.name)
# # print(l2.model)
# # print(l1.laptop_name)
# # print(l2.laptop_name)


# #       object / instance method
# # class Person:
# #     def __init__(self,first_name,last_name,age):
# #         self.first_name=first_name
# #         self.last_name=last_name
# #         self.age=age
# #     def full_name(self):
# #         return f'{self.first_name} {self.last_name}'

# # p1=Person('naeemul abrar','nasib',17)
# # p2=Person('tansir oj','jaman',12)
# # print(p1.full_name())
# # print(p2.full_name())


# #       ex.2 
# # class Laptop:         # attributes
# #     def __init__(self,name,model,price):
# #         self.price=price
# #         self.model=model
# #         self.name=name

# #     def discount(self,a):
# #         return self.price - (a/100*self.price)
# # l1=Laptop('lenovo','ideapad 330', 63000)
# # l2=Laptop('samsung','j15',35500)
# # print(l2.discount(10))


# #           class variable // class attributes
# # class Circle:
# #     pie=3.1416  #----> its a class variabel
# #     def __init__(self,radius):
# #         self.radius=radius
# #     def calc_circumference(self):
# #         return 2* Circle.pie*self.radius

# # c=Circle(4)
# # c1=Circle(5)
# # print(c.calc_circumference())
# # print(c1.calc_circumference())


# #       class variables part 2
# # class Laptop:         # attributes
# #     discount_per=10
# #     def __init__(self,name,model,price):
# #         self.price=price
# #         self.model=model
# #         self.name=name

# #     def discount(self):
# #         return self.price - (Laptop.discount_per/100*self.price)

# # l1=Laptop('lenovo','ideapad 330', 63000)
# # l2=Laptop('samsung','j15',35500)
# # print(l2.discount())



# #       ex.3
# # class Person:
# #     count_instance=0
# #     def __init__(self,first_name,last_name,age):
# #         Person.count_instance+=1
# #         self.first_name=first_name
# #         self.last_name=last_name
# #         self.age=age

# # p1=Person('naeemul','abrar',17)
# # p2=Person('tancir oj','jaman',12)
# # print(Person.count_instance)


# #           class method 
# # class Person:
# #     count_instance=0
# #     def __init__(self,first_name,last_name,age):
# #         Person.count_instance+=1
# #         self.first_name=first_name
# #         self.last_name=last_name
# #         self.age=age

# #     @classmethod
# #     def count_instances(cls):
# #         return f'you have created {cls.count_instance} instance for {cls.__name__} class'

# # p1=Person('naeemul', 'abrar', 17)
# # p2=Person('tancir oj','jaman',12)
# # p3=Person('tancir oj','jaman',12)
# # print(Person.count_instances())


# #       class method as a constractor
# # class Person:
# #     count_instance=0
# #     def __init__(self,first_name,last_name,age):
# #         Person.count_instance+=1
# #         self.first_name=first_name
# #         self.last_name=last_name
# #         self.age=age

# #     @classmethod
# #     def count_instances(cls):
# #         return f'you have created {cls.count_instance} instance for {cls.__name__} class'

# #     @classmethod
# #     def for_string(cls,string):
# #         first,last,age=string.split(',')
# #         return cls(first,last,age)
    
# #     def full_name(self):
# #         return f'{self.first_name} {self.last_name}'

# # p1=Person('naeemul', 'abrar', 17)
# # p2=Person('tancir oj','jaman',12)
# # p3=Person.for_string('tancir oj,jaman,12')
# # print(Person.count_instances())
# # print(p3.full_name())


# #           static method
# # class Person:
# #     count_instance=0
# #     def __init__(self,first_name,last_name,age):
# #         Person.count_instance+=1
# #         self.first_name=first_name
# #         self.last_name=last_name
# #         self.age=age

# #     @staticmethod
# #     def hello():
# #         return 'this is a static method'

# # print(Person.hello())


# #       property
# # class Phone:         # attributes
# #     discount_per=10
# #     def __init__(self,name,model,price):
#         # if price > 0:
#         #     self.price=price
#         # else:
#         #     self.price=0
#         # self.price= max(price,0)
#         # self.model=model
#         # self.name=name
#         # self.complete_specification= f'{self.name} {self.model} and price is {self.price}'


# #     @property
# #     def complete_specification(self):
# #             return f'{self.name} {self.model} and price is {self.price}'


# # p1=Phone('Nokia',1100,1000)
# # p1.price=500
# # print(p1.price)


# #       inheritance
# # class Phone: # base / parent  class  
# #     def __init__(self,name,model,price):
# #         self.price=max(price,0)
# #         self.model=model
# #         self.name=name

# #     def full_name(self):
# #         return f'{self.name} {self.model}'

# #     def call(self,num):
# #         return f'calling {num}.....'


# # class Smartphone(Phone): # derives / child class       
# #     def __init__(self,name,model,price,ram,internal_memory):
# #         # two ways
# #         # Phone.__init__(self,name,model,price) # 1st uncommon way
# #         super().__init__(name,model,price)      # 2nd way common way
# #         self.ram=ram
# #         self.internal_memory=internal_memory


# # p1=Phone('Nokia',1100,1000)
# # s1=Smartphone('Samsung','J2',10000,'2gb','8gb')
# # print(p1.full_name())
# # print(s1.full_name())



# #        multilevel inheritance  and   method resolution order //MRO  and method overwriting and isinstance( )
# # class Phone: # base / parent  class  
# #     def __init__(self,name,model,price):
# #         self.price=max(price,0)
# #         self.model=model
# #         self.name=name

# #     def full_name(self):
# #         return f'{self.name} {self.model}'

# #     def call(self,num):
# #         return f'calling {num}.....'


# # class Smartphone(Phone): # derives / child class       
# #     def __init__(self,name,model,price,ram,internal_memory):
# #         # two ways
# #         # Phone.__init__(self,name,model,price) # 1st uncommon way
# #         super().__init__(name,model,price)      # 2nd way common way
# #         self.ram=ram
# #         self.internal_memory=internal_memory

# #     def full_name(self):
# #         return f'{self.name} {self.model} and price in {self.price}'    #   method overwriting



# # class Flightship(Smartphone): # derives / child class       
# #     def __init__(self,name,model,price,ram,internal_memory,front_cam):
# #         # two ways
# #         # Phone.__init__(self,name,model,price) # 1st uncommon way
# #         super().__init__(name,model,price,ram,internal_memory)      # 2nd way common way
# #         self.front_cam=front_cam


# # p1=Phone('Nokia',1100,1000)
# # s1=Smartphone('Samsung','J2',10000,'2gb','8gb')
# # s2=Flightship('Samsung','S10',10000,'2gb','8gb','9mp')
# # # print(p1.full_name())
# # # print(s1.full_name())
# # # print(s2.full_name())
# # # print(help(Smartphone))  # this is MRO //method resolution order

# # # print(isinstance(s2,Phone))     # isinstance()
# # print(issubclass(Smartphone,Phone)) # issubstance()



# #      multiple inheritance
# # class A:
# #     def call(self):
# #         return 'i\'m from class A'

# # class B:
# #     def call(self):
# #         return 'i\'m from class B'

# # class C(B,A):
# #     pass  # it's for only pass
# # o1=A()
# # o2=B()
# # o3=C()
# # print(o3.call())
# # print(help(C))
# # print(C.mro())
# # print(C.__mro__)


# #       dunder method / magic / spacial and operator overloading  and polymorphism
# class My_phone:
#         def __init__(self,name,model,price):
#                 self.name=name
#                 self.model=model
#                 self.price=price

#         def full_name (self):
#                 return f'{self.name} {self.model}'
# #               str,,,repr

#         # def __str__ (self):
#         #         return f'{self.name} {self.model}'  # for normal users

#         def __repr__ (self):
#                 return f'My_phone(\'{self.name}\',\'{self.model}\', and price is {self.price})' # for developers

#         # def __len__(self):
#         #         return len(self.full_name())  # len function

#         def __add__ (self,others):
#                 return self.price + others.price        # operator overloading

# p1=My_phone('Nokia',1100,1000)
# p2=My_phone('Nokia',1600,1200)
# print((p1+p2))  





  





# # chapter17.py  





#           #   RAISE errors
# # def add(a,b):
# #     if type(a)==int and type(b)==int:
# #         return a+b
# #     else:
# #         raise TypeError('You have entered wrong data type')

# # print(add('2','3'))


# #       example 1-----> not implemented errors
# # class Animal:
# #     def __init__(self,name):
# #         self.name=name
    
# #     def sound(self):
# #         raise NotImplementedError('You have to define this method ')

# # class Dog(Animal):
# #     def __init__ (self,name,breed):
# #         super().__init__(name)
# #         self.breed=breed

# #     def sound(self):
# #         return 'bhow bhow'

# # class Cat(Animal):
# #     def __init__ (self,name,breed):
# #         super().__init__(name)
# #         self.breed=breed

# #     def sound(self):
# #         return 'mew mew'

# # a1=Cat('jacky','mikky')
# # print(a1.sound())



# #           example 2
# # class Mobile:
# #     def __init__ (self,name):
# #         self.name=name

# # class Mobile_store:
# #     def __init__ (self):
# #         self.phone=[]

# #     def add_mobile(self,new_phone): 
# #         if isinstance(new_phone,Mobile):
# #             self.phone.append(new_phone)
# #         else:
# #             raise TypeError(f'{new_phone} is not an elements of Mobile')

# # m=Mobile('oneplus 6')
# # store=Mobile_store()
# # samsung='samsung galaxy s9'
# # store.add_mobile(m)
# # print(store.phone[0].name)



# #       exception handling 
# # while True:
# #         try:
# #                 age = int(input('enter ur age:'))
# #                 break
# #         except ValueError:
# #                 print('invalid input')

# # if age>=18:
# #         print('u can play this game' )
# # else:
# #         print('u can\'t play this game')


# #               else and finally keyword
# # while True:
# #         try:
# #                 num = int(input('enter a number:'))

# #         except ValueError:
# #                 print('enter an integer')
# #         except:
# #                 print('invalid input')
# #         else:
# #                 print(f'user input={num}')
# #                 break
# #         finally:
# #                 print('final block')



# #     ex.1                 
# # def devide(a,b):
# #         try:
# #                 return a/b
# #         except ZeroDivisionError:
# #                 print('please don\'t devide by zero ')
# #         except:
# #                 print('enter numbers only')
        
# # print(devide(10,5))



# # #               custom error
# # class NameTooShortError(ValueError):
# #         pass

# # def name_fun(a):
# #         if len(a) < 8:
# #                 raise NameTooShortError('entered name is too short')
# #         else:
# #                 return f'hi {a}'

# # name=input('enter ur name:')
# # print(name_fun(name))




# #                       debugging
# # import pdb 
# #                         # l= line... n = run... q= quit..... c= continue
# # pdb.set_trace()  # we can write this line anywhere we wish  



# # name=input('type ur name:')
# # age=input('type ur age:')
# # print(f'hi {name} ur age is {age}')
# # age2=int(age)+5
# # print (f'u will be {age2} in next five years')  





  





# # chapter18.py  





#   #               read text file

# #   methods ----> open, close, tell, read, seek, readline,

# f=open('file1.txt')
# # print(f'cursor position is {f.tell()}')
# # print(f.read())
# # print(f'cursor position is {f.tell()}')
# # f.seek(9)  #------------------------------> by this u can change the positon of cursor
# # print(f'cursor position is {f.tell()}')
# # f.close()

# # print(f.readline(),end='')
# # print(f.readline(),end='')

# # print(f.readlines())

# # print(f.name)

# # print(f.closed)




# #       with block // context manager

# # with open('file1.txt') as f:
# #     print(f.read())




# #           write files------> 'w'--> write, 'a'---> append , 'x' ------> create file if it  doesn't exist  , 'r+'----> write and read
# #           't' ---> text mode,'b'---> binary mode, '+'----> read + write            

# # with open ('file1.txt', 'r+') as f:
# #     f.seek(len(f.read()))
# #     f.write('this is append \n ')



# #           read and write in one time
# # with open('file1.txt', 'r') as rf:
# #     with open('file2.txt', 'w') as wf:
# #         wf.write(rf.read())



# #           ex.1
# # with open('file2.txt', 'r') as rf:
# #     with open ('file1.txt','a') as af:
# #         for line in rf.readlines():
# #             name,salary=line.split(',')
# #             af.write(f'{name}\'s salary is {salary}')




# #                   
# # with open ('file1.txt','r') as f:
# #     data=f.read()
# #     print(data)

  





  





# # chapter19.py  





#   #           csv file----> coma separated values

# # from csv import reader
 
 
# # with open ('file1.csv', 'r') as f:
# #     csv_reader= reader(f)
# #     next(csv_reader)
# #     for row in csv_reader:
# #         print(row)



# #           read csv file with dictReader

# # from csv import DictReader

# # with open('file1.csv','r') as f:
# #     csv_reader=DictReader(f)
# #     for row in csv_reader:
# #         print(row)




# #               write in csv file
# # from csv import writer

# # with open ('file1.csv', 'a',newline='') as f: # newline command is to avoid gap
# #     csv_writer=writer(f)

#             # methods= writerow,writerows

#     # csv_writer.writerow(['name','class'])
#     # csv_writer.writerow(['nasib','11'])
#     # csv_writer.writerow(['nasib','11'])

#     # csv_writer.writerows([['name','class'],['nasib','11'],['tansir','5']])




#     #                   dictwriter 
# # from csv import DictWriter
# # with open ('file1.csv','w',newline='') as f:
# #         csv_writer=DictWriter(f,fieldnames=['first_name', 'last_name'])
# #         csv_writer.writeheader()
# #         # methods=writerow,writerows
# #         csv_writer.writerow({
# #                 'first_name':'mohmmad',
# #                 'last_name':'nasib'
# #         })

# #         csv_writer.writerows([
# #                 {'first_name':'mohammad','last_name':'nasib'},
# #                 {'first_name':'mohammad','last_name':'tansir'}
# #         ])  




# #           from harry's advance tutorial
# def imprtnt():
#   print('This is the best way to use a function in another file')

# def main():
#   print('This is the best way to write "if __name__== __main__ funtion ') 

# print(__name__)

# if __name__ == "__main__": #  this is used to avoid the extra datas from another file
    # main() 

  