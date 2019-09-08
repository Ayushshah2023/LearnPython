'''lis=['allison','van dijk','trent','robertson','joe','henderson','gini','afabhino','mane','salah','bobby']
count=0
for el in lis:
    if(el[0]=='a'or el[0]=='e'or el[0]=='i'or el[0]=='o'or el[0]=='u'):
        count=count+1
print(count)      
# you can use a list of vowels and then add if i[0] in vowels
#herein the variable attache to the for lop can access th element directly, thus if it is a string then var[0] will access the first element of the string
lise = [1,2,3,4,5,6,7,8,9,10,11,12]
sum=0
for i in lise:
    sum= sum + i
print(sum)
#idhar to access hte element you don't have to use arrayname[0] , if you have designated a varaible w for it then directly use w
#DOUBT why count++ doen't work and concept of arrays in python
#pythontutor
#wapp , taking a int as input , print 3,5,35 if the number is divisible by 3,5,both,none
qw = int(input("Enter a number"))
if (qw%3==0 and qw%5!=0):
    print(3)
elif (qw%5==0 and qw%3!=0):
    print(5)
elif(qw%3==0 and qw%5==0):
    print(35)
else:
    print(0)
#if you use both wala case first , then masti nahi hoyenga
'''
'''lin=[10,33,25]
sum=0
count=0
for q in lin:
    while((z/10)!=0):
        count=count+1
        z=z/10
    w=str(q)
    z=len(w)
    for e in range(0,z):
        sum=sum+int(w[e])
print(sum)
#Yaha pe range isn't required sidha you can write for e in z'''

'''lise=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
li=[1,2,3,4,5,6,7,8,9,10]
for i in lise:
    for j in li:
        print( str(i) + 'x' + str(j) + '= ' + str((i*j)))
    print("-"*7)
#Herein the string can be multiplied to each other'''

#WHile loop
count=0
while count<11:
     print(count)
     count=count+1

li=[10,20,30,40,50,60,70,80,90,100]
sum=0
ct=0;
while ct<len(li):
    sum=sum+li[ct]
    ct+=1
print(sum)


     

