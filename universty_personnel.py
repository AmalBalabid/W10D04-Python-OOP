# --------------- universty_personnel class ------------------
class universty_personnel:
    def __init__ (self ,id,name,university_id,university_email):
        self.id = id
        self.name = name
        self.university_id = university_id
        self.university_email = university_email
    
    def Personal_Information(self):
        return f"{self.id} - {self.name} - {self.university_id} - {self.university_email}"
    
    def set_id(self,id):
        self.id=id

    def get_id(self):
        return self.id

    def set_name(self,name):
        self.name=name
        
    def get_name(self):
        return self.name

    def set_university_id(self,university_id):
        self.university_id=university_id
        
    def get_university_id(self):
        return self.university_id

    def set_university_email(self,university_email):
        self.university_email=university_email
        
    def get_university_email(self):
        return self.university_email

u_p = universty_personnel(437,"Saad",437000000,"salwu@###.edu.sa")
u_p.set_university_email("test@gmail.com")
print(u_p.Personal_Information())
print("---------------------------------")


# --------------- Teacher class ------------------
class Teacher(universty_personnel):
    def __init__ (self ,id,name,university_id,university_email,specialization,salary_per_hour,number_of_teaching_hours):
        super().__init__(id,name,university_id,university_email)
        self.specialization=specialization
        self.salary_per_hour=salary_per_hour
        self.number_of_teaching_hours=number_of_teaching_hours
    
    
    def Personal_Information(self):
        return f"{self.id} - {self.name} - {self.university_id} - {self.university_email} - {self.specialization} - {self.salary_per_hour}"
    
    def set_specialization(self,specialization):
        self.specialization=specialization
        
    def get_specialization(self):
        return self.specialization

    def set_salary_per_hour(self,salary_per_hour):
        self.salary_per_hour=salary_per_hour
        
    def get_salary_per_hour(self):
        return self.salary_per_hour

    def set_number_of_teaching_hours(self,number_of_teaching_hours):
        self.number_of_teaching_hours=number_of_teaching_hours
        
    def get_number_of_teaching_hours(self):
        return self.number_of_teaching_hours
    
    def total_salary(self):
        return (self.get_salary_per_hour()) * (self.get_number_of_teaching_hours())

teacher1 = Teacher(437,"gg",437000000,"salwu@.edu.sa","math",100,8)
print(teacher1.Personal_Information())
print("---------------------------------")

# --------------- Students class ------------------
class Students(universty_personnel):
    def __init__ (self ,id,name,university_id,university_email,level,number_of_points,credit):
        super().__init__(id,name,university_id,university_email)
        self.level=level
        self.number_of_points=number_of_points
        self.credit=credit
    
    def Personal_Information(self):
        return f"{self.id} - {self.name} - {self.university_id} - {self.university_email} - {self.calculating_gpa()}"
    
    def set_level(self,level):
        self.level=level
        
    def get_number_of_teaching_hours(self):
        return self.number_of_teaching_hours

    def set_number_of_points(self,number_of_points):
        self.number_of_points=number_of_points
        
    def get_number_of_points(self):
        return self.number_of_points

    def set_credit(self,credit):
        self.credit=credit
        
    def get_credit(self):
        return self.credit
    
    def calculating_gpa(self):
        return (self.credit) * (self.number_of_points)

students1 = Students(123,"John",3232,"johan@z.edu",4,10,2)
print(students1.Personal_Information())
print("---------------------------------")

# --------------- Teaching_Assistant class ------------------
class Teaching_Assistant(Teacher,Students):
    def __init__ (self ,teacher,students):
        self.teacher=teacher
        self.students=students
#  for testing multi inherits
#     def __init__ (self ,id,name,university_id,university_email,specialization,salary_per_hour,number_of_teaching_hours,level,number_of_points,credit):
#         Teacher.__init__(self,id,name,university_id,university_email,specialization,salary_per_hour,number_of_teaching_hours)
#         Students.__init__(self,id,name,university_id,university_email,level,number_of_points,credit)
# Teaching_Assistantz1 = Teaching_Assistant(437,"gg",437000000,"salwu@.edu.sa","math",100,8,4,10,8)

students2 = Students(436,"saad",43700,"SaadAl@z.edu",2,22,222)
teacher2 = Teacher(437,"Saad",437000000,"Dr.Saad@edu.sa","math",100,8)

Teaching_Assistantz1 = Teaching_Assistant(teacher2,students2)
print(Teaching_Assistantz1.students.Personal_Information())
print(Teaching_Assistantz1.teacher.Personal_Information())
