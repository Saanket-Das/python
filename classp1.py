# IMPORTING SAMPLE DATA
# print("Sanket Kumar Das", "24MCA10060")
# !ls


#SYSTEM INFO
# print("Sanket Kumar Das", "24MCA10060")
# !cat /proc/cpuinfo


#THIS SECTION
# print("Sanket Kumar Das", "24MCA10060")
# print("This is a section")


#PRINT A NUMBER
# print("Sanket Kumar Das", "24MCA10060")
# a = 10
# print(a)
# type(a)



# print("Sanket Kumar Das", "24MCA10060")
# a+=10
# print(a)

# print("Sanket Kumar Das", "24MCA10060")
# b = 30
# print(a+b)

# print("Sanket Kumar Das", "24MCA10060")
# branch = 'MCA'
# print(branch)
# print(id(branch))


# print("Sanket Kumar Das", "24MCA10060")
# branch += ' from VIT'
# print(branch)



# print("Sanket Kumar Das", "24MCA10060")
# reg = ' 24MCA10060'
# print(branch+reg)


#PRINT NAME
# print("Sanket Kumar Das", "24MCA10060")
# name = input("Enter your name : ")
# print("My name is " + name)



# print("Sanket Kumar Das", "24MCA10060")
# print("%s"%name)



#SUM OF NUMBERS
# print("Sanket Kumar Das", "24MCA10060")
# print('Hello')
# print("Sanket Kumar Das", "24MCA10060")
# A=20
# B=10
# C=A+B
# print(C)



# print("Sanket Kumar Das", "24MCA10060")
# print(x[0])
# print(x[0:5])
# print(x[0:])
# print(x[0:-1])
# print(x[0:-2])
# print(x[::-1])
# print(x[-8:-1:2])
# print(x[0:12:3])


#   DETERMING THE BIRTH YEAR FROM CURRENT YEAR
# print("Sanket Kumar Das", "24MCA10060")
# year=input("enter the the birth year")
# year1=input("enter current year")
# age=int(year1)-int(year)
# print(age)


#REVERSE OF A STRING
# print("Sanket Kumar Das", "24MCA10060")
# # reverse string
# a = "Hello World"
# rev_str = a[::-1]
# print(rev_str)

#DOC FORMAT
# def multiplier(a, b):
#     """Take two numbers and return their product."""
#     return a*b


#CHANGING A STRING AT A SPECIFIC INDEX
# print("Sanket Kumar Das", "24MCA10060")
# b = "CourseRegistration"
# rev_str1 = b[-8:-1:2]
# print(rev_str1)
# print(b.replace("course", "sanket"))

#DICOUNT AMOUNT CALCULATION
# print("Sanket Kumar Das", "24MCA10060")
# p=int(input("enter purschase amount"))
# d=p*(10/100)
# if(p>10000):
#     print(p-d)
# else:
#    print("n0 discount")


#POSITIVE NEGETIVE NUMBER
# print("Sanket Kumar Das", "24MCA10060")
# n=eval(input("enter a number"))
# if n()>0):
#     print("it is a positive number")
# else:
#     print("it is a negetive number")


#LEAP YEAR OR NOT
# print("Sanket Kumar Das", "24MCA10060")
# y= int(input("enter a year"))
# if y%100==0:
#     print("it is a leap year")
# elif y%4==0 and y%10 !=0:
#     print("it is a leap year")
# else:
#      print("it is not a leap year")   



#DECIDE THE GRADE
# print("Sanket Kumar Das", "24MCA10060")
# m= int(input("enter the marks"))
# if (m<40):
#     print("grade D")
# elif(m>40 and m<50 ): 
#     print("grade C") 
# elif(m>50 and m<60 ):    
#     print("grade B")
# elif(m>60 and m<70 ):    
#     print("grade A")
# else:
#    print("grade O") 


#WHILE LOOP
print("Sanket Kumar Das", "24MCA10060")
n=int(input("enter a number"))
s=0 
i=1
while (i<=n):
    s=s+i
    i=i+1
    print(s)


#FACTORIAL OF A NUMNER
print("Sanket Kumar Das", "24MCA10060")
n=int(input("enter a number"))
f=1
i=1
while(i<=n):
    f=f*i
    i=i+1
print(f)


