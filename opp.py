class University  :
    def __init__(self,id,name, university_id ,email):
        self.id=id
        self.name=name
        self.university_id=university_id
        self.email=email

    def personal_info(self):
        print("the id ",self.id," the name ",self.name," the university id ", self.university_id," email " ,self.email)
    def get_id(self):        
            return self.id
    def set_id(self, id):           
            self.id = id
    def get_name(self):        
            return self.name
    def set_name(self, name):           
            self.name = name
    def get_uId(self):        
            return self.university_id
    def set_uId(self, university_id):           
            self.university_id = university_id
    def get_email(self):        
            return self.email
    def set_email(self, email):           
            self.email = email
    
personal_univ=University(1,"sara",3,"zxc@zxc.com")
personal_univ.personal_info()


class Teacher(University):
        def __init__(self, id, name, university_id, email,specialization ,salary_per_hour,number_of_teaching_hours):
            super().__init__(id, name, university_id, email)
            self.specialization=specialization
            self.salary_per_hour=salary_per_hour
            self.number_of_teaching_hours=number_of_teaching_hours
        def get_specialization(self):        
            return self.specialization
        def set_specialization(self, specialization):           
            self.specialization = specialization
        def get_salary_per_hour(self):        
            return self.salary_per_hour
        def set_salary_per_hour(self, salary_per_hour):           
            self.salary_per_hour = salary_per_hour
        def get_number_of_teaching_hours(self):        
            return self.number_of_teaching_hours
        def set_number_of_teaching_hours(self, number_of_teaching_hours):           
            self.number_of_teaching_hours = number_of_teaching_hours
               
            
        def personal_info(self):
            return super().personal_info(),"specialization",self.specialization,"salary per hour",self.salary_per_hour,"number of teaching hours",self.number_of_teaching_hours
        
        def calculate_salary(self):
                return "the total salary is ",(self.salary_per_hour*self.number_of_teaching_hours)
        
teacher_object = Teacher(1, "nora", 3, "nora@ghj.com", "math", 123, 3)
print(teacher_object.personal_info())
print(teacher_object.calculate_salary())

class Student(University):
        def __init__(self, id, name, university_id, email ,level, number_of_points, credit):
            super().__init__(id, name, university_id, email)
            self.level=level
            self.number_of_points=number_of_points
            self.credit=credit
        def get_level(self):        
            return self.level
        def set_level(self, level):           
            self.level = level
        def get_number_of_points(self):        
            return self.number_of_points
        def set_number_of_points(self, number_of_points):           
            self.number_of_points = number_of_points
        def get_credit(self):        
            return self.credit
        def set_credit(self, credit):           
            self.credit = credit
        
        def personal_info(self):
            print(super().personal_info(),"the level ",self.level,"number of points",self.number_of_points,"the credit ",self.credit)
    
        def culcalet_gpa(self):
                return "the GPA IS ",(self.number_of_points*self.credit)
Student_object= Student(1 ,"reem",2,"as@asd.co",4,8,4)
print(Student_object.culcalet_gpa())

class Tetcher_Assistant(Teacher,Student):
        def __init__(self, id, name, university_id, email, specialization, salary_per_hour, number_of_teaching_hours):
            super().__init__(id, name, university_id, email, specialization, salary_per_hour, number_of_teaching_hours)  

test=Tetcher_Assistant(1,"nahed",3,"sdfg@sdf","math",234,54)
