#This is a basic calculator that requires the user to input two numbers and the operation for the program to run.
#The operation signs in this calculator are (+ _ * /)
#The output will be the result of opeartion used and the numbers the user inputs.

#This function will add two numbers
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
sum = firstNumber + secondNumber
print("The difference of the two numbers is: ", sum)


#This function will subtract two numbers
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
difference = firstNumber - secondNumber
print("The difference of the two numbers is: ", difference)

#This function will multiply two numbers
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
product = firstNumber * secondNumber
print("The product of the two numbers is: ", product)

#This function will divide two numbers
firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
division = firstNumber / secondNumber
print("The quotient of the two numbers is: ", division)