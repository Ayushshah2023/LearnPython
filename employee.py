'''
#create a class called company D
#object is an employee D
#employee-employee id D, name, designation,salary,statue-{active(default),terminated,suspended}
#annual hike is 10% of the og sslaryD
#hike ratio is a class attribute  D
#fina a way to assign valuesD
#at least 5 objectsD
#function compute hike (self)D
#hike in rupees for that annual yearD
#change status(self,new status)D
#count of all the active employee in class D
#active to others and others to active should affect itD
'''
class company:
    annual_hike=0.1
    def assign_id(self,id):
        self.id=id
    def assign_name(self,name):
        self.name=name
    def assign_des(self,des):
        self.designation=des
    def assign_salary(self,salary):
        self.salary=salary
    def assign_status(self,status="active"):
        self.status=status
    def hike(self,years):
        self.salary=self.salary+(years*0.1*self.salary)
        print(self.salary)
    def status_reassign(self,status="active"):
        self.status=status
        if self.status=='active':
            active_count=active_count+1
count=0
ct=0
e1=company()
e2=company()
e3=company()
e4=company()
e5=company()
a=int(input("Enter the number of employees needed"))
active_count=0
#for i in range(1,a):
   # e[i=company()
ct=ct+1
e1.assign_id(input("Enter the employee id " + str(count)))
e1.assign_name(input("Enter the employee name " + str(count)))
e1.assign_des(input("Enter the employee designations " + str(count)))
e1.assign_salary(input("Enter the employee salary " + str(count)))
e1.assign_status(input("Enter the employee status " + str(count)))
e1.hike(input("Enter the number of years of work"))
q1=input("Enter y for yes to change the status of the employee else enter n for no")
if q1=='y':
    e1.status_reassign(input("Enter the new employee status ")
#if e1.status=="Active" :
    #active_count=active_count+1
ct=ct+1
e2.assign_id(input("Enter the employee id " + str(count)))
e2.assign_name(input("Enter the employee name " + str(count)))
e2.assign_des(input("Enter the employee designations " + str(count)))
e2.assign_salary(input("Enter the employee salary " + str(count)))
e2.assign_status(input("Enter the employee status " + str(count)))
e2.hike(input("Enter the number of years of work"))
q1=input("Enter y for yes to change the status of the employee else enter n for no")
if q2=='y':
    e2.status_reassign(input("Enter the new employee status ")
#if e2.status=="Active":
    #active_count=active_count+1
ct=ct+1
e3.assign_id(input("Enter the employee id " + str(count)))
e3.assign_name(input("Enter the employee name " + str(count)))
e3.assign_des(input("Enter the employee designations " + str(count)))
e3.assign_salary(input("Enter the employee salary " + str(count)))
e3.assign_status(input("Enter the employee status " + str(count)))
e3.hike(input("Enter the number of years of work"))
q3=input("Enter y for yes to change the status of the employee else enter n for no")
if q3=='y':
    e1.status_reassign(input("Enter the new employee status ")
#if e3.status=="Active":
    #active_count=active_count+1
ct=ct+1
e4.assign_id(input("Enter the employee id " + str(count)))
e4.assign_name(input("Enter the employee name " + str(count)))
e4.assign_des(input("Enter the employee designations " + str(count)))
e4.assign_salary(input("Enter the employee salary " + str(count)))
e4.assign_status(input("Enter the employee status " + str(count)))
e4.hike(input("Enter the number of years of work"))
q4=input("Enter y for yes to change the status of the employee else enter n for no")
if q4=='y':
    e4.status_reassign(input("Enter the new employee status ")
#if e4.status=="Active":
    #active_count=active_count+1
ct=ct+1
e5.assign_id(input("Enter the employee id " + str(count)))
e5.assign_name(input("Enter the employee name " + str(count)))
e5.assign_des(input("Enter the employee designations " + str(count)))
e5.assign_salary(input("Enter the employee salary " + str(count)))
e5.assign_status(input("Enter the employee status " + str(count)))
e5.hike(input("Enter the number of years of work"))
q5=input("Enter y for yes to change the status of the employee else enter n for no")
if q5=='y':
    e5.status_reassign(input("Enter the new employee status ")
#if e5.status=="Active":
   # active_count=active_count+1

        
        
