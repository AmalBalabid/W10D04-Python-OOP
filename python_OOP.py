class Universty_personnel:
    def __init__(self,id,name,university_id,university_email):
        self.id=id
        self.name=name
        self.university_id=university_id
        self.university_email = university_email

    def Personal_Information(self):
        return f"{self.id} {self.name} {self.university_id} {self.university_email}"

#setters
    def set_id(self,id):
        self.id=id
    def set_name(self,name):
        self.name=name
    def set_university_id(self,university_id):
        self.university_id=university_id
    def set_university_email(self,university_email):
        self.university_email=university_email
#getters
    def get_id(self):
        return self.id
    def get_name(self):
        return self.name
    def get_university_id(self):
        return self.university_id
    def get_university_email(self):
        return self.university_email
#child1 class
class Teacher(Universty_personnel):
    def __init__(self,id,name,university_id,university_email,specialization,salary_per_hour,number_of_teaching_hours):
        super().__init__(id,name,university_id,university_email)
        self.specialization=specialization
        self.salary_per_hour=salary_per_hour
        self.number_of_teaching_hours=number_of_teaching_hours
#setters
    def set_specialization(self,specialization):
        self.specialization=specialization
    def set_salary_per_hour(self,salary_per_hour):
        self.salary_per_hour
    def set_number_of_teaching_hours(self,number_of_teaching_hours):
        self.number_of_teaching_hours
#getters
    def get_specialization(self):
        return self.specialization
    def get_salary_per_hour(self):
        return self.salary_per_hour
    def get_number_of_teaching_hours(self):
        return self.number_of_teaching_hours
#Total salary method
    def Total_salary(self):
        return self.salary_per_hour * self.number_of_teaching_hours
#Override Personal Information method 
    def Personal_Information(self):
        return super().Personal_Information(),f" {self.specialization} {self.salary_per_hour} {self.number_of_teaching_hours}"
#child2 class 
class Students(Universty_personnel):
    def __init__(self,level,number_of_points,credit):
        self.level=level
        self.number_of_points=number_of_points
        self.credit=credit
#calculate the GPA method
    def Calculate_GPA(self):
        return self.number_of_points * self.credit
#setters
    def set_level(self,level):
        self.level=level
    def set_number_of_points(self,number_of_points):
        self.number_of_points=number_of_points
    def set_credit(self,credit):
        self.credit=credit
#getters
    def get_level(self):
        return self.level
    def get_number_of_points(self):
        return self.number_of_points
    def get_credit(self):
        return self.credit
#child3 class
class Teaching_Assistant(Teacher,Students):
    pass

# person1 = Universty_personnel("1", "norah", 4359779,"norah@tuwaiq.com")
# print(person1.Personal_Information())
teacher=Teacher("1","amal",685678,"amal@tuwaiq.com","Math",100,8)
print(teacher.Personal_Information())
print(teacher.Total_salary())
student=Students("5",90,10)
print(student.Calculate_GPA())