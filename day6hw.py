'''def num1():
    count=0
    res=83
    while(res!=0):
        a=int(input("Enter a number between 0 and 100"))
        if(a<res):
            print("The number you have entered is lesser than expected")
            count=count+1
            #return num1(b)
        elif(a==res):
            count=count+1
            print("Correct answer  " + str(count) + " tries were used")
            break
        else:
            print("Answer is larger than in expected value")
            count=count+1
            #return num1(b)
num1()
'''
def num2(res):
    count=0
    while(res!=0):
        a=int(input("Enter a number between 0 and 100"))
        if(a<res):
            print("The number you have entered is lesser than expected")
            print("This means the number is between "+str(a)+" to 100")
            count=count+1
        elif(a==res):
            count=count+1
            print("Correct answer  " + str(count) + " tries were used")
            break
        else:
            print("Answer is larger than in expected value")
            print("This means the number is between 0 to "+str(a))
            count=count+1
num2(55)
