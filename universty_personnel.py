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

# --------------- teacher class ------------------
class teacher(universty_personnel):
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

teacher1 = teacher(437,"gg",437000000,"salwu@.edu.sa","math",100,8)
print(teacher1.Personal_Information())