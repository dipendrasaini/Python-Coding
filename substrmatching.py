#Check if String Contains Substring in Python
 
substr ="denzil"
 
string="geeks for denzil"
 
q = len(substr)
 
n = len(string)
 
substr_counter = 0  
 
for i in range(n):
  if substr[substr_counter] == string[i]:
      substr_counter +=1
      if substr_counter == len(substr):
         print("Substring match")
         break       
  else:
      ## reset the counter
      substr_counter = 0 
      if i == len(string)-1:
         print("Substring NOt match")
         break
