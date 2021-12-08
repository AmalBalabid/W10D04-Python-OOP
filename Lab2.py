class University:
    def __init__(self, id, name, universityId, email):
        self.id = id
        self.name = name
        self.universityId = universityId
        self.email = email

    def Personal_Information(self):
        print("Id: ",self.id," Name: ",self.name," University ID: ",self.universityId," Email: ",self.email)

#setter & getter for id
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

#setter & getter for name
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

#setter & getter for universityId
    def get_universityId(self):
        return self.universityId

    def set_universityId(self, universityId):
        self.universityId = universityId

#setter & getter for email
    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email


#Teacher Class
class Teacher(University):

    def __init__(self, id, name, universityId, email, specialization, salary, teachHours):

        super().__init__(id, name, universityId, email)
        self.specialization = specialization
        self.salary = salary
        self.teachHours = teachHours

#setter & getter for specialization
    def get_specialization(self):
        return self.specialization

    def set_specialization(self, specialization):
        self.specialization = specialization

#setter & getter for salary
    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary

#setter & getter for teachHours
    def get_teachHours(self):
        return self.teachHours

    def set_teachHours(self, teachHours):
        self.teachHours = teachHours

    def total_salary(self):
       return self.salary*self.teachHours
      
    
    def Personal_Information(self):
        print("ID: ",self.id," - Name: ",self.name," - University ID: ",self.universityId," - Email: ", self.email," - Specialization: ", self.specialization," - Salary: ",self.total_salary())



#Student Class
class Student(University):

    def __init__(self, id, name, universityId, email, level, numOfPoints, credit):

        super().__init__(id, name, universityId, email)
        self.level = level
        self.numOfPoints = numOfPoints
        self.credit = credit

    def calcGpa(self):
        return self.numOfPoints*self.credit

    def Personal_Information(self):
        print("ID: ",self.id," - Name: ",self.name," - University ID: ",self.universityId," - Email: ",self.email," - Level: ",self.level," - GPA: ",self.calcGpa())

#setter & getter for level
    def get_level(self):
        return self.level

    def set_level(self, level):
        self.level = level

#setter & getter for numOfPoints
    def get_numOfPoints(self):
        return self.numOfPoints

    def set_numOfPoints(self, numOfPoints):
        self.numOfPoints = numOfPoints

#setter & getter for credit
    def get_credit(self):
        return self.credit

    def set_credit(self, credit):
        self.credit = credit

#TachAssistant Class
class TeachAssistant(Teacher, Student):

    def __init__():
       super().__init__()

teacher = Teacher(1, "Afnan", 3, "Afnan@hotmail.com", "Programming", 25000, 7)
teacher.Personal_Information()

student = Student(2, "Aljohara", 3, "aljohara@hotmail.com", 4, 90, 1)
student.Personal_Information()

