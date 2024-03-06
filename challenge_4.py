#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

set1 = set()
set2 = set()

print("Enter intergers for the 1st set(type 'done' when finished)")

while True:
  number = input()
  if number.lower() == "done":
    break
  else:
    try:
      set1.add(int(number))
    except ValueError:
      print("Invalid Input!")

print("Enter intergers for the 2nd set(type 'done' when finished)")

while True:
  number = input()
  if number.lower() == "done":
    break
  else:
    try:
      set2.add(int(number))
    except ValueError:
      print("Invalid Input!")

common_elements = set1.intersection(set2)
print("The common elements are: ", common_elements)
