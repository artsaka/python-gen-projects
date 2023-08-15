from employee import Employee

class Accounting(Employee):
    __departmentName = "Accounting Department"
    def __init__(self, name, salary, age):
        # while instantiate...Do not pass the value when using its own department name. 
        super().__init__(name, salary, self.__departmentName)        
        self.__age = age

    #Overloading method with additional attribute(s)    
    def _showData(self):
        super()._showData()
        print(f"Age: {self.__age}")

    #Overloading method toString() method
    def __str__(self):
        return (f"{super().__str__()} \nAge: {self.__age} years old")