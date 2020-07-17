# #       from learning python by mark lutfz


# m=[[1,2,3],[4,5,6],[7,8,9]]

# # l=[row[1] for row in m]
# # print(l)

# # g=(sum(row) for row in m)
# # print(next(g))
# # print(next(g))
# # print(next(g))

# # print(list(map(sum,m)))


# # print([ord(x) for x in 'nasib'])    #   returns an integer representing the Unicode code
# # print([ord(x) for x in 'sahed']) 
# # print([ord(x) for x in 'jahid']) 
# # print([ord(x) for x in 'hamim']) 
# # print([ord(x) for x in 'riyaz'])
# # print([ord(x) for x in 'fysal'])


#   map funtion
# num=[1,2,3,4,5]
# l=[]
# for i in num:
#     l.append(i**2)
# print(l)

# print(list(map(lambda a: a**2,num))) # map funtion does same this what above fuction is doing

#   page 147
# d={'a':1,'b':2,'c':3}
# d['a']=5
# print(d.get('a') if 'a' in d else 'missing')


#           150 page
# x=set('nasib')
# y={'t','a','n','s','i','r'}
# print(x&y)# Intersection
# print(x|y)# union
# print(x-y)#different


#               153 page
# class Worker:
#     def __init__(self,name,pay):
#         self.name=name
#         self.pay=pay

#     def lname(self):
#         l=self.name.split()[-1]
#         return l

nasib=Worker('naeemul abrar',1000)
print(nasib.lname())


a=input('ddd  ')
print(a)