"""

identifiers without underscore are considered as public, can be accessed any where
__private has two underscores and can be accessed only in the class
_protected has one underscore and can be accessed in the class and its child

Each modifier allow degree of accessing object(s) by other methods or assignment
"""

#Encapsulation using private method
class Employee:
    def __init__(self, name, salary, department):
        self.__name = name  # private
        self.__salary = salary  # private
        self._department = department # protected
        self._showData()

    # protected method
    def _showData(self):
        print(f"Employee name: {self.__name}")
        print(f"Salary: {self.__salary}")
        print(f"Department: {self._department}")

if __name__ == "__main__":
    #create a new instance(object) via constructor
    obj1 = Employee("Nana", 20000, "HR")
    # private attribute cannot re-assign a new value
    obj1.__name = "Victoria" 
    # protected attribute can be reassigned a new value
    obj1._department = "Account"
    obj1._showData()