'''120078090
120078 090
870021 090
87,00,21 090
87,00,21, + , + 090'''
'''def inrc(a):
    s=''
    count=0
    for i in range(0,len(a)):
        if(i<(len(a)-3)):
            s=s+a[i]
            count=count+1
            if(count>=2):
                s=s+","
                count=0
        if(i>=(len(a)-3)):
            s=s+a[i]
            count=count+1
            if(count>=3):
                s=s+","
                count=0
    return s
print(inrc('1200780'))

def addl(a,b):
    final=[]
    for i in range(0,len(a)):
        final.append(a[i])
        final.append(b[i])
    return final
print(addl(['d','e','c'],[1,2,3]))'''

'''def add2(a,b):
    final=[]
    if(len(a)>=len(b)):
        for i in range(0,len(b)):
            final.append(a[i])
            final.append(b[i])
        for j in range(len(b),len(a)):
            final.append(a[j])
    if(len(b)>len(a)):
        for i in range(0,len(a)):
            final.append(a[i])
            final.append(b[i])
        for j in range(len(a),len(b)):
            final.append(b[j])
    return final
print(add2([1,3,5,7,9],[2,4,6,8]))
'''

def add3(a,b):
    final=[]
    if(len(a)>=len(b)):
        for i in range(0,len(b)):
            final.append(a[i])
            final.append(b[i])
        print(final+a[len(b):])
    else:
        for i in range(0,len(a)):
            final.append(a[i])
            final.append(b[i])
        print(final+b[len(a):])
add3([1,3,5,7,9],[2,4,6,8])

def pana(sttr):
    ct=0
    chars="qwertyuioplkjhgfdsazxcvbnm"
    for char in chars:
        count = sttr.count(char)
        if count < 1:
            return("It isnt a pangram")
        else:
            return("It is a pangram")
'''if(pana("The quick brown fox jumps over the lazy dog")==false):
    print("It isn't a pangram")
else:
    print("It isn't a pangram")'''
print(pana("The quick brown fox jumps over the lazy dog"))
