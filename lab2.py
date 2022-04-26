import re
import MySQLdb
db = MySQLdb.connect("localhost","root","12345","pythonschema")
cursor = db.cursor()

ptrn = r'^[a-zA-z0-9]+@[a-z]+.[a-z]{2,4}$'

class Person:
    def __init__(self , fullName , money , sleepmood,healthRate):
        self.fullName = fullName
        self.money = money
        self.sleepmood = sleepmood
        if healthRate <= 0:
            self.healthRate = 0 
        elif healthRate >=100:
            self.healthRate = 100
        else:
            self.healthRate = healthRate 
 

    def sleep(self,hours ):
        if hours == 7:
            print("happy")
        elif hours < 7:
            print ("tired")
        else:
            print("lazy")

    def eat(self,meals ):
        if meals == 3 :
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        elif meals == 1:
            self.healthRate = 50
        else:
            print("please enter 1, 2, or 3")

    def buy(self,items ):
        self.money -= (items*10)




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


class Office:
    def __init__(self , name  ):
       self.name = name
      
    def get_all_employees(self):
        stmnt= "select * from employee"
        try:
            cursor.execute(stmnt)
            rows = cursor.fetchall()
            print("--------------------------------------------------")
            for row in rows:
                print (row)
            print("--------------------------------------------------")
        except:
            print ("something went wrong")

    def get_employee(self, empID ):
        stmnt = f'select * from employee where id = "{empID}"'
        try:
            cursor.execute(stmnt)
            row = cursor.fetchone()
            print("--------------------------------------------------")
            print (row)
            print("--------------------------------------------------")
        except:
            print("not executed")
            db.rollback()
    def fire(self,empID ):
        stmnt = f'delete from employee where id = "{empID}"'
        try:
            cursor.execute(stmnt)
            db.commit()
        except:
            print("not executed")
            db.rollback()
    def hire(self, emp):
        stmnt = f'insert into employee values ("{emp.id}" , "{emp.email}" , "{emp.workmood}" ,"{ emp.salary}" , "{emp.is_manager}")'
        try:
            cursor.execute(stmnt)
            db.commit()
        except:
            print("not executed")
            db.rollback()
        
    


office = Office("OSD")
print ('1) Show\n2) Select\n3) Hire\n4) Fire\n5) Exit')
choice = int(input("enter your choice: "))
while choice!= 5:
    if choice == 1:
        office.get_all_employees()
    elif choice == 2:
        empid= int (input("enter id to search for: "))
        office.get_employee(empid)
    elif choice == 3:
        x = input("do you want to add new employee: [y/n] ")
        while x != "n":
            user = input("if manager press t \nif normal employee press f : ")
            print("Enter your data: ")
            id =int (input("ID: "))
            email = input("Email: ")
            work_hours =int (input("Work Hours: "))
            salary =int(input("Salary: "))
            emp = Employee(id,email,work_hours , salary , user)
            office.hire(emp)
            x = input("do you want to add new employee: [y/n] ")
    elif choice==4:
        empid= int (input("enter id to delete: "))
        office.fire(empid)
    print ('1) Show\n2) Select\n3) Hire\n4) Fire\n5) Exit')
    choice = int(input("enter your choice: "))





