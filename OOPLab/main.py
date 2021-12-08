class University:
    def __init__(self, id, name, university_id, university_email):
        self.id = id
        self.name = name
        self.university_id = university_id
        self.university_email = university_email

    def Personal_Information(self):
        data = {
            "ID: " + self.id,
            "Name: " + self.name,
            "University ID: " + self.university_id,
            "University Email: " + self.university_email
        }
        return data


    def set_id(self,id):
        self.id = id
    def get_id(self):
        return self.id


    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name


    def set_university_id(self, university_id):
        self.university_id = university_id
    def get_university_id(self):
        return self.university_id


    def set_university_email(self, university_email):
        self.university_email =  university_email
    def get_university_email(self):
        return self.university_email

class Teacher(University):
    def __init__(self,id, name, university_id, university_email, specialization, salary_per_hour, number_of_teaching_hour):
        super().__init__(id, name, university_id, university_email)
        self.specialization = specialization
        self.salary_per_hour = salary_per_hour
        self.number_of_teaching_hour = number_of_teaching_hour

    def set_specialization(self, specialization):
        self.specialization = specialization
    def get_specialization(self):
        return self.specialization


    def set_salary_per_hour(self, salary_per_hour):
        self.salary_per_hour = salary_per_hour
    def get_salary_per_hour(self):
        return self.salary_per_hour


    def set_number_of_teaching_hour(self,number_of_teaching_hour):
        self.number_of_teaching_hour = number_of_teaching_hour
    def get_number_of_teaching_hour(self):
        self.number_of_teaching_hour


    def total_salary(self):
        return self.salary_per_hour * self.number_of_teaching_hour

    def Personal_Information(self):
        data = {
            "ID: " + self.id,
            "Name: " + self.name,
            "University ID: " + self.university_id,
            "University Email: " + self.university_email,
            "Teacher Specialization: " + self.specialization,
            "Total Salary: " + str(self.total_salary()),
        }
        return data


class Students(University):
    def __init__(self,id, name, university_id, university_email, level, number_of_points, credit):
        super().__init__(id, name, university_id, university_email)
        self.level = level
        self.number_of_points = number_of_points
        self.credit = credit

    def Personal_Information(self):
        data = {
            "ID: " + self.id,
            "Name: " + self.name,
            "University ID: " + self.university_id,
            "University Email: " + self.university_email,
            "Your GPA is: " + str(self.gpa())
        }
        return data

    def set_level(self,level):
        self.level = level
    def get_level(self):
        return self.level


    def set_number_of_points(self,number_of_points):
        self.number_of_points = number_of_points
    def get_number_of_points(self):
        return self.number_of_points


    def set_credit(self, credit):
        self.credit = credit
    def get_credit(self):
        return self.credit


    def gpa(self):
        return self.number_of_points * self.credit


class Teaching_Assistant(Teacher,Students):
    def __init__(self,id, name, university_id, university_email,Students, Teacher):
        super().__init__(id, name, university_id, university_email,Students,Teacher)
        # super().__init__(id, name, university_id, university_email, level, number_of_points, credit)
    def Personal_Information(self):
        data = {
            "ID: " + super().id,
            "Name: " + super().name,
            "University ID: " + super().university_id,
            "University Email: " + super().university_email,
            "Your GPA is: " + str(super().gpa())
        }

print("\n--------------------Class University----------------------")
uni = University("1", "Riyadh", "1d", "u@gmail.com")
print(uni.get_id())
print(uni.get_name())
print(uni.get_university_id())
print(uni.get_university_email())
print(uni.Personal_Information())

print("\n--------------------Class Teacher----------------------")
teacher_one = Teacher("3", "Abha", "3d", "abha@gmail.com","Tech",90,8)
print(teacher_one.get_id())
print(teacher_one.get_name())
print(teacher_one.get_university_id())
print(teacher_one.get_university_email())
print(teacher_one.get_specialization())
print(teacher_one.get_number_of_teaching_hour())
print(teacher_one.get_salary_per_hour())
print(teacher_one.Personal_Information())

print("\n--------------------Class Students----------------------")
student_one = Students("3", "Abha", "3d", "abha@gmail.com","Four",90,3)
print(student_one.get_id())
print(student_one.get_name())
print(student_one.get_university_id())
print(student_one.get_university_email())
print(student_one.get_level())
print(student_one.get_number_of_points())
print(student_one.get_credit())
print(student_one.Personal_Information())

# teacher_assistant_teacher = Teacher("PHY",80,8)
# teacher_assistant_student = Students("Fifth",80,2)
# teacher_assistant = Teaching_Assistant("2","Jeddah","2T","Jeddah@gmail.com",teacher_assistant_teacher,teacher_assistant_student)
# print(teacher_assistant.Personal_Information())