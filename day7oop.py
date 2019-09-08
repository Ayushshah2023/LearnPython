#for basics see one.py
'''class university:
    univ_name="Mumbai University"
    def __init__(self,stu_name,stu_id,stu_bran):#yeh name or og par name alag ho sakta hai
        self.name=stu_name
        self.id=stu_id
        self.branch=stu_bran#constructor ka naam hi yahi hai
        print("AN OBJ IS CREATED")
    def assign_name(self,student_name): #self:student1,student_name=user
        self.name=student_name #name=user
    def assign_id(self,student_id):
        self.id=student_id
    def assign_branch(self,student_branch):
        self.branch=student_branch

student1=university()
student2=university()
count=0
print(student1.univ_name)#object_name.attribute_name
count=count+1
#multiple access in this can be done by for loop
student1.assign_name(input("Enter student " + str(count)+" name"))
student1.assign_id(input("Enter student "+ str(count)+" id"))
student1.assign_branch(input("Enter student "+ str(count)+" branch"))
print(student1.name)
print(student1.id)
print(student1.branch)
count=count+1
student2.assign_name(input("Enter student "+ str(count)+" name"))
student2.assign_id(input("Enter student "+ str(count)+" id"))
student2.assign_branch(input("Enter student "+ str(count)+" branch"))
print(student2.name)
print(student2.id)
print(student2.branch)
# DOUBT HOW TO DO THIS student3=university(input("Enter name"),input("Enter ID"),input("Enter branch"))
'''
'''
This all can be done by condstructors

def __init__(self,stu_name,stu_id,stu_bran):
    self.name=stu_name
    etc
    etc
now niche
student1= Universuty(1,"abc",'extc')
'''

class circle:
    def assign_rad(self,radius):
        self.radius=radius
    def assign_col(self,colour):
        self.colour=colour
    def area(self,radius):
        pi=float(3.142)
        print(pi*float(radius)*float(radius))
count=0
c1=circle()
c2=circle()
count=count+1
c1.assign_rad(input("Enter radius of circle " + str(count)))
c1.assign_col(input("Enter colour of circle " + str(count)))
c1.area(c1.radius)
print(c1)
count=count+1
c2.assign_rad(input("Enter radius of circle " + str(count)))
c2.assign_col(input("Enter colour of circle " + str(count)))
c2.area(c2.radius)
'''
create a class called company D
object is an employee D
employee-employee id D, name, designation,salary,statue-{active(default),terminated,suspended}
annual hike is 10% of the og sslaryD
hike ratio is a class attribute  D
fina a way to assign valuesD
at least 5 objectsD
function compute hike (self)D
hike in rupees for that annual yearD
change status(self,new status)
count of all the active employee in class
active to others and others to active should affect it
'''


