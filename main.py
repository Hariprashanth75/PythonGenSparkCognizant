# name = "Alex"
# age = 25
# height = 6.5

# print("Hi my name is", name , "and I am", age, "years old and I am ", height, "feet tall")

# num1 =50
# num2 =20
# print("The sum of", num1, "and", num2, "is", num1 + num2)
# print("The difference of", num1, "and", num2, "is", num1 - num2)
# print("The product of", num1, "and", num2, "is", num1 * num2)
# print("The quotient of", num1, "and", num2, "is", num1 / num2)
# print("The remainer of", num1, "and", num2, "is", num1 % num2)

# num = input("Enter  a number: ")
# num = int(num)
# if num > 0:
#   print("The number is positive")
# elif num < 0:
#   print("The number is negative")
# else:
#   print("The number is zero")


# age = int(input("Enter your age: "))
# if age >= 18:
#   print("You are eligible to vote")
# else:
#   diff = 18 - age
#   print("You are not eligible to vote only", diff, "more years to go")

# for i in range(5):
#   print("This is ",i, "of")
#   for j in range(5):
      
#     print("This is j", j**2)
# count=0
# while count < 5:
#   print(count)
#   count+=1

# for i in range(2,5):
# #   print("This is ",i, "of")
# #   for j in range(5):
#    print("This is i", i**2)

# for i in range(1, 6):
#   for j in range(1, 6):
#       print(f"{i * j:2}", end=" ")
#   print() 

# for i in range(5):
#   for j in range(5):
#      print(f"i = {i}, j = {j}")


# num = int(input("Enter a number: "))

# while num!=0:
#   print(num)
#   num-=1
#   if(num==0):
#     print("Blast off")

# for i in range(11):
#   print(f"i = {i} x {num} = {i*num}")

# def factorial(n):
#   result = 1
#   for i in range(1, n + 1):
#       result *= i
#   return result

# # Test the function
# num = int(input("Enter a number: "))
# result = factorial(num)
# print(f"The factorial of {num} is {result}")




# import random

# random_number = random.randint(1, 100)

# print("Welcome to the Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")
# i=0
# while True:
#     guess = int(input("Take a guess: "))
    
#     if guess < random_number:
#        i+=1
#        print("Too low! Try again.")
#     elif guess > random_number:
#         i+=1
#         print("Too high! Try again.")    
#     else:
#         print(f"Congratulations! You guessed the number { random_number } in { i } tries. ")
#         break



# value = "Python is amazing!"
# print("The first 6 letters ",value[0:6])
# print("The string in reverse order ",value[::-1])
# print("Sliced string ", value[10:])

# value = " hello, python world! "
# print(value.strip())
# print(value.capitalize())
# print(value.replace("python", "java"))
# print(value.upper())


# sample = input("Enter a string")

# remove_spaces = sample.replace(" ", "")
# if remove_spaces == remove_spaces[::-1]:
#   print("The string is a palindrome")
# else:
#   print("The string is not a palindrome")









# password = input("Enter a password: ")
# if len(password) < 8:
#     print("Password must be at least 8 characters long.")
# elif not any(char.isdigit() for char in password):
#     print("Password must contain at least one digit.")
# elif not any(char.isupper() for char in password):
#     print("Password must contain at least one uppercase letter.")
# elif not any(char.islower() for char in password):
#     print("Password must contain at least one lowercase letter.")
# else:
#     print("Password is valid.")
  


# squares = [x**2 for x in range(5)]
# print(squares)

# my_list = [1, 4, 5 , 2, 3]
# sorted_list = sorted(my_list)
# print(sorted_list)
# print(my_list[::-1])
# for item in my_list: 
#     print(item)

# for i, item in enumerate(my_list): 
#     print(i, item)

# print(my_list[0])
# print(my_list[-1])
# print(my_list[0:2])
# print(my_list[::-1])
# nested = [1, [2, 3], 4]
# print(nested[1][0])

# my_list.append("banana") 
# print(my_list)
# my_list.extend([5, 6]) 
# print(my_list)
# my_list.insert(1, "orange")
# print(my_list)

# my_list.remove("apple") 
# print(my_list)
# my_list.pop(1) 
# print(my_list)
# my_list.clear()
# print(my_list)

# squares = [x**2 for x in range(5)]
# print(squares)
# evens = [x for x in range(10) if x % 2 == 0]
# print(evens)
# matrix = [[i * j for j in range(5)] for i in range(5)]
# print(matrix)



# student = {"name": "Alex", "age": 21, "major": "Math"}
# print(student["name"])
# print(student.get("age"))
# student["grade"] = "A"
# print(student)
# if "Name" in student: 
#     print("Name is in the dictionary!")

# my_tuple = (1, 2, 3)
# single_element_tuple = (5,)
# print(my_tuple[0]) 
# print(my_tuple[0:2])

# fruits =["apple", "banana", "orange"]
# fruits.append("grape")
# fruits.remove("apple")
# print(fruits[::-1])
# for fruit in fruits:    
#     print(fruit)

# aboutMe ={"Name": "Harry", "Age": 22, "City": "Mumbai"}
# aboutMe["favourite_color"]="blue"
# print(len(aboutMe))
# for key, value in aboutMe.items():
#     print(key, value)

# inventory = {
# "apple": (10, 2.5),
# "banana": (20, 1.2),
# "orange": (15, 3.0),
# "grape": (5, 4.0)     
# }
# inventory["coconut"]= (8, 2.8)
# inventory["apple"]=(12, 2.5)
# inventory.pop("banana")

inventory = {}

# Get the number of items to be added to the inventory
num_items = int(input("Enter the number of items: "))

# Add items to the inventory
for i in range(num_items):
    item_name = input("Enter the name of the item: ")
    item_quantity = int(input("Enter the quantity of the item: "))
    item_price = float(input("Enter the price of the item: "))
    inventory[item_name] = (item_quantity, item_price)
    
for item, (quantity, price) in inventory.items():
    print(f"{item}: {quantity} in stock, ${price:.2f} per unit")
    
total_value = sum(quantity * price for quantity, price in inventory.values())
print(f"Total value of inventory: {total_value}")







































