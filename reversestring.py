# reverse the string
 
string = "geeks quiz practice code"
 
n = len(string)
 
i = 0
 
newstr=""
 
while (i < n):
 
  newstr+=string[n-1-i]
  i+=1
print(newstr)

 
 
## string are immutable u can modified the string like above
