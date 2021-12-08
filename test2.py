# Create a universty personnel class (parent class) contains:

class universty_personnel :
    def __init__(self,id, name,university_id,university_email):
        self.id = id
        self.name = name
        self.university_id = university_id
        self.university_email= university_email

   
#    Method called Personal_Information which will return all that person's information.
    def Personal_Information(self):
       return f"{self.id} {self.name} {self.university_id} {self.university_email}"

   
#    Setter and getter for all attributes
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


      
#Create a teacher class (child class, extend from universty personnel) contains:

class Teacher(universty_personnel):
    def __init__(self,id, name,university_id,university_email,specialization,salary_hour,teaching_hours):
        super().__init__(self,id, name,university_id,university_email)
        self.specialization = specialization
        self.salary_hour = salary_hour
        self.teaching_hours = teaching_hours

    def get_specialization(self):
         return self.specialization
    def set_specialization(self, specialization):
        self.specialization = specialization
    def get_salary_hour(self):
         return self.salary_hour
    def set_salary_hour(self, salary_hour):
        self.salary_per_hour = salary_hour
    def get_teaching_hours(self):
         return self.teaching_hours
    def set_teaching_hours(self, teaching_hours):
        self.number_of_teaching_hours = teaching_hours
    def total_salary(self):
        return self.salary_per_hour * self.number_of_teaching_hours
    def Personal_Information(self):
        return super(), f"{self.specialization} {self.salary_hour} {self.teaching_hours}"


# Create a class for students (child class, extend from universty personnel) contains:

    class Students(universty_personnel):
        def __init__(self, level, number_points, credit):
         self.level = level
         self.number_points = number_points
         self.credit = credit
    def get_level(self):
         return self.level
    def set_level(self, level):
        self.level = level
    def get_number_of_points(self):
         return self.number_points
    def set_number_of_points(self, number_points):
        self.number_points = number_points
    def get_credit(self):
         return self.credit
    def set_credit(self, credit):
        self.credit = credit
    def GPA(self):
         return self.number_points * self.credit


class Teaching_Assistant(Teacher,Students):


    pass

          Teacher = Teacher(1,"ghadeer",489,"GHAD@hotmail.com","Math", 19, 30)
          Students = Students(1,"sara",3883,"Reema@gh@hotmail.com",5, 4, 1)
        