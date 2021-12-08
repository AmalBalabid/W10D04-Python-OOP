class Universty_Personnel:
​
    def __init__(self, id, name, university_id, university_email):
        self.id = id
        self.name = name
        self.university_id = university_id
        self.university_email = university_email 

    def Personal_Information(self):
        return f"{self.id} {self.name} {self.university_id} {self.university_email}"


    def get_id(self):
         return self.id

    def set_id(self, id):
        self.id = id 

    def get_name(self):
         return self.name

    def set_name(self, name):
        self.name = name

    def get_university_id(self):
         return self.university_id

    def set_university_id(self, university_id):
        self.university_id = university_id   


     def get_university_email(self):
         return self.university_email

    def set_university_email(self, university_email):
        self.university_email = university_email          



class Teacher(Universty_Personnel):

    def __init__(self, specialization, salary_per_hour, number_of_teaching_hours):
        super().__init__(self.id, self.name, self.university_id, self.university_email)
        self.specialization = specialization
        self.salary_per_hour = salary_per_hour
        self.number_of_teaching_hours = number_of_teaching_hours


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
        

    def total_salary(self):
        return self.salary_per_hour * self.number_of_teaching_hours 

    def Personal_Information(self):
        return super(), f"{self.specialization} {self.salary_per_hour} {self.number_of_teaching_hours}"


class Students(Universty_Personnel): 

    def __init__(self, id, name, university_id, university_email, level, number_of_points, credit):
        super().__init__(self.id, self.name, self.university_id, self.university_email)
        self.level = level
        self.number_of_points = number_of_points
        self.credit = credit  




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


    def GPA(self):
        return self.number_of_points * self.credit  


class Teaching_Assistant(Teacher,Students):
    pass


student = Students(1,"Reema",123,"Reema@jh1223",3, 5, 9)
teacher = Teacher (2,"Norah",456,"Norah@jh1223","Math", 500, 20)



