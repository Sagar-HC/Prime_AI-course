# class Student:
#     def __init__(self,name):
#         self.name = name

# std1 = Student("sagar")

# print(std1.name)

#online store for products

class Store:
    count = 0
    def __init__(self,name ,price):
        self.name = name
        self.price = price
        Store.count += 1
        
    @classmethod
    def get_count(cls):
        print(f"the count of products is {cls.count}")

    @staticmethod
    def cal_discount(amount , discount):
        discountwa = (amount*discount)/100
        final_price = amount - discountwa

        print(f"the discount of the product is{discountwa} and the final price is {final_price}") 


prd1 = Store("iphone",200000)
prd1.cal_discount(200000,10)