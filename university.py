class University:

    # constructor
    def __init__(self, id, name, university_id, email):
        self.id = id
        self.name = name
        self.university_id = university_id
        self.email = email

    # setter & getter for id
    def get_id(self):
        return self.id
      
    def set_id(self, id):
        self.id = id
    # setter & getter for name
    def get_name(self):
        return self.name
      
    def set_name(self, name):
        self.name = name

    # setter & getter for university_id
    def get_university_id(self):
        return self.university_id
      
    def set_university_id(self, university_id):
        self.university_id = university_id

    # setter & getter for email
    def get_email(self):
        return self.email
      
    def set_email(self, email):
        self.email = email


    def personal_information(self):
        return f"id: {self.id}\nName: {self.name}\nUniversity id: {self.university_id}\nEmail: {self.email}"

# ---------class Teacher---------- #
class Teacher(University):

    # constructor
    def __init__(self, id, name, university_id, email, specialization, salary_per_hour, number_of_teaching_hours):
        super().__init__(id, name, university_id, email)
        self.specialization = specialization
        self.salary_per_hour = salary_per_hour
        self.number_of_teaching_hours = number_of_teaching_hours

    # setter & getter for specialization
    def get_specialization(self):
        return self.specialization
      
    def set_specialization(self, specialization):
        self.specialization = specialization

        # setter & getter for salary_per_hour
    def get_salary_per_hour(self):
        return self.salary_per_hour
      
    def set_salary_per_hour(self, salary_per_hour):
        self.salary_per_hour = salary_per_hour

        # setter & getter for number_of_teaching_hours
    def get_number_of_teaching_hours(self):
        return self.number_of_teaching_hours
      
    def set_number_of_teaching_hours(self, number_of_teaching_hours):
        self.number_of_teaching_hours = number_of_teaching_hours

    def total_salary(self):
        total_salary = self.salary_per_hour * self.number_of_teaching_hours
        return f"Total Salary = {total_salary}"

    def personal_information(self):
        return f"id: {self.id}\nName: {self.name}\nUniversity id: {self.university_id}\nEmail: {self.email}\nSpecialixation: {self.specialization}\nSalary per hour: {self.salary_per_hour}\nNumber of teaching hours: {self.number_of_teaching_hours}"

# ---------class Student---------- #
class Student(University):

    # constructor
    def __init__(self, id, name, university_id, email, level, number_of_points, credit):
        super().__init__(id, name, university_id, email)
        self.level = level
        self.number_of_points = number_of_points
        self.credit = credit

    # setter & getter for level
    def get_level(self):
        return self.level
      
    def set_level(self, level):
        self.level = level

        # setter & getter for number_of_points
    def get_number_of_points(self):
        return self.number_of_points
      
    def set_number_of_points(self, number_of_points):
        self.number_of_points = number_of_points

        # setter & getter for credit
    def get_credit(self):
        return self.credit
      
    def set_credit(self, credit):
        self.credit = credit

    def calculate_gpa(self):
        gpa = self.number_of_points * self.credit
        return f"Student GPA: {gpa}"

    def personal_information(self):
        return f"id: {self.id}\nName: {self.name}\nUniversity id: {self.university_id}\nEmail: {self.email}\nLevel: {self.level}\nNumber of points: {self.number_of_points}\nCredit: {self.credit}"


class Teaching_Assistant(Student, Teacher):
    def __init__(self, student, teacher):

        self.student = student
        self.teacher = teacher

# Testing Teacher methods
teacher = Teacher(1,"Faisal", 3, "f.f.edu.sa","English",100,24)
print("\n-----Teacher-----")
print(teacher.personal_information())
print(teacher.total_salary())

# Testing Student methods
student = Student(5,"Ahmed", 2, "a@a.edu.sa", 6, 40, 79)
print("\n-----Student-----")
print(student.personal_information())
print(student.calculate_gpa())

# Testing Teaching_Assistant 
teaching_assistant = Teaching_Assistant(student, teacher)
print("\n-----Teaching Assistant-----")
print(teaching_assistant.teacher.personal_information())
print(teaching_assistant.student.personal_information())
