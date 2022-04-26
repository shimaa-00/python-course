import imp
import re
from person import  Person
ptrn = r'^[a-zA-z0-9]+@[a-z]+.[a-z]{2,4}$'
class Employee(Person):
    def __init__(self , id, email, workhours, salary, is_manager):
        self.id = id 
        result = re.match(ptrn,email)
        if result:
            self.email = email
        else:
            while result==None:
                print("invalid email") 
                email = input("Enter valid Email : ")
                result = re.match(ptrn,email)
            self.email = email
        self.workmood = self.work(workhours)
        self.salary = 1000 if salary < 1000 else salary
        self.is_manager ="true" if is_manager == "t" else "false"
    def work(self,hours ):
        if hours == 8:
            return "happy"
        elif hours > 8:
            return "tired"
        else:
            return "lazy"
    def sendEmail(to, subject, body, reciver):
        ptrn = r'^[a-zA-z0-9]+@[a-z]+\.[a-z]{2,4}$'
        result = re.match(ptrn, to)
        if result:
            MyEmail = open("Email.txt", "a")
            MyEmail.write("to: " + to + "\n")
            MyEmail.write("Subject: " + subject + "\n")
            MyEmail.write("Body: " + body + "\n")
            MyEmail.write("Reciver: " + reciver + "\n")
            MyEmail.write("================================= " + "\n")
            MyEmail.close()
        else:
            raiseExceptions("Sorry invalid email")