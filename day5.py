'''#FUNCTIONS
#function definations
#function calling
def display(s):
    return s
#In the parentheses you will pass parameters
response = display('bca')
print(response)
#this is similar to java bas the only diff is that we dont have to mention the return type of the function
#onput is arguments
#functions are methods
def sq(q):
    return int(q*q)
a=sq(5)
print(a)'''
'''#here in we have toa ssume that the the marameter is in the format that you want it in , htus you  dint have to specify the datatype to a parameter
def lena(s):
    count=0
    for i in range(0,len(s)):
            count=count+1
    return count
q=lena("q w e r")
print(q)
#herein i isnt used hence you can replace it with an _'''
'''def conn(usd):
    return usd*70
print(conn(75))
def conn1(inr):
    return inr/70
print(conn1(7500))'''
'''def facto(a): 
    prod=1
    for i in range(1,a+1):
        prod=prod*i
    return prod
print(facto(8))'''
'''pro=1
def fra(b):
    pro=pro*b
    if(b-1>0):
        return fra(b-1)
    if(b==1):
        print(pro)
 '''   
'''#print(fra(5))
def q(s):
    if(s==1):
        return s
    else:
        return(s*q(s-1))
print(q(5))
'''
'''def cot(li):
    lit=[]
    for i in range(0,len(li)):
        lit.append(len(li[i]))
    print(lit)
print(cot(['abc','xyz','abc']))
'''
'''def filter_long_words(li,a):
    lit=[]
    for i in li:
        if(len(i)>a):
            lit.append(i)
    print (lit)
print(filter_long_words(['abc','xyz','abc'],2))'''

def inrc(a):
    n=1
    for i in range(1,int((len(a)/3))):
        if(len(a)>((3*i)+1)):
            a.insert((-3*n),",")
            n=n+1
        '''if(len(a)>=4):
            a.insert(-3,",")
        if(len(a)>=7):
            a.insert(-6,",")
        if(len(a)>=10):
            a.insert(-9,",")'''
        return a
print(inrc([1,1,1,1,2,2,2,3,3]))
'''
'aaabbabaaaccca' -> {'a':6,'b':3,'c':1}
'aaaabbcabadaabb' -> 'abcabadab' remove the redundant cases
'''
def dictc(a):
    dict={}
    li = "abcd"
    for i in li:
        count = a.count(i)
        if count > 1:
            dict.update({i:count})
    print(dict)
dictc("aabbaabbaccaabcbabaabcbab")

def red(a):
    b=''
    for i in range(0,len(a)):
        if(i<(len(a)-1)):
            if(a[i]!=a[i+1]):
                b=b+a[i]
        if(i>=len(a)-1):
            if(a[i]!=a[i-1]):
                b=b+a[i]
    print(b)
red('aaabbabaaaccca')
        
