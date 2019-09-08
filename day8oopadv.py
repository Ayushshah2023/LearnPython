class stack:
    def __init__(self):
        self.li=[]
    def push(self,value):
        self.li.append(value)
    def pop(self):
        if(len(self.li)>=1):
            del self.li[-1:]
        else:
            print("Enter a data to pop out")
    def display(self):
        for i in range(len(self.li)):
            print(self.li[i])
    def length(self):
        print(len(self.li))
    def peek(self):
        print(self.li[-1])
s1=stack()
s1.push(5)
s1.push(3)
s1.display()
s1.pop()
s1.display()
s1.push(9)
s1.push(11)
s1.peek()
s1.display()
s1.length()

#merge sort in python
