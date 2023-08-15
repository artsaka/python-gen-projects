from employee import Employee

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

    def __str__(self):
        return (super.__str__()+ ", ประสบการณ์: {} ปี, ทักษะ: {}".format(self.__experience, self.__skill))