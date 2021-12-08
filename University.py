




class University:
    def __init__(self,id,name,universitynumber,email):
        self.id=id
        self.name = name
        self.universitynumber=universitynumber
        self.email=email
       

    def print_info(self):
        print('Id:', self.id)
        print('Name:', self.name)
        print('UniversityId:', self.universitynumber)
        print('Email',self.email)

def get_id(self):
      return self._id


def set_id(self, id):
  self._id = id

def get_name(self):
      return self._name

def set_name(self, name):
  self._name = name

def get_universitynumber(self):
      return self._universitynumber

def set_universitynumber(self, number):
  self._universitynumber = number

def get_email(self):
      return self._name

def set_email(self, email):
  self._email = email



university_one=University(1,"king khaled",1,"tii@hotmail.com")

university_one.print_info()


#class Teacher ------------------------------------------------------------------

class Teacher(University): 
    def __init__(self,id,name,universitynumber,email,salariPerhour,specialization,numberofteachinghours):
        super().__init__(id,name,universitynumber,email)
        self.salariPerhour = salariPerhour
        self.specialization =specialization
        self.numberofteachinghours = numberofteachinghours
    def get_salariPerhour(self):
        return self._salariPerhour

    def set_salariPerhour(self, salari):
        self._salariPerhour = salari

    def get_specialization(self):
      return self._specialization

    def set_specialization(self, s):
        self._specialization = s

    def get_numberofteachinghours(self):
      return self._numberofteachinghours



    def set_numberofteachinghours(self, a):
     self._numberofteachinghours = a

    def calculate_salary(self):
        result=self.salariPerhour * self.numberofteachinghours
        return result
    
    def print_info(self):
        print('Id:', self.id)
        print('Name:', self.name)
        print('UniversityId:', self.universitynumber)
        print('Email',self.email)
        print("total sallary",self.calculate_salary())
   
teacher_ahmed=Teacher(2,"Abdulaziz",1,"A@gmail.com",80,"Math",20)
teacher_ahmed.print_info()
teacher_ahmed.calculate_salary()

#class Student ------------------------------------------------------------------
class Student(University): 

   def __init__(self,id,name,universitynumber,email,level,numberofpoints,credit):
        super().__init__(id,name,universitynumber,email)
        self.level = level
        self.numberofpoints =numberofpoints
        self.credit = credit
   def get_level(self):
      return self._level



   def set_level(self, level):
      self._level =level

   def get_numberofpoints(self):
      return self._numberofpoints

   def set_numberofpoints(self, n):
      self._numberofpoints =n

   def get_credit(self):
    return self._credit

   def set_credit(self, credit):
      return self._credit
    
   def GPA(self) :
         result=self.numberofpoints * self.credit
         return result 


   def print_info(self):
        print('Id:', self.id)
        print('Name:', self.name)
        print('UniversityId:', self.universitynumber)
        print('Email',self.email)
        print("GPA",self.GPA())

student_noura=Student(3,"prince sattam",3,"nn@gmail.com",3,250,3.5)
student_noura.print_info()
student_noura.GPA()

#Teaching Assistant class (child class inheriting the Student and Teacher classes)
class TeachingAssistant(Teacher,Student):
      def __init__():

           super().__init__
          
          

# TeachingAssi=TeachingAssistant(TeachingAssi,)
