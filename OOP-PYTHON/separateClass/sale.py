from employee import Employee

class Sale(Employee):
    __departmentName = "Sale Department"
    def __init__(self, name, salary, area):
        super().__init__(name, salary, self.__departmentName)       
        self.__area = area
    
    #Overloading method with additional attribute(s)
    def _showData(self):
        super()._showData()
        print(f"Sale area: {self.__area} ")

    def __str__(self):
        return (super().__str__()+", พื้นที่รับผิดชอบ: {}".format(self.__area))