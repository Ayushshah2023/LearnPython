#call the test function from one.py
#every python file is a python module
''' you can import these modules into any files
any folder containing python files is called a python package'''
from dummy.two import sum,test
test()
a=int(input("Enter first number"))
b=int(input("Enter 2nd number"))
sum(a,b)
#-(Dummy)package
#herein sidha you can access the fns
#you can use one from and one import in your statement , hence till second last level use the from with dots and then use import
#object oriented programmming
"""
till now we have done functional programming
University(class)
    -univ_name(class attributes)
    -grading
    -location
each student(object)
    -student_id(Object attributes/features)
    -name
    -branch
    -year
    -grades


constructors : class name wala function called pehle sabse
self: first parameter of any function defined in hte class refers to any current obj
"""
