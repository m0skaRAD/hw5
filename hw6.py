class Student:
    def __init__(self, name, age, year, grade):
        self.name = name
        self.age = age
        self.year = year
        self.grade = grade

    def info(self):
        print(f"Student: {self.name}, Age: {self.age}, Year: {self.year}, Grade: {self.grade}")

    def increase_year(self):
        self.year += 1

    def update_grade(self, new_grade):
        self.grade = (self.grade + new_grade) / 2

student1 = Student("Nastya", 20, 1, 85)
student1.info()  

student1.increase_year()
student1.info()  

student1.update_grade(200)
student1.info()  
