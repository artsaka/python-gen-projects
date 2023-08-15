class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def showData(self):
        print(f"Name of employee: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Department: {self.department}")
    
if __name__ == "__main__":
    obj1 = Employee("KungFu", 20000, "Account")
    obj1.showData()
    print(obj1.__class__, '\n')
    obj2 = Employee("Sakaow", 50000, "Developer")
    obj2.showData()
    print(dir(obj2), '\n')
    
    


