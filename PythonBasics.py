#Hello World Program

print("Hello World")

#Input Statements
myVar = input("What's your name?")
print("Hello " + myVar + ", Welcome to python")

#Comments
# Single line Comments
'''
Multiline
Comment
''' 

#Conditional Statements
myNum = int(input("Enter a Number"))
if myNum == 10:
	print("It's ten")
elif myNum>10:
	print("It's greater than ten")
else:
	print("It's less than ten")


#try - except
mystr = input("Enter something:")
try:
	mystr = int(mystr)
except:
	print("The string is not a number")


#Grade program
score = float(input("Enter Score: "))

if score>=0.0 or score<=1.0:
    if score>=0.9:
        print('A')
    elif score>=0.8:
        print('B')
    elif score>=0.7:
        print('C')
    elif score>=0.6:
        print('D')
    else:
        print('F')
else:
    print("Error")


#While and for loop
i,add=0,0
while True:
	a = int(input("Enter a positive number"))
	if a>0:
		i+=1
		add = add + a
	else:
		break;
print(add)
print(add/i)


