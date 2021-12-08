#-----------------------class universty_personnel---------------------

class universty_personnel:

    def __init__(self, id, name, university_id, university_email):
        self.id = id
        self.name = name
        self.university_id = university_id
        self.university_email = university_email

    def get_id(self):
        return self.id
    def set_id(self, data):
        self.id = data

    def get_name(self):
        return self.name
    def set_name(self, data):
        self.name = data

    def get_university_id(self):
        return self.university_id
    def set_university_id(self, data):
        self.university_id = data

    def get_university_email(self):
        return self.university_email
    def set_university_email(self, data):
        self.university_email = data
    
    def Personal_Information(self):
        return f"{self.id} {self.name} {self.university_id} {self.university_email}"


universty_personnel_one = universty_personnel(437, "Abdullah", 20, "imam@edu.sa")
print(universty_personnel_one.Personal_Information())



#--------------------class teacher-----------------------------

class teacher(universty_personnel):

    
    def __init__(self, id, name, university_id, university_email, specialization, salary_per_hour, number_of_teaching_hours):
        super(). __init__(id, name, university_id, university_email)
        self.specialization = specialization
        self.salary_per_hour = salary_per_hour
        self.number_of_teaching_hours = number_of_teaching_hours

    def get_specialization(self):
        return self.specialization
    def set_specialization(self, data):
        self.specialization = data

    def get_salary_per_hour(self):
        return self.salary_per_hour
    def set_salary_per_hour(self, data):
        self.salary_per_hour = data

    def get_number_of_teaching_hours(self):
        return self.number_of_teaching_hours
    def set_number_of_teaching_hours(self, data):
        self.number_of_teaching_hours= data

    def total_salary(self):
        return self.salary_per_hour * self.number_of_teaching_hours

    def Personal_Information(self):
        return f"{self.id} {self.name} {self.university_id} {self.university_email} {self.specialization} {self.salary_per_hour} {self.number_of_teaching_hours} "


teacher_one = teacher(455, "Abdullah", 20, "imam@edu.sa","math", 100, 80)
print(teacher_one.total_salary())
print(teacher_one.Personal_Information())




#-------------------------class students---------------------------

class students(universty_personnel):

    def __init__(self, id, name, university_id, university_email, level, number_of_points, credit):
        super(). __init__(id, name, university_id, university_email)
        self.level = level
        self.number_of_points = number_of_points
        self.credit = credit

    def get_level(self):
        return self.level
    def set_level(self, data):
        self.level = data

    def get_number_of_points(self):
        return self.number_of_points
    def set_number_of_points(self, data):
        self.number_of_points = data

    def get_credit(self):
        return self.credit
    def set_credit(self, data):
        self.credit = data
    
    def calculating(self):
        return self.number_of_points * self.credit

    def Personal_Information(self):
        return f"{self.id} {self.name} {self.university_id} {self.university_email} {self.level} {self.number_of_points} {self.credit} "


student_one = students(455, "Abdullah", 20, "imam@edu.sa", 3, 9, 10)
print(student_one.Personal_Information())


#------------------------class Teaching_Assistant

class Teaching_Assistant(students , teacher):
    pass
