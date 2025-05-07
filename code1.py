



class Car:
    def __init__(self,brand, model):
        self.brand =brand
        self.model=model
    def display(self):
        return f"Car brand : {self.brand} ,car model :{self.model} "
class Ele(Car):
    def __init__(self, brand, model,battery):
        super().__init__(brand,model)
        self.battery   =battery

    def display(self):
         return f"{super().display()} ,car battery :{self.battery} "       
    
c=Ele("tesla","ss",100)
print(c.display()) 
