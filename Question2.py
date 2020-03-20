class College:       # outer class
    
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.Absent =self.Absent()          # accessing the inner class
        self.Present = self.Present()        # accessing the inner class
    
    def AbsentStudents(self):
        print("NAME: " + self.name +",","Roll no.:" + self.rollno + "," + "Status: " ,end="")
        self.Absent.show()
    
    def PresentStudents(self):
        print("NAME: " + self.name +",","Roll no.:" + self.rollno + "," + "Status: " ,end="")
        self.Present.show()
        
    
    
    #inner class
    
    class Absent:
        def __init__(self):
            self.Absent = "Absent"
        def show(self):
            print(self.Absent)
            
 
       #inner class     
    class Present:
        def __init__(self):
            self.present = "Present"
        def show(self):
            print(self.present)

s1 = College("John","22") 
s2 = College("Kiran","23")
s3 = College("Robert","24")
s4 = College("Emma","25")

print("TODAY ABSENT STUDENTS")
s1.AbsentStudents()
s3.AbsentStudents()

print()

print("TODAY PRESENT STUDENTS")
s2.PresentStudents()
s4.PresentStudents()