#SUM OF DIGITS
# print("Sanket Kumar Das", "24MCA10060")
# n=int(input("enter a number"))
# s=0
# while(n>0):
#     d=n%10
#     s=s+d
#     n=n//10
# print(s)   


#GREATEST OF ALL NUMBER
# print("Sanket Kumar Das", "24MCA10060")
# num1 = eval(input("Enter first number: "))
# num2 = eval(input("Enter second number: "))
# num3 = eval(input("Enter third number: "))
# if num1 > num2:
#   if num1 > num3:
#     print(num1, "- First number is the greatest number")
#   else:
#     print(num3, "- Second number is the greatest number")
# else:
#   if num2 > num3:
#     print(num2, "- Second number is the greatest number")
#   else:
#     print(num3, "- Third number is the greatest number")



#LIST 
# print("Sanket Kumar Das", "24MCA10060")
# l = ["Apple", "Mango", "Grapes"]
# if "Mango" in l:
#   print("Mango is present.")
# else:
#   print("Mango is not present.")


# AARITHMETIC OPERATORS
# print("Sanket Kumar Das", "24MCA10060")
# x=10
# y=20
# z=x+y
# print(z)



#POSTIVE NEGETIVE NUMBER
# print("Sanket Kumar Das", "24MCA10060")

# number = eval(input("Enter any number: "))
# if number < 0:
#   print("Negative number")
# else:
#   print("Positive number")


#LEAP YEAR USING ONW CONDITION
# print("Sanket Kumar Das", "24MCA10060")
# year = eval(input("Enter any year: "))
# if year%4==0:
#   print("Leap year")
# else:
#   print("Not a leap year")



#GRADE DETERMINATION
# print("Sanket Kumar Das", "24MCA10060")
# if
# elif & else
# marks = int(input("Enter your marks: "))
# if marks>=90:
#   print("Grade S")
# elif marks>=80:
#   print("Grade A")
# elif marks>=70:
#   print("Grade B")
# elif marks>=40:
#   print("Grade C")
# else:
#   print("Fail")


#GREATEST USING ONLY IF
# print("Sanket Kumar Das", "24MCA10060")
# num1 = 10
# num2 = 14
# num3 = 12
# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# if (num2 >= num1) and (num2 >= num3):
#     largest=num2
# if (num3>num1) and (num3>num2):
#    largest = num3

# print("The largest number is", largest)



#USING MAX FUNCTION
# print("Sanket Kumar Das", "24MCA10060")
a, b, c = input("Enter three numbers separated by spaces: ").split()
a = float(a)
b = float(b)
c = float(c)
print(max(a, b, c))



#FINDING MAX
# print("Sanket Kumar Das", "24MCA10060")
# def findlargest(n1, n2, n3):
#   if n1>n2 and n1>n3:
#     return n1
#   elif n2>n1 and n2>n3:
#     return n2
#   else:
#     return n3
# n1 = float(input("Enter first number: "))
# n2 = float(input("Enter second number: "))
# n3 = float(input("Enter third number: "))
# result = findlargest(n1, n2, n3)
# print(f"The largest number among {n1}, {n2}, and {n3} is {result}.")


#ASCII VALUE OF STRINGS
# print("Sanket Kumar Das", "24MCA10060")
# import string
# alphabets = string.ascii_lowercase
# for ch in alphabets:
#   print("Character: "+ ch + " ASCII value: "+ str(ord(ch)))




# print("Sanket Kumar Das", "24MCA10060")
# n=[float(input("enter number{}:".format(1+1))) for i in range(3)]
# l=max(*n)
# print("the largest number {l}.")



#TUPLE
print("Sanket Kumar Das", "24MCA10060")
# convert list to tuple
list1 = [1, 2, 3, 4, 5]
tuple1 = tuple(list1)
print(tuple1)
print(list1)


#TUPLEE
# print("Sanket Kumar Das", "24MCA10060")
# mytuple = ("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
# mytuple1=("1","2","3")
# print(mytuple)
# print(len(mytuple))
# print(mytuple[1])
# print(mytuple[-1])
# print(mytuple[2:5])
# result=mytuple+mytuple1
# print(result)


#ADDING TUPLES
# print("Sanket Kumar Das", "24MCA10060")
# a = (20,30,60,"apple", "ball")
# print(a[0])
# print(a[2])

# print("Sanket Kumar Das", "24MCA10060")
# print(a[1:3])
# b = (2,4)
# print(a+b)
# print(b*2) 

