import re
import MySQLdb
from employee import Employee
from person import Person
from office import Office

ptrn = r'^[a-zA-z0-9]+@[a-z]+.[a-z]{2,4}$'

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





