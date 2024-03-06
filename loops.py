#while loop - used to iterate over a block of code as long as the test expression is true
#Example 1

x = 1    #int

while x < 10:
  print(x)
  x += 1     #0r x = x + 1

#Example 2

n = 10
sum = 0       #sum = 1 +2 + 3 .....+ n
x = 1         #counter

while x <= n:
  sum = sum + x
  x += 1            #update counter (indexing variable)

  print(" The sum is ", sum)