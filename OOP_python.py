class University_Personnel():

    def __init__(self, id, name, university_id, email):
        self.id = id
        self.name = name
        self.university_id = university_id
        self.email = email

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getUniversity_id(self):
        return self.university_id

    def getEmail(self):
        return self.email

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def setUniversity_id(self, university_id):
        self.university_id = university_id

    def setEmail(self, email):
        self.email = email

    def personal_info(self):
        return f"ID:{self.id}, Name: {self.name}, University id: {self.university_id}, Email:{self.email}"


class Student(University_Personnel):

    def __init__(self, level, number_of_point, credit, id, name, university_id, email):
        super().__init__(id, name, university_id, email)
        self.level = level
        self.number_of_point = number_of_point
        self.credit = credit

    def personal_info(self):
        return f"ID:{self.id}, Name: {self.name}, University id: {self.university_id}, Email:{self.email}, Level: {self.level}, Number of point:{self.number_of_point}, Credit:{self.credit}"

    def calculate_gpa(self):
        return f"GPA = {self.number_of_point * self.credit}"

    def getLevel(self):
        return self.level

    def getNumber_of_point(self):
        return self.number_of_point

    def getCredit(self):
        return self.credit

    def setLevel(self, level):
        self.level = level

    def setNumber_of_point(self, number_of_point):
        self.level = number_of_point

    def setCredit(self, credit):
        self.credit = credit


class Teacher(University_Personnel):

    def __init__(self, specialization, salary_per_hour, number_of_teaching_hours, id, name, university_id, email):
        super().__init__(id, name, university_id, email)
        self.specialization = specialization
        self.salary_per_hour = salary_per_hour
        self.number_of_teaching_hours = number_of_teaching_hours

    def personal_info(self):
        return f"ID:{self.id}, Name: {self.name}, University id: {self.university_id}, Email:{self.email}, " \
               f"Specialization:{self.specialization}, Salary per hour:{self.salary_per_hour}, Number of teaching" \
               f" hours:{self.number_of_teaching_hours} "

    def calculate_salary(self):
        return f"Total salary:  {self.salary_per_hour * self.number_of_teaching_hours}"

    def getSpecialization(self):
        return self.specialization

    def getSalary_per_hour(self):
        return self.salary_per_hour

    def getNumber_of_teaching_hours(self):
        return self.number_of_teaching_hours

    def setSpecialization(self, specialization):
        self.specialization = specialization

    def setSalary_per_hour(self, salary_per_hour):
        self.salary_per_hour = salary_per_hour

    def setNumber_of_teaching_hours(self, number_of_teaching_hours):
        self.number_of_teaching_hours = number_of_teaching_hours


class Teacher_Assistant(Student, Teacher):
    def __init__(self, id, name, university_id, email,
                 level, number_of_point, credit,
                 specialization, salary_per_hour, number_of_teaching_hours):
        self.student = Student(level, number_of_point, credit, id, name, university_id, email)
        self.teacher = Teacher(specialization, salary_per_hour, number_of_teaching_hours, id, name, university_id,
                               email)


student = Student(19, 200, 10, 0, "omar", 0, "o@o.co")
teacher = Teacher("CS", 500, 2000, 4, "Khaled", 0, "k@k.co")
teacher_assistant = Teacher_Assistant(1, "Tameem", 0, "a@a.co", 10, 33, 44, "CS", 100, 20)
print("Teacher")
print(teacher.personal_info())
print(teacher.calculate_salary())
print("---------------------------------------------------------------------------")
print("Student")
print(student.personal_info())
print(student.calculate_gpa())

print("---------------------------------------------------------------------------")
print("Student Assistant")
print(teacher_assistant.student.personal_info())
print(teacher_assistant.student.calculate_gpa())

print("---------------------------------------------------------------------------")

print("Teacher Assistant")
print(teacher_assistant.teacher.personal_info())
print(teacher_assistant.teacher.calculate_salary())
