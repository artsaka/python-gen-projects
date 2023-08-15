"""
We do not want to assign or access the values of attributes directly to constructor
setter method helps us to assign (new) values to the constructor's variables
getter method helps us to access or read the values of variables (return variable)
"""
class Emplyee:
    # constructor
    def __init__(self, name, salary, department):
        self.__name = name   # private variable has two underscores
        self.__salary = salary
        self._department = department  # protected variable has one underscore

    # protected method be able to access within the class and its child
    def _showData(self):
        print(f"Employee name: {self.getName()}")
        print(f"Salary: {self.getSalary()}")
        print(f"Department: {self.getDepartment()}")
        print("Print casting int to string", str(self.getSalary()))

    def setName(self, name):
        self.__name = name
    
    def setSalary(self, salary):
        self.__salary = salary

    def setDepartment(self, department):
        self._department = department

    # returns the value of the attribute
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getDepartment(self):
        return self._department

if __name__ == '__main__':
    obj1 = Emplyee("Pru", 20000, "Account")
    obj1._showData()

    print("Excellent emplyee:", obj1.getName())

