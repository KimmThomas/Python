#Break statement: with this, we can stop the loop even if the while conditition is true

x = 1
while x < 10:
  print(x)
  if x == 3:
    break
  x += 1               #This  can be done before the if statement but now it will exclude 3 in the output because the increament will be before the if statement. x will be 2

#Continue Statetement: Stopm current and continue to the next. Here we increment 1st and print after

x = 0
while x < 10:
  x += 1
  if x == 3:       #This gives the option to skip over the path of the loop where the external condition is triggered but returns and continues with the code. Results will skip 3
    continue
  print(x)


#else condition
  
  q = 1
  while q < 10:
    print(q)
    q += 1
  else:
    print("is q not less than 10")



#for loop
    music_genre = ["pop", "jazz", "pop"]
    for music in music_genre:
      print(music)
      if music == "jazz":         #displays upto the condition
        break

