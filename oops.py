
class Employee:
  def __init__(self, name, salary):
   self.name = name
   self.salary = salary
  def getSalary(self):
   return self.salary
rohan =Employee("Rohan" ,"3455")
print(rohan.salary)
print(rohan.name) 
rohan =Employee("sanket" ,"355")
print(rohan.salary)
print(rohan.name) 