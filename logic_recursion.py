############ Q1. Ask the user for an integer, multiply it by itself + 1, and print the result
# Topic: user input

integer = int(input("Choose an integer"))

integer = integer + (integer + 1)

print(integer)

############ Q2. Ask the user for an integer
# If it is an even number, print "even"
# If it is an odd number, print "odd"

# Topic: conditionals, user input

number = int(input("Give me an integer"))
if number % 2 == 0:
    print("even")
else:
    print("odd")

############# Q3. Iterate through each element in the list USING A FOR LOOP, add 5 to it, and print them 
# Topic: loops + lists

numbers = [1, 2, 3, 4, 5]

# Code here

for A in numbers:
    A += 5
    print(A)

# ############# Q4. Iterate through the list and only print values that are divisible by 3 ############
# Topic: list, loops, conditions, comparison operators

numbers = list(range(0, 500))

# Code Here

for number in numbers:
    if number % 3 == 0:
        print (number)
    else:
        pass

# ############# Q5. Iterate through the list and count the number of even numbers within the list ############
# Topic: lists, loops, conditions, comparison operators

numbers = list(range(0, 500))

# Code Here

for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        pass

############# Q6. Iterate through each element in the list, add 5 to it, and print them
# MUST USE A WHILE LOOP
# Topic: loops + lists
# Hint: You can use len() function

numbers = [1, 2, 3, 4, 5]

# Code here

for number in numbers:
    number += 5
    print(number)




############# Q7. For the following list:
# Print ALL numbers divisible by 7 and label them like so: "Divisible by 7: 70"
# Print ALL numbers divisible by 3 and label them like so: "Divisible by 3: 6"
# Print ALL numbers divisible by 3 and 7 and label them like so: "Divisible by 3 and 7: 21"
############

# Topic: lists, loops, conditions, string concatenation

numbers = list(range(0, 500))

# Code here

for number in numbers:
    if number % 3 and number % 7 == 0:
        print("Divisible by 3 and 7:", number)
    else:
        pass 



