#Strings
string = "Hello_World"

#String Slicing

hello = string[:5]
world = string[6:]
llo_Wo = string[2:8]

#String Concatenation

string1 = hello + '_' + world

#if clause 'in'

if 'he' in string:
	print('Yes')

#String Comparison
# Z<a, A<a, b>a ASCII

if string == "Hello":
	print("Yes")
if string>"ABC":
	print("It comes after ABC")
else:
	print("It comes before ABC")

#String Library functions
string.lower() #Does not change the string itself
string = string.lower() #Changes the string
print(string)

#https://docs.python.org/2.5/lib/string-methods.html
#https://www.digitalocean.com/community/tutorials/an-introduction-to-string-functions-in-python-3

print(string.find('ll')) #returns 2
print(string.find('z')) #returns -1
print(string.find('l',4)) #After including 4th position where is the next occurence

print(string.replace('_',''))

print(string.startswith("He")) #returns False because it starts with he
print(string.endswith("ld")) #returns True

#Print Letter by letter
for letter in 'banana':
	print(letter)
