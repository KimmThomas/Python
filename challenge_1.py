#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

numbers = []

#Get user input
while True:
  number = input("Enter a number (or 'done' to finish): ")
  if number.lower() == "done":
    break
  else:
    try:       #Try to convert the input to an integer and add to the list
      numbers.append(int(number))
    except ValueError:
      print("Invalid Number!")
total = sum(numbers)
print("The sum of all the integer numbers in the list is: ", total)