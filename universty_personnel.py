class universty_personnel:
    def __init__ (self ,id,name,university_id,university_email):
        self.id = id
        self.name = name
        self.university_id = university_id
        self.university_email = university_email
    
    def Personal_Information(self):
        return f"{self.id} - {self.name} - {self.university_id} - {self.university_email}"

u_p = universty_personnel(437,"Saad",437015722,"salwuhayb@imamu.edu.sa")
print(u_p.Personal_Information())
