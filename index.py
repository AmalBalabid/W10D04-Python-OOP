class universtyPersonnel:

     def __init__(self, id, name, universty_id,universty_email):
         self.id = id
         self.name = name
         self.universty_id = universty_id
         self.universty_email= universty_email

     def get_id(self):
         return self.id
     def get_name(self):
         return self.name
     def get_universty_id(self):
         return self.universty_id
     def get_universty_email(self):
         return self.universty_email


     def set_id(self,id):
         self.id=id
     def set_name(self,name):
         self.name=name
     def set_universty_id(self,universty_id):
         self.universty_id=universty_id
     def set_universty_email(self,universty_email):
         self.universty_email=universty_email




     def Personal_Information(self):
         return f"{self.id} {self.name} {self.universty_id} {self.universty_email}"




class Teacher(universtyPersonnel):
     def  __init__(self, id, name, universty_id,universty_email,specialization,salary_per_hour,number_teaching_hours):
         super().__init__( id, name, universty_id,universty_email)
         self.specialization = specialization
         self.salary_per_hour = salary_per_hour
         self.number_teaching_hours = number_teaching_hours
     def get_specialization(self):
         return self.specialization
     def get_salary_per_hour(self):
         return self.salary_per_hour
     def get_universty_number_teaching_hours(self):
         return self.number_teaching_hours



     def set_specialization(self,specialization):
         self.specialization=specialization
     def set_salary_per_hour(self,salary_per_hour):
         self.salary_per_hour=salary_per_hour
     def set_number_teaching_hours(self,number_teaching_hours):
         self.number_teaching_hours=number_teaching_hours


     def total_salary(self):
         total=self.salary_per_hour*self.number_teaching_hours
         return total

 # come back
     def Personal_Information(self):
         print( "",self.id ,""+ self.name +"", self.universty_id,""+self.specialization+ "",self.total_salary())

class students (universtyPersonnel):
     def  __init__(self, id, name, universty_id,universty_email,levle,number_of_points,credit):
         super().__init__( id, name, universty_id,universty_email)
         self.levle = levle
         self.number_of_points = number_of_points
         self.credit = credit
     def get_levle(self):
         return self.levle
     def get_number_of_points(self):
         return self.number_of_points
     def get_credit(self):
         return self.credit



     def set_levle(self,levle):
         self.levle=levle
     def set_number_of_points(self,number_of_points):
         self.number_of_points=number_of_points
     def set_credit(self,credit):
         self.credit=credit


     def calculating_GPA(self):
         GPA=self.number_of_points*self.credit
         return GPA



     def Personal_Information(self):
         print( "",self.id ,""+ self.name +"", self.universty_id,""+self.levle+ "",self.calculating_GPA())

class  teaching_assistant (Teacher,students):
     pass

teaher_one = Teacher(20, "Amal", 20,"amalgassam@hotmail.com", "Math",2,3)
student_one = students(20, "Noura", 20,"Nouragassam@hotmail.com", "5",20,2)
teaher_one.Personal_Information()

student_one.Personal_Information()
