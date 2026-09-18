class Employee:
    employeeid = 2576
    name = "sai"
    basicsalary=20000
    def total_salary(self):
        HRA = 0.2*self.basicsalary
        DA = 0.1*self.basicsalary
        totalsalary = HRA+DA+self.basicsalary
        print("Total salary is",totalsalary)
e = Employee()
print("employeeid = ",e.employeeid)
print("name =",e.name)
print("basicsalary =",e.basicsalary)
e.total_salary()
        
    
