#Create your own Python code examples that demonstrate each of the following. 
#Do not copy examples from the book or any other source. 
#Try to be creative with your examples to demonstrate that you invented them yourself.

#Example 1: Define a function that takes an argument.
#Call the function. Identify what code is the argument and what code is the parameter.

print =("Hello My name is Justin")    

#will return "Hello My name is Justin"

#a will return Hello My name is Justin
#a is  the argument and "hello my name is Justin" is the parameter

#Example 2: Call your function from Example 1 three times with different kinds of arguments: 
#a value, a variable, and an expression.
 #Identify which kind of argument is which. 

print(type("Hello My name is Justin"))
#<class 'str'>
print(type(2-1))
#<class 'int'>
print(type(2.4))
#<class 'float'>


#Example 3: Create a function with a local variable. 
# Show what happens when you try to use that variable outside the function. 
# Explain the results.

def function ():
  name="Justin"
  print("hello "+ name)

function()

print(name)
#Traceback (most recent call last):File "<stdin>", line 1, in <module>NameError: name 'name' is not defined
#name is not defined because it is a local variable and is only available within the function.


#Example 4: Create a function that takes an argument.       
# Give the function parameter a unique name. 
# Show what happens when you try to use that parameter name outside the function. Explain the results.

def function(param):
    a=param*2
    print(a)

print(param)

#Traceback (most recent call last):File "<stdin>", line 1, in <module>NameError: name 'param' is not defined>>> 

param=1
print(param)

#the parameter is not defined because it is a local variable and is only available within the function.


#Example 5: Show what happens when a variable defined outside a function has the same name as a local variable inside a function. 
#Explain what happens to the value of each variable as the program runs.

a=1201
def function():     

    a=1202
    print(a)

#print(a)
#1201
#function()
#1202