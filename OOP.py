class UniverSity_Personal:
    def __init__(self, id, name, universityId, email):
        self.id = id
        self.name = name
        self.universityId = universityId
        self.email = email


@property
def Personal_Information(self):
    return f"{self.name} {self.universityId} {self.email}"


@property
def name(self):
    return f"{self.name}"


@name.setter
def set_name(self, name):
    self.name = name


@property
def id(self):
    return f"{self.id}"


@id.setter
def set_id(self, id):
    self.id = id


@property
def universityId(self):
    return f"{self.universityId}"


@universityId.setter
def set_universityId(self, universityId):
    self.universityId = universityId


@property
def email(self):
    return f"{self.universityId}"


@email.setter
def set_email(self, email):
    self.email = email


# Student class
class Student(UniverSity_Personal):
    def __init__(self, id, name, universityId, email, level, number_of_points, credit):
        super().__init__(id, name, universityId, email)
        self.level = level
        self.number_of_points = number_of_points
        self.credit = credit


@property
def level(self):
    return f"{self.level}"


@email.setter
def set_level(self, level):
    self.level = level


@property
def number_of_points(self):
    return f"{self.number_of_points}"


@number_of_points.setter
def set_number_of_points(self, number_of_points):
    self.number_of_points = number_of_points


@property
def credit(self):
    return f"{self.credit}"


@credit.setter
def set_credit(self, credit):
    self.credit = credit


@credit.getter
def get_credit(self):
    return self.credit


@staticmethod
def calculating_GAP():
    return number_of_points * credit


@staticmethod
def Personal_Information(self):
    super.Personal_Information
    return f"{self.level} {self.number_of_points} {self.credit}"


# Teacher class
class Teacher(UniverSity_Personal):
    def __init__(self, id, name, universityId, email, specialization, salary_per_hour, number_of_teaching_hours):
        super().__init__(id, name, universityId, email)
        self.specialization = specialization
        self.salary_per_hour = salary_per_hour
        self.number_of_teaching_hours = number_of_teaching_hours


@property
def specialization(self):
    return f"{self.specialization}"


@specialization.setter
def set_specialization(self, specialization):
    self.specialization = specialization


@specialization.getter
def get_specialization(self, specialization):
    return specialization


@property
def salary_per_hour(self):
    return f"{self.salary_per_hour}"


@salary_per_hour.setter
def set_salary_per_hour(self, salary_per_hour):
    self.salary_per_hour = salary_per_hour


@salary_per_hour.getter
def get_salary_per_hour(self):
    return self.salary_per_hour


@property
def number_of_teaching_hours(self):
    return f"{self.salary_per_hour}"


@number_of_teaching_hours.setter
def set_number_of_teaching_hours(self, number_of_teaching_hours):
    self.number_of_teaching_hours = number_of_teaching_hours


@number_of_teaching_hours.getter
def get_number_of_teaching_hours(self):
    return self.number_of_teaching_hours


@staticmethod
def total_salary():
    return salary_per_hour*number_of_teaching_hours


@staticmethod
def Personal_Information(self):
    super.Personal_Information
    return f"{self.specialization} {self.salary_per_hour} {self.number_of_teaching_hours}"


class Teaching_Assistant(Teacher, Student):
    pass

    class Teacher(UniverSity_Personal):
        def __init__(self, id, name, universityId, email, specialization, salary_per_hour, number_of_teaching_hours, level, number_of_points, credit):
            super().__init__(id, name, universityId, email, specialization,
                             salary_per_hour, number_of_teaching_hours)
     

student_one = Student(1, "Maha", 301, "maha@gmail.com", 3, 100, 5)

teacher_one = Teacher(101, "Sarah", 30321, "Sarah@gmail.com", "IT", 500, 120)

student_one.set_name = "hala"
student_one.set_level = "5"
student_one.set_email = "hala@gmail.com"
print(student_one.name)
print(student_one.credit)
print(student_one.email)
print(student_one.level)

teacher_one.set_salary_per_hour = 1000
print(teacher_one.salary_per_hour)
print(teacher_one.email)

print(teacher_one.total_salary)
