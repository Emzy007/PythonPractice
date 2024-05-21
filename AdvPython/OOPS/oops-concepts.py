class Student:
    def __init__(self, id, marks):
        self.id = id
        self.__marks = marks
    def set_marks(self, marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def __add__(self,other):
        print(f'{other.get_marks()} - {self.get_marks()} =',(other.get_marks() - self.get_marks()))
Student(1,90) + Student(2,40)