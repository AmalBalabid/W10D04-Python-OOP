class Person:
  def __init__(self, id, name,uId,email):
    self.id = id
    self.name = name
    self.uId = uId
    self.email = email

  def Personal_Information(self):
    print("id: ",self.id," name: " , self.name," university id: ",self.uId," email: ",self.email)

  def get_id(self):        
        return self.id
  def set_id(self, id):           
        self.id = id

  def get_name(self):        
        return self.name
  def set_name(self, name):           
        self.name = name

  def get_uId(self):        
        return self.uId
  def set_uId(self, uId):           
        self.uId = uId

  def get_email(self):        
        return self.email
  def set_email(self, email):           
        self.email = email


class Teacher(Person):
  def __init__(self, id, name,uId,email,specialization, salaryPerHour,teachingHours):
    super().__init__(id, name,uId,email)
    self.specialization = specialization
    self.salaryPerHour = salaryPerHour
    self.teachingHours = teachingHours

  def total_salary(self):
    return self.salaryPerHour*self.teachingHours

  def Personal_Information(self):
    print("id: ",self.id," name: " , self.name," university id: ",self.uId," email: ",self.email," specialization: ",self.specialization," salary: ",self.total_salary())

  def get_specialization(self):        
        return self.specialization
  def set_specialization(self, specialization):           
        self.specialization = specialization

  def get_salaryPerHour(self):        
        return self.salaryPerHour
  def set_salaryPerHour(self, salaryPerHour):           
        self.salaryPerHour = salaryPerHour

  def get_teachingHours(self):        
        return self.teachingHours
  def set_teachingHours(self, teachingHours):           
        self.teachingHours = teachingHours


class Students(Person):
  def __init__(self, id, name,uId,email,level, points,credit):
    super().__init__(id, name,uId,email)
    self.level = level
    self.points = points
    self.credit = credit

  def GPA(self):
    return self.points * self.credit

  def Personal_Information(self):
    print("id: ",self.id," name: " , self.name," university id: ",self.uId," email: ",self.email," level: ",self.level," GPA: ",self.GPA())

  def level(self):        
        return self.level
  def set_level(self, level):           
        self.level = level

  def get_points(self):        
        return self.points
  def set_points(self, points):           
        self.points = points

  def get_credit(self):        
        return self.credit
  def set_credit(self, credit):           
        self.credit = credit


class TeachingAssistant(Teacher,Students):
  def __init__():
    super().__init__()



person = Person(6, "Olsen",87,"s@a.c")
person.Personal_Information()

teacher = Teacher(6, "Olsen",87,"s@a.c","math",2,6)
teacher.Personal_Information()
print(teacher.get_id())

students = Students(6, "Olsen",87,"s@a.c",1,5,2)
students.Personal_Information()

# teaching_assistant = TeachingAssistant()