#Functions
def Hello():
	print("Hello World")
	print("This is a function")

#Power function
def powerfind(num,p):
	return num**p

Hello()
print(powerfind(10,2))
print(pow(10,3)) #Inbuilt Function

#Largest Number - While loop
m=0
while True:
	a = int(input("Enter a Number,-1  to break"))
	if a > m:
		m=a
	elif a==-1:
		break
print("Largest Number:",m)

#None Value
a = None #It means an abscence of a value

#'is' matches both type and value

#Another way for if loop
b=0
if b is 0 : print("b is 0") 


#largest and smallest with try and except

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else:
        try:
            num=int(num)
            if largest is None and smallest is None:
                largest = smallest = num
            else:
                if num>largest:
                    largest = num
                elif num<smallest:
                    smallest=num
              
        except:
            print("Invalid input")   

print("Maximum is", largest)
print("Minimum is", smallest)

#For Loop

for i in [1,2,3,4,5]:
	print(i)
for i in range(0,10,2):
	print(i)