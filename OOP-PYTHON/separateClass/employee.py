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
    
    def _getIncome(self, overtime=0, bonus=0):
        return (self.getSalary()*12) + overtime + bonus

    def _showData(self):
        print(f"Employee name: {self.getName()}")
        print(f"Salary: {self.getSalary()}")
        print(f"Department: {self.getDepartment()}")
    

    # Display information using string method
    def __str__(self):
        return f"Employee Name: {self.__name} \nDepartment: {self._department} \nSalary: {self.getSalary()} \nAnnual income is {self._getIncome()}"
