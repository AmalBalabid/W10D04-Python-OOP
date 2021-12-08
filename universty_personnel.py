# --------------- universty_personnel class ------------------
class universty_personnel:
    def __init__ (self ,id,name,university_id,university_email):
        self.id = id
        self.name = name
        self.university_id = university_id
        self.university_email = university_email
    
    def Personal_Information(self):
        return f"{self.id} - {self.name} - {self.university_id} - {self.university_email}"
    
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

u_p = universty_personnel(437,"Saad",437000000,"salwu@###.edu.sa")
u_p.set_university_email("test@gmail.com")
print(u_p.Personal_Information())