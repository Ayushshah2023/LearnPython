#lambda functions
''' An approach to create a function'''
display= lambda s,q:(s+q)
print(display(12,33))
even_odd= lambda num:"Even" if num%2==0 else "Odd"
print(even_odd(int(input("Enter a number"))))
#IF ELSE in a line
#full whether wala widget types
#filter functions
li=[1,2,3,4,5,6,7,8,9,10]
#def is_even(num):
   # lambda num:True if num%2==0 else False
    #return
final=filter(lambda num:True if num%2==0 else False,li)
print(list(final))


#MAP common operation to a list
li=[1,2,3,4,5,6]
finale=map(lambda num:num*num , li)
print(list(finale))

#MAp,Filter both take functions as arguments thus they are called as HIGHER oRDER functions
#map is usually used as IP to higher order functions
#map is an anonymus
