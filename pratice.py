# x="Good Morning"
# print(x[::-1])
# print(x[0:6])
# print(x[0:7:2])

# def multi(a, b):
#   c=a*b
#   return c
 
# result= multi(10,10)
# print(result)


# p=int(input("enter the purchased amount"))
# if(p>1000):
#   d=p-(p*(10/100))
# print (d)

# m=int(input("eneter the marks for grade"))
# if(m<40):
#  print("D")
# elif(m>40 and m<50):
#   print("C")
# elif(m>50 and m<60):
#   print("B")
# else:
#   print("A")


# n=int(input("enter a number"))
# s=0
# while(n>0):
#  d=n%10
#  s=s+d
#  n=n//10
# print(s)


# l=["s","m", "t","s","w"]
# if ("0" in l):
#     print("founded")
# else:
#     print("not")


# n=int(input("enter number"))
# m=int(input("enter another number"))
# a=n+m
# s=n-m
# p=n*m
# d=n/m
# print(a,s,p,d)


# l=["s","m", "t","s","w"]
# if ("0" in l):
#     print("founded")
# else:
#     print("not")
# t=tuple(l)
# print(t)



# mytuple = ("apple", "banana", "cherry","orange", "kiwi", "melon", "mango")
# mytuple1=("1","2","3")
# print(mytuple)
# print(len(mytuple))
# print(mytuple[1])
# print(mytuple[-1])
# print(mytuple[2 :5])
# result=mytuple+mytuple1
# print(result)


# import numpy as np

# # Create a random number generator (RNG) with a fixed seed for reproducibility
# rng = np.random.default_rng(seed=1701)

# # Generate a 1D array (vector) with 6 random integers (0 to 9)
# x1 = rng.integers(10, size=6)

# # Generate a 2D array (matrix) of shape (3, 4) with random integers (0 to 9)
# x2 = rng.integers(10, size=(3, 4))

# # Generate a 3D array of shape (3, 4, 5) with random integers (0 to 9)
# x3 = rng.integers(10, size=(3, 4, 5))

# # Print properties of x3
# print("x3 ndim: ", x3.ndim)   # Number of dimensions
# print("x3 shape:", x3.shape)  # Shape of the array
# print("x3 size: ", x3.size)   # Total number of elements
# print("dtype: ", x3.dtype)    # Data type of array elements



# import numpy as np
# r=np.random.default_rng()
# arr1=r.integers(10,size=6)
# print(arr1)
# arr2=r.integers(10,size=(3,4))
# print(arr2)



# import numpy as np
# arr1=np.array([1,2,3,4,5,6])
# print(arr1)
# arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr2)


# for i in range(1,10):
#  print(i)




# import numpy as np
# arr1=np.array([1,2,3,4,5,6])
# print(arr1)
# a=np.sum(arr1)
# s=np.max(arr1)
# p=np.prod(arr1)
# d=np.min(arr1)
# print(a,s,p,d)





# import pandas as pd

# # Series Example
# data_series = pd.Series([10, 20, 30, 40], index=['A', 'B', 'C', 'D'])
# print("Series:\n", data_series)

# # DataFrame Example
# data_frame = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'Los Angeles', 'Chicago']
# })
# print("\nDataFrame:\n", data_frame)


# import pandas as pd
# d=pd.DataFrame({'name':['s','m'],
#             'age':[21,23],
#             'marks':[10,80]})
# print(d)


# print(d.iloc[1])



# import pandas as pd

# # Load NYC Taxi Dataset
# url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
# df = pd.read_csv(url)

# print("NYC Taxi Dataset:\n", df.head())




# class Car:
#     def __init__(self, brand, model):
#         self.brand = brand  # Encapsulation
#         self.model = model

#     def display_info(self):  # Abstraction
#         return f"Car Brand: {self.brand}, Model: {self.model}"

# # Inheritance and Polymorphism
# class ElectricCar(Car):
#     def __init__(self, brand, model, battery_capacity):
#         super().__init__(brand, model)
#         self.battery_capacity = battery_capacity

#     def display_info(self):  # Polymorphism
#         return f"{super().display_info()}, Battery: {self.battery_capacity} kWh"

# car1 = ElectricCar("Tesla", "Model S", 100)
# print(car1.display_info())





# class Car:  # Class name should be capitalized (PEP8 convention)
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display(self):
#         return f"Car brand: {self.brand}, Car model: {self.model}"


# class Ele(Car):  # Inheriting from Car class
#     def __init__(self, brand, model, battery):  # Fix the method name
#         super().__init__(brand, model)  # Call parent class constructor
#         self.battery = battery  # Define the battery attribute

#     def display(self):
#         return f"{super().display()}, Car battery: {self.battery}"  # Fix method call


# # Create an instance of the Ele class
# c = Ele("Tesla", "SS", 100)
# print(c.display())  # Call the display method


    