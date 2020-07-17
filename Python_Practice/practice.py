 #   ex.1
# name=input('enter ur name:')
# age=int(input('enter ur age:'))
# year=(2020-age)+100
# print(f'your name is {name} and ur age will be 100 in {year} ')


#       ex.2 odd and even
# input=int(input('enter a number:'))
# if input%2==0:
#     print('This is an even number')
# else:
#     print('This is an odd number')
#   ex.3 
# l=list(range(1,56))
# l2=[i for i in l if i<5 or i==5]
# print(l2)


#   ex.4...divisor
# input=int(input('enter a num to divide:'))
# l=[a for a in range(2,input+1) if input%a==0 ]
# print(l)


#       ex.5
# import random
# l1=range(1,random.randint(1,30))
# l2=range(1,random.randint(1,50))
# l3=[i for i in l1 if i in l2]
# print(l3)


#       ex.6   palindrom
# user=input('enter a word :')
# palindrom=user[::-1]
# if user ==palindrom:
#     print('This is a palindrom')
# else:
#     print('This is not a palindrom')


# 3   ex.7   even list
# l=range(1,50)
# even=[a for a in l if a%2==0]
# print(even)


#       ex.8  rock,paper,scissor
# a=['rock','paper','scissor']
# i=input('enter rock,paper or scissor: ')
# import random
# pc=random.choice(a)
# if pc=='rock' and i=='paper':
#     print('Player wins')
# elif pc=='rock' and i== 'scissor':
#     print('Pc wins')
# elif pc=='paper' and i == 'scissor':
#     print('Player wins')
# elif pc=='paper' and i == 'rock':
#     print('Pc wins')
# elif pc=='scissor' and i == 'paper':
#     print('Pc wins')
# elif pc=='scissor' and i == 'rock':
#     print('plyer wins')
# elif pc==i:
#     print('Its a tie')
# else:
#     print('Invalid input')



#           ex.9  gussing game
# i=int(input('enter a numer between 1 and 9:'))
# import random
# a=random.randint(1,9)
# l=1
# game_over=False
# while not game_over:
#     if i==a:
#         print(f'You win in {l} attemp')
#         game_over=True
#     else:
#         if i>a:
#             print('its too high')
#             l+=1
#             i=int(input('enter again:'))
#         else:
#             print('its too short')
#             l+=1
#             i=int(input('enter again:'))


#       ex 10
# import random
# l1=range(1,random.randint(1,30))
# l2=range(1,random.randint(1,50))
# l3=[i for i in l1 if i in l2]
# print(l3)

d={
    'a':'2',
    'b':'3',
    'c':'4'
}
for i in d:
    print(i)



#   ex..11  prime num
# user=int(input('enter a num:'))
# list1=list(range(2,user))
# list2=[]
# for devisor in list1:
#     if user%devisor==0:
#         list2.append(devisor)
# if list2==[]:
#     print('this is a prime number')
# else:
#     print('this is not a prime number')


# alternative function to define prime num


# def isPrime():
#     num=int(input('enter a number:'))
#     pr_num=[]
#     for i in range(2,num):
#         if num%i ==0:
#     	    pr_num.append(i)
#     if pr_num == []:
#         return('Prime')
#     else:
#         return('Not Prime')
     
# print(isPrime())



#       ex.12 
# def first_last(l):
#     return [l[0],l[-1]]
# l=[5, 10, 15, 20, 25]
# print(first_last(l))


#       ex.13   fibonaki
# def gen_fib(count):
#     i = 1
#     if count == 0:
#         fib = []
#     elif count == 1:
#         fib = [1]
#     elif count == 2:
#         fib = [1,1]
#     elif count > 2:
#         fib = [1,1]
#         while i < (count - 1):
#             fib.append(fib[i] + fib[i-1])
#             i += 1

#     return fib
# count = int(input("How many fibonacci numbers would you like to generate? "))
# print(gen_fib(count))


#       ex.14  
# def dedupe_v1(x):
#   y = []
#   for i in x:
#     if i not in y:
#       y.append(i)
#   return y

# def dedupe_v2(x):
#     return list(set(x))

# a = [1,2,3,4,3,2,1]
# print (dedupe_v1(a))
# print (dedupe_v2(a))


#       ex.15
def reverse_word(w):
    return ' '.join(w.split()[::-1])

print(reverse_word('my name is nasib'))