
##PLEASE FILL OUT THE BELOW DETAILS
##Student Name:  Binod Gurung
##Course Number: SIMR/20/001
##Student Number: 21171412

#Section 1 25 Marks


#1) Create and Assign a type float variable called fltOne the value 10 (3)

fltOne = float(10)
print(fltOne)

#2) Create and Assign a type float variable called fltTwo the value 20 (3)

fltTwo = float(20)
print(fltTwo)

#3) Create and Assign a type float variable called fltThree with the product of fltTwo and fltOne(3)

fltThree = float(fltOne * fltTwo)

#4) Create and assign a variable called stringOne with the value "The product of fltOne and fltTwo = "(3)

stringOne = "The product of fltOne and fltTwo = "

#5) On the console, output stringOne and fltThree (in that order) (3)

print(stringOne, fltThree)

#6) increment fltOne  (3)

fltOne += 1

#7)  prompt the user to provide an input to fltTwo with the message "Please provide another number for fltTwo". Ensure a float is given (4)

fltTwo = float(input("Please provide another number for fltTwo."))

#8) on the console, output the product of fltOne and flotTwo with a suitable message (3) 

product = fltOne * fltTwo
print("The product of fltOne and fltTwo is:" , product)

#####################################################
#Section 2 35 Marks

#8) take the input from fltTwo and apply a decision based on the number inputted . 
#The decision should be based on if the user inputs a number below 100 
#the code should output "below 100" (5)

if fltTwo < 100:
    print("below 100")

#9) take the difference between of fltOne and fltTwo (fltOne - fltTwo)

difference = fltOne - fltTwo
print(difference)

#Using if, else and elif, output the following: 
#If the product is below 0, output "below 0"
#if the product is 0 output "value is zero"
#if the product is above 0 output "above 0" (8)

if product < 0:
    print("below 0:")
elif product == 0:
    print("value is zero")
else:
    print("above 0")

#10) create a list called listOfInts (4)

listOfInts = []

#11 part a) create a for loop to iterate through the above list and populate the list with 
#{4,6,8,10,12,14,16,18,20,22}. Output the list to the console with a suitable message(7)

number = 2
for i in range(10):
    number += 2
    listOfInts.append(number)
    
print(listOfInts)

#11 part b) create a for loop to iterate through the above list and 
#multiply each value by three assigning the new value to the respective 
#index in the list. The list should now look like {12,18,24.....} (8)

for j in listOfInts:
    new_number = j * 3
    listOfInts.append(new_number)

print(listOfInts)


#11 part c )output listOfInts to the screen with a suitable message (3)
