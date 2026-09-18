class student:
    name = input("Name : ")
    rollno = int(input("Rollno : "))
    marks = int(input("Marks : "))
    def get(self):
        print(self.name)
        print(self.rollno)
        print(self.marks)
s=student()
print(s.get())
        
    
    