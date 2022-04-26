import MySQLdb
db = MySQLdb.connect("localhost","root","12345","pythonschema")
cursor = db.cursor()
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
        
    

