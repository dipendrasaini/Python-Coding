string = "amaama"
= len(string)
temp = 0
 
print(n//2)
 
for i in range(int(length/2)):
  if string[i] == string[length -1 - i]:
       if i == int(length/2)-1 :
         print("Palindrom")
  else:
     print("String is not palidrom")
  if string[i] == string[int(len(string)/2)-1+i]:
     temp = temp+i 
     if temp == int(len(string)/2)-1:
        print("String is symmetrical")
  else :
      if temp == int(len(string)/2)-1:
        print("String is Not symmetrical") 

  # key take away from this question is
  # range(5) -> 0,1,2,3,4
  # range("string") -> s \n t \n r \n i \n g \n
  # // -> produce integer value
  # add += 1 => is the logice to add directly 
  # add -=1 => for decresing the logic 
  # always flag value for comparistion of string
