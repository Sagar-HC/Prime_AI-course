# # class Student:
# #     def __init__(self,name):
# #         self.name = name

# # std1 = Student("sagar")

# # print(std1.name)

# #online store for products

# class Store:
#     count = 0
#     def __init__(self,name ,price):
#         self.name = name
#         self.price = price
#         Store.count += 1
        
#     @classmethod
#     def get_count(cls):
#         print(f"the count of products is {cls.count}")

#     @staticmethod
#     def cal_discount(amount , discount):
#         discountwa = (amount*discount)/100
#         final_price = amount - discountwa

#         print(f"the discount of the product is{discountwa} and the final price is {final_price}") 


# prd1 = Store("iphone",200000)
# prd1.cal_discount(200000,10)


# class College:
#         subject = "MAths"

# class Student(College):
#     def __init__(self,Name):
#         self.name = Name



# st1 = Student("SAgu")

# print(st1.subject, st1.name)


# from abc import ABC # here the abc is abstract class


class Classroom:
    def __init__(self,acc_num , owner_name , balance):
        self.acc_num = acc_num
        self.owner_name = owner_name
        self.balance = balance

        
    def deposit(self, depo):
            self.balance = self.balance+depo

    def withdraw(self, withdraw):
            self.balance = self.balance - withdraw

    def check_balance(self):
            print(self.balance)

c1 = Classroom(1,"sagar",12000)
c1.deposit(100000)
c1.withdraw(12000)

c1.check_balance()



