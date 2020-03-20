
class StudentNames():
    
    def __init__(self,name1,name2,name3,name4,name5,name6):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
        self.name4 = name4
        self.name5 = name5
        self.name6 = name6
    
    def names(self):
        NameList = [self.name1,self.name2,self.name3,self.name4,self.name5,self.name6]
        firstnames = [name.split(' ')[0] for name in NameList]
        print(firstnames)

        countnames = {}
        for name in firstnames:
            name = name.lower() 
            if name in countnames:
                countnames[name] += 1
            else:
                countnames[name] = 1

        print(countnames)

Student = StudentNames("Emma wild","Emma wilson","Elijah mason","Emma watson","Elijah wilson","Emma hemsworth")

Student.names()
