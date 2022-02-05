class Student:
    def __init__(self,name,age,math_score,literature_score):
        self.name=name
        self.age=age
        self.math_score=math_score
        self.literature_score=literature_score
    def toString(self):
        return "Name: "+self.name+"\nAge: "+str(self.age)+"\nmath_score: "+str(self.math_score)+"\nliterature_score: "+str(self.literature_score)
    
students=[]
s1=Student("T-naul",20,8,6)
s2=Student("T-naul",21,7,7)
s3=Student("T-naul",16,6,8)
students.append(s1)
students.append(s2)
students.append(s3)

for i in range(len(students)):
    print(students[i].toString())
