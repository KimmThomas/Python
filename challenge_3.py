#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

person_info = {}


person_info["name"] = input("Please enter your name: ")
person_info["age"] = input("Please enter your age: ")
person_info["favourite_color"] = input("Please enter your favourite color: ")

print(person_info)