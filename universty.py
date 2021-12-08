class Universty:
    
    def __init__(self, id , name , universtyid ,universtyEmail):
        self . id =id
        self . name = name 
        self . universtyid = universtyid 
        self . universtyEmail = universtyEmail
       
    def Personal_Information_method(self):
           return f"{self.id} {self.name} {self.universtyid} {self.universtyEmail}"

          # getter method
    def get_id(self):
        return self._id
      
    # setter method
    def set_id(self,id ):
        self._id= id
  
          # getter method
    def get_name(self):
        return self._id
      
    # setter method
    def set_name(self,name ):
        self._name= name

      # getter method
    def get_universtyid(self):
        return self._id
      
    # setter method
    def set_universtyEmail(self,universtyEmail ):
        self.universtyEmail= universtyEmail

# _________________________________________

class Teacher(Universty):

    def __init__(self,specialization,salary , numberofteaching):

        self.specialization=specialization
        self.salary=salary
        self.numberofteaching=numberofteaching  
        
    def Personal_Information_method(self):
           print(self.specialization ,self.salary,self.numberofteaching)

          # getter method
    def get_specializationid(self):
        return self._specialization
      
    # setter method
    def set_specialization(self,specialization ):
        self._specialization=specialization

        
          # getter method
    def get_salary(self):
        return self._salary
      
    # setter method
    def set_salary(self,salary ):
        self._salary= salary

        
          # getter method
    def get_numberofteaching(self):
        return self._numberofteaching
      
    # setter method
    def set_numberofteaching(self,numberofteaching):
        self._numberofteaching= numberofteaching

def total_salary_method(self):
           total= self.salary * self.numberofteaching 
           print(total)

         

# ___________________________________________________

class Students (Universty):

   def __init__(self,level,numberofpoints,credit):
        self.level =level
        self.numberofpoints =numberofpoints 
        self.credit =credit
 
   def Personal_Information_method(self):
           return f"{self.level} {self.numberofpoints} {self.credit} "

   def GPA(self): 
         GPA= self.numberofpoints * self.credit
         print(GPA)

          # getter method
   def get_level(self):
        return self._level
      
    # setter method
   def set_level(self,level ):
        self._level=level

          # getter method
   def get_numberofpoints(self):
        return self._numberofpoints
      
    # setter method
   def set_numberofpoints(self,numberofpoints ):
        self._numberofpoints=numberofpoints

   # getter method
   def get_credit(self):
        return self._credit
      
    # setter method
   def set_credit(self,credit ):
        self._credit=credit
# ________________________________________________________

class TeachingAssistant(Teacher,Students):

 def __init__():
     super().__init__()

teacher = Teacher("math",500,3)
teacher.Personal_Information_method()

students = Students(2,3,1)
students.Personal_Information_method()

