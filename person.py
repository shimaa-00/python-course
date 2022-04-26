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





