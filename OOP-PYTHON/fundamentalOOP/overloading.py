# Overloading
# method has the same name with different parameters i.e constructor 
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
    
    

# child class inherit the parent's attributes
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


class Programmer(Employee):
    __deptpartmentName = "Programmer - Technology C"
    def __init__(self, name, salary, experience, skill):
        super().__init__(name, salary, self.__deptpartmentName)        
        self.__experience = experience
        self.__skill = skill
    
    #Overloading method with additional attribute(s)
    def _showData(self):
        super()._showData()
        print(f"Experience: {self.__experience} year(s)")
        print(f"Skill: {self.__skill}")
        

class Sale(Employee):
    __departmentName = "Sale Department"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)       
        self.__area = area
    
    #Overloading method with additional attribute(s)
    def _showData(self):
        super()._showData()
        print(f"Sale area: {self.__area} ")


if __name__ == "__main__":
    employee = Employee("Hans", 40000, "Procurement")
    employee._showData()
    # print(f"Annual income is {employee._getIncome()}")
    # print(employee.__str__())
    print('\n')

    programmer = Programmer("Jada", 35000, 2, "Game development")
    # print("Annual income is {}".format(programmer._getIncome()))
    # programmer._showData()
    # print(programmer.__str__())    
    print('\n')
    
    account = Accounting("Mana", 30000, 35)
    # print("Annual income is", str(account._getIncome()))
    account._showData()
    print(account.__str__())
    print('\n')

    sale = Sale("Sala", 35000, "เชียงใหม่")
    print(f"Annual income is {sale._getIncome(500, 10000)}")
    # sale._showData()
    # print(sale.__str__())
    print('\n')
    