class Univerity:
    def __init__(self,id,name,unv_id,email):
        self.id=id
        self.name=name
        self.unv_id=unv_id
        self.email=email

class Student(Univerity):
    def __init__(self, id, name, unv_id, email,level,number_of_point,credit):
        super().__init__(id, name, unv_id, email)
        self.level=level
        self.number_of_point=number_of_point
        self.credit=credit

    def personal_info(self):
        return f"{self.id} {self.name} {self.email}"

    def calculate_gpa(self):
        return self.number_of_point/self.credit


class Teacher(Univerity):
    def __init__(self, id, name, unv_id, email,specializion,salary_per_hour,number_of_teaching_hour):
        super().__init__(id, name, unv_id, email)
        self.specializion=specializion
        self.salary_per_hour=salary_per_hour
        self.number_of_teaching_hour=number_of_teaching_hour

    def personal_info(self):
        return f"{self.id} {self.name} {self.email} {self.specializion}"    

    def calculate_salary(self):
        return (self.number_of_teaching_hour*self.salary_per_hour)*30

class Teacher_Assistant(Student,Teacher):
    def __init__(self,student_one,teacher_one):
        self.student_one=student_one
        self.teacher_one=teacher_one

student_one = Student(1,"Ali",1,"ali@a.com",4,20,10)
print(student_one.personal_info())
print(student_one.calculate_gpa())

teacher_one = Teacher(1,"Omar",1,"omar@o.com","CS",40,8)
print(teacher_one.personal_info())
print(teacher_one.calculate_salary())

teacher_Assistant = Teacher_Assistant(student_one,teacher_one)
print(teacher_Assistant.teacher_one.personal_info())
print(teacher_Assistant.teacher_one.calculate_salary())

print(teacher_Assistant.student_one.personal_info())
print(teacher_Assistant.student_one.calculate_gpa())
