# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 12:16:49 2026

@author: merug
"""

class student:
    Name="sai"
    Rollno=23
    subject1=78
    subject2=59
    subject3=65
    total = subject1+subject2+subject3   
    avg = total/3 
    def grade(self):
        if(self.avg>90):
            print("grade A")
        elif(75>=self.avg<=89):
            print("grade B")
        elif(60>=self.avg<=74):
            print("grade C")
        elif(40>=self.avg<=59):
             print("grade D")
        else:
            print("FAIL")
s=student()
print("total marks :",s.total)
print("average :",s.avg)
s.grade()