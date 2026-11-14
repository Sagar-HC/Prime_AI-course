# num = int(input("enter your number:"))

# if(num % 2 == 0):
#     print("even")
# else:
# #     print("jaa re chirkut")
# i = 1
# n = int(input("enter your number:"))
# i = 1
# multiplication =1
# while(i<=10):
#     print( f"{n} * {i} =" , n*i)
#     i +=1


# word = "artificial intelligence"
# count_i = 0
# for char in word:
#     if(char == 'i'):
#         count_i +=1
# print(count_i)

#sum of n natural numbers
# sum=0
# n = int(input("enter number:"))
# for i in range(n):
#     sum+=i+1
# print(sum)

# def sum(a,b):
#     c = a+b
#     print(c)

# sum(10,20)

def fact(n):
    factorial = 1
    for i in range(1,n+1):
        factorial= factorial*i
    print(factorial) 

n = int(input("enter your number :")) 
fact(n)