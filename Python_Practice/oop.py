



# #               object oriented programming


# class brothers():
#     incr=2
#     n_b=0
#     def __init__(self,fname,lname,age,pocket_money):
#         self.fname=fname
#         self.lname=lname
#         self.age=age
#         self.pocket_money=pocket_money
#         brothers.n_b+=1

# #           instance method
#     # def m_incr(self):
#     #     self.pocket_money=int(self.pocket_money*self.incr)       #  this is best
#         # self.pocket_money=int(self.pocket_money*brothers.incr)    # this is unique
        

# #   class method ----> vi-4   
#     # @classmethod         #   decorators
#     # def chng_incr(cls,amount):
#     #     cls.incr=amount

# #       vi----5 
#     # @classmethod #  as an alternative constructor
#     # def from_str(cls,string):
#     #     fname,lname,age,pocket_money=string.split('-')  #   arguments should be same 
#     #     return cls(fname,lname,age,pocket_money)

#     # @staticmethod  # it doesn't call neither class nor object's variable
#     # def is_open(day):
#     #     if day=='friday':
#     #         return(False)
#     #     else:
#     #         return True

# #           vi----7 
# #               inheritance
# # class older_bro(brothers):
# #     def __init__(self,fname,lname,age,pocket_money,school,label):
# #         super().__init__(fname,lname,age,pocket_money)  # to call parent class
# #         self.school=school
# #         self.label=label

# #     def m_incr(self):
# #         self.pocket_money=int((self.pocket_money*self.incr)+100)

# #           vi------9
#     @property           #   it will be trated like a variable
#     def email(self):
#         return self.fname+self.lname+'@gmail.com'
    
#     @email.setter
#     def email(slef,given_email):
#         name_list=given_email.split('@')[0].split('.')
#         slef.fname=name_list[0]
#         slef.lname=name_list[1]




# #               vi---9
# # import harshit_course # this is extra
# # harshit_course.imprtnt()

# if __name__ == "__main__":
#     nasib=brothers('naeemul abrar','nasib',17,300)
#     tansir=brothers('tansiruj jaman','tansir',12,100)
#     tansir.lname='modo'
#     print(nasib.email,tansir.email)
#     tansir.email='modo.tansir@gmail.com'
#     print(nasib.email,tansir.email)



# #               vi---8
# #   its about dunder/magic method



# #           vi-----7
# # print(nasib.label)
# # nasib.m_incr()
# # print(nasib.pocket_money)
# # help(older_bro)


# #           vi-----6
# # print(brothers.is_open('sunday'))

# #           vi--- 5

# # hasib=brothers.from_str('asharafuz-hasib-1-10')
# # print(hasib.pocket_money)



# #               vi---4

# # print(nasib.pocket_money)
# # nasib.chng_incr(4)
# # # nasib.incr=4
# # nasib.m_incr()
# # print(nasib.pocket_money)


# #    vi---3


# # print(nasib.pocket_money)
# # nasib.m_incr()
# # print(nasib.pocket_money)



# # print(brothers.__dict__)   #   __dict__ to see the varaibles of class
# # print(nasib.__dict__)          #   __dict__ to see the personal varaibles of any object


# # nasib.incr=5                     #   i can change personally the value of any variable and there it changes for only nasib
# # print(nasib.__dict__)
# # nasib.m_incr()
# # print(nasib.pocket_money)




# #   vi--- 2

# # print(nasib.fname,tansir.lname)

