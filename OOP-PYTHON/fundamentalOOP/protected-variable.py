class Employee:
    def __init__(self, name, salary, department):
        # protected attribute using underscore to declare the variables
        self._name = name
        self._salary = salary
        self._department = department
        self._showData()

    #protected method using uderscore to define its name
    def _showData(self):
        print(f"Employee name: {self._name}")
        print(f"Salary: {self._salary}")  
        print(f"Department: {self._department}")  

if __name__ == "__main__":
    obj1 = Employee("Billi", 200000, "CEO")
    # must define with underscore when reassign value 
    obj1._name = "MacSakaow"
    print(obj1._name)
