def com(l1,l2):
    ct=0
    for i in l1:
        for j in l2:
            if(i==j):
                ct=ct+1
    if(ct<1):
        print("It is not overlapping")
    else:
        print("It is overlapping")
com([1,2,3,4,5],[6,7,8,9])

#s.lower() and s.upper()
#local and global variable
a=20
def pr(a):
    a=a+5
    print(a)
pr(10)
#if you want to remove the local variable and access the global value of a then you have to use (global a) before using it further
def pr():
     global a
     a=a+5
     print(a)
pr()
#inside a function you can refer a variable with same name as either as global or local
def test(b):
    global a
    a=b+5
    print(a)
test(20)
#o/p will be 25
#EXCEPTIONS
try:
    a=10
    b=0
    print(a/b)
#except:
   # print("ENter valid number")

except Exception as e:
    print("error" ,e)
    
            
