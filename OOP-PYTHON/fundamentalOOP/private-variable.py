class Employee:
    def __init__(self, name, salary, department):
        # protected attribute using underscore to declare the variables
        self._name = name
        #private variable using two underscore (__)
        self.__salary = salary
        self.__department = department
        # self._showData()

    #protected method using uderscore to define its name
    def _showData(self):
        print(f"Employee name: {self._name}")
        print(f"Salary: {self.__salary}")  
        print(f"Department: {self.__department}")  

if __name__ == "__main__":
    obj1 = Employee("Billi", 200000, "CEO")
    # must define with underscore when reassign value 
    obj1._name = "MacSakaow"
    print(obj1._name)
    obj1._showData()
    # cannot alter a private variable's value
    obj1.__salary = 500000
