class Employee:
    month_working_day=22
    def __init__(self,id,name,basesalary) -> None:
        self.__id=id
        self.__name=name
        self.__basesalary=basesalary
    
  
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,id):
        self.__id=id
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name=name
    
    @property
    def basesalary(self):
        return self.__basesalary
    @basesalary.setter
    def basealary(self,salary):
        self.__basesalary=salary
    
    def showsalaryinfo(self):
        msg = "Employee {} ,this month's base salary is {}".format(self.name,self.basesalary) 
        return msg


class Worker(Employee):
    def __init__(self, id, name, salary) -> None:
        super().__init__(id, name, salary)
        self.__workinghours=8
        self.__salarybyhour=30
    
    # @property
    # def workinghours(self):
    #     return self.__workinghours
    # @workinghours.setter
    # def workinghours(self,hours):
    #     self.__workinghours=hours

    @property 
    def salarybyhour(self):
        return self.__salarybyhour
    @salarybyhour.setter
    def salarybyhour(self,salary):
        self.__salarybyhour=salary

    def computesalary(self):
        return self.basesalary+self.__salarybyhour*self.__workinghours * self.month_working_day
    

    def showsalaryinfo(self):
        baseinfor = super().showsalaryinfo()
        monthlysalary =" ,salary by hour is {}, working hours is {} , working days is {}, Total monthly salary is {}".format(self.salarybyhour,self.__workinghours,self.month_working_day,self.computesalary())
        full_infor=baseinfor+monthlysalary
        print(full_infor)

class Saleman(Employee):
    def __init__(self, id, name, basesalary) -> None:
        super().__init__(id, name, basesalary)
        self.__monthlysales=0
        self.__percent=0.03

    @property
    def monthlysale(self):
        return self.__monthlysales
    @monthlysale.setter
    def monthlysale(self,msale):
        self.__monthlysales=msale
    
    @property
    def percent(self):
        return self.__percent
    @percent.setter
    def percent(self,percent):
        self.__percent=percent

    def totalmonthlysalary(self):
        totalmonthlysalary=self.basealary+self.monthlysale*self.percent
        return totalmonthlysalary

    def showsalaryinfo(self):
        baseinfor = super().showsalaryinfo()
        monthlysalarymsg =" ,your monthy sales is {},percent is {}, Total monthly salary is {}".format(self.monthlysale,self.percent,self.totalmonthlysalary())
        full_infor=baseinfor+monthlysalarymsg
        print(full_infor)

class manager(Employee):
    pass

class salemanager(Employee):
    pass


# worker1=Worker(1,'Amy',1500)
# worker1.salarybyhour=20
# worker1.showsalaryinfo()

sale1=Saleman(2,"bobo",1000)
sale1.monthlysale=50000
sale1.showsalaryinfo()
