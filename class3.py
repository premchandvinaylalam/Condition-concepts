#string methods
#upper
#lower
#strip
#title

name = input("enter name")
text = input("text")
print(name.upper())
print(name.lower())
print(name.strip()) # it will clear the space if unwanted.
print(text.title()) #convert's the statement into title

#when you multiple a character with number we'll get character that many time.
print("a"*50)

#striped --- it will remove white spaces
name = "             Prem           "
print(name.strip())
print(len(name))  # len is 28 
print(len(name.strip())) #len will be 4