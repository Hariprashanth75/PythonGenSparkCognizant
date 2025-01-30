age = int(input("Enter your age: "))
if age >= 18:
  print("You are eligible to vote")
else:
  diff = 18 - age
  print("You are not eligible to vote only", diff, "more years to go")