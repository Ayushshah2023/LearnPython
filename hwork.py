import array
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
employee=[]
i=0
e=array.array(i,[])
a=int(input("Enter the number of employees needed"))
active_count=0 
for i in range(1,a):
    e[i]=company()
    employee.append(e[i])
    employee[i].assign_id(input("Enter the employee id i "))
    employee[i].assign_name(input("Enter the employee name i " ))
    employee[i].assign_des(input("Enter the employee designations i "))
    employee[i].assign_salary(input("Enter the employee salary i "))
    employee[i].assign_status(input("Enter the employee status i "))
    employee[1].hike(input("Enter the number of years of work"))
    if (employee[i].status=="Active"):
        active_count=active_count+1
'''count=count+1
e2.assign_id(input("Enter the employee id "))
e2.assign_name(input("Enter the employee name " + str(count)))
e2.assign_des(input("Enter the employee designations " + str(count)))
e2.assign_salary(input("Enter the employee salary " + str(count)))
e2.assign_status(input("Enter the employee status " + str(count)))
e2.hike(input("Enter the number of years of work"))
if (e2.status=="Active"):
    active_count=active_count+1
count=count+1
e3.assign_id(input("Enter the employee id " + str(count)))
e3.assign_name(input("Enter the employee name " + str(count)))
e3.assign_des(input("Enter the employee designations " + str(count)))
e3.assign_salary(input("Enter the employee salary " + str(count)))
e3.assign_status(input("Enter the employee status " + str(count)))
e3.hike(input("Enter the number of years of work"))
if (e3.status=="Active"):
    active_count=active_count+1
count=count+1
e4.assign_id(input("Enter the employee id " + str(count)))
e4.assign_name(input("Enter the employee name " + str(count)))
e4.assign_des(input("Enter the employee designations " + str(count)))
e4.assign_salary(input("Enter the employee salary " + str(count)))
e4.assign_status(input("Enter the employee status " + str(count)))
e4.hike(input("Enter the number of years of work"))
if (e4.status=="Active"):
    active_count=active_count+1
count=count+1
e5.assign_id(input("Enter the employee id " + str(count)))
e5.assign_name(input("Enter the employee name " + str(count)))
e5.assign_des(input("Enter the employee designations " + str(count)))
e5.assign_salary(input("Enter the employee salary " + str(count)))
e5.assign_status(input("Enter the employee status " + str(count)))
e5.hike(input("Enter the number of years of work"))
if (e5.status=="Active"):
    active_count=active_count+1
    '''
