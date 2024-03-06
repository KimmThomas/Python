#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words = ["John", "Kim", "Joseph", "Emily", "Amos"]

odd_words = [word for word in words if len(word) % 2 != 0]

print("The words with odd number of characters are: ", odd_words)