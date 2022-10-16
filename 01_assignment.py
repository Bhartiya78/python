#variable in python
a=10
b=10
print(a,b)
print(id(a),id(b))
#string concatenation in python
a="Hello"
b="World"
print(a+b)
print(a+" "+b)
c=20
print(c+30)
#airthmetic operators
'''Addtion(+)
Subtraction(-)
Multiplication(*)
Division(/)
Modulus(%): Reminder
Exponents(**)
Floor Division(//): Give Integers Values Only'''
a=20
b=30
print(a+b)
print(a-b)
print(a*b)
print(a/b)

print(a%3)

print(5**2)  #5*5
print(5**4)  #5*5*5*5

print(10//3)

#Assignment Operators
x=5
x+=5 # x+5
print(x)

x-=5
print(x)

#Camparison Operators
'''  ==: Equal Equal to
     !=: Not Equal
     >=: Greater than or Equal to
     <=: Less than or Equal to '''
     
x=10
y=20
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#Logical Operators
x=4
print(x<6 and x<8) #return true only if both the statements are true
print(x>5 and x>1)

print(x>4 or x>1) #return true if atleast one of the conditions are true
print(x>4 or x>5)

print(not(x>4 or x>5)) #it returns the reversed result(vice versa)

#5..identity operators
a=[40,50]
b=[40,50]
c=a
print(a is c) #returns true if both the variables are the same object pointing to a same memory location
print(b is a) ##it will return false because only object is same but the memory location is different here


