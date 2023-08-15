# Inheritance
class Employee:
    # Class variables
    minSalary = 20000
    maxSalary = 150000
    companyName = "Berich PyLtd"

    def __init__(self, name, salary, department):
        # instance variables
        self.__name = name
        self.__salary = salary
        self._department = department
    
    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self.__salary = salary

    def setDepartment(self, department):
        self._department = department
    
    def getName(self):
        return self.__name
    
    def getSalary(self):
        return self.__salary
    
    def getDepartment(self):
        return self._department
    
    # Annual income
    def _getIncome(self):
        return self.getSalary() * 12

    def _showData(self):
        print(f"Employee name: {self.getName()}")
        print(f"Salary: {self.getSalary()}")
        print(f"Department: {self.getDepartment()}")
    

    # Display information using string method
    def __str__(self):
        return f"Employee Name: {self.__name} \nDepartment: {self._department} \nSalary: {self.getSalary()} \nAnnual income is {self._getIncome()}"
    
    

# child class inheritance the parent's attributes
class Accounting(Employee):
    __departmentName = "Accounting Department"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)
        # super()._showData()
        


class Programmer(Employee):
    __deptpartmentName = "Technology Consulting"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__deptpartmentName)
        # super()._showData()
        

class Sale(Employee):
    __departmentName = "Sale Department"
    def __init__(self, name, salary):
        super().__init__(name, salary, self.__departmentName)       
        # super()._showData()
        

if __name__ == "__main__":
    employee = Employee("Hans", 40000, "Programmer")
    employee._showData()
    # print(f"Annual income is {employee._getIncome()}")
    # print(employee.__str__())
    print('\n')

    programmer = Programmer("Jada", 35000)
    # print("Annual income is {}".format(programmer._getIncome()))
    # programmer._showData()
    print(programmer.__str__())    
    print('\n')
    
    account = Accounting("Mana", 30000)
    # print("Annual income is", str(account._getIncome()))
    print(account.__str__())
    print('\n')

    sale = Sale("Sala", 35000)
    # print(f"Annual income is {sale._getIncome()}")
    print(sale.__str__())
    print('\n')
    