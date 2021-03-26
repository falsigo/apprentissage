from math import *

print("|\    ")
print("| \   ")
print("|  \  ")
print("|___\ ")
#___________________________________________________________________
phrase = "Brazuca"
phrase_alt = "Brazooka"
print(len(phrase))
#___________________________________________________________________
print(phrase[0])

print(phrase.index("a")) #returns the index position of passed text, throws an error if not found
print(phrase_alt.index("o")) # notice how it is only printing the first occurence of the letter
print(phrase.replace("zu","zoo"))
#___________________________________________________________________
print(3 + 4)
print(3 * 4.5 + 90)
print(3 * (4.5 + 90)) #brackets supported
print(10 % 3) #modulus

my_num = 99
print(str(my_num)) #converting into string
#print( my_num + "This is my num") # this returns an error because cannot have a number concatenated with a string while still being a number

print(pow(4,5))
print(max(1212,3232))
print(round(3.44))
#___________________________________________________________________

#these are from the math function library
print(floor(log(1023, 2)))
print(ceil(log(1023, 2)))
print(sqrt(1000))

#___________________________________________________________________
#Getting input from the user

#name = input("Enter your name")
#age = input("Enter your age")
#print("Hello " + name + ", congrats on being " + age)

#___________________________________________________________________
#Creating a basic calculator

num1 = input("Enter a number")
num2 = input("Enter another number")
print(num1 + num2) #the result is a string, Python will automatically save any user input in the form of a string
#inorder to have the input being treated as a number we can simpy use the inbuilt python function int() and pass the user input variable inside

print(int(num1) + int(num2)) #does not allow float
print(float(num1) + float(num2))
