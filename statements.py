#if
#if-else
#if-elif-else

#Sequence structure - Execute as they appear
#Decision Structure - a condition must be met

#Boolean Expressions - Has to be evaluated and outcome is True/False
#relational operators (<, >, <=, >=, !=, ==)

num = 0

num1 = 1

if num > num1:
  print("num is greater than num1")  #Identation - The space before print
else:
  print("num1 is greater than num")  #False block of code

#if-elif-else statement - multiple conditions
# grading system >80 - A, >70 - B, >60 - C, >50 - D, <50 - Fail
  
marks = int(input("Enter your Marks: "))

if marks >= 81 and marks <= 100:
  print("A")
elif marks >= 71 and marks <= 80:
  print("B")
elif marks >= 61 and marks <= 70:
  print("C")
elif marks >= 51 and marks <= 60:
  print("D")
elif marks >= 0 and marks <= 50:
  print("Fail")
else:
  print("Out of Range")