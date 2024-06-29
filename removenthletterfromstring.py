#How to Remove Letters From a String in Python
 
x = 'Geeks123For123Geeks'
 
# remove 7th charctor from string
 
n = len(x)
 
sublen1 = len(x[:7])
 
sublen2 = len(x[8:])
 
 
print(sublen1)
print(sublen2)
 
start = x[:7]
 
print(x[:7])
 
print(x[8:])
 
finalstr = x[:7]+x[8:]
 
print(finalstr)
