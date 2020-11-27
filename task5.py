#1) create a function getting two integer inputs from user.& print the following:
#a) Addition of two number is + value

def addition(a,b):
add=a+b
print("addition of two numbers:",a+b)
addition(200,100)
#output= addition of two numbers: 300

#b) Subraction of two numbers is + value

def subraction(a,b):
sub=a-b
print("subraction of two numbers:",a-b)
subraction(200,100)
#output= subraction of two numbers: 100

#c) Division of two numbers is + value

 def division(a,b):
 div=a/b
 print("division of two numbers:",a/b)
 division(200,100)

 #output=division of two numbers: 2

#d) Multiplication of two numbers is + value

def multiplication(a,b):
mul=a*b
print("multipication of two numbers:",a*b)
multiplication(200,100)

#output= multipication of two numbers: 20000

#2) create a function covid() & it should accept patient name,and body temperature,by default the body temperature should be 98 degree:

def covid(patient_name):
print("Name of the patient:"+patient_name+"")
covid('tian')

#output= Name of the patient:tian

def covid(body_temperature):
print("Body temperature of the patient:"+body_temperature+"")
covid('98 degree')

#output= Body temperature of the patient:98 degree
