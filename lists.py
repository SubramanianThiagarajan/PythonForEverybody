#list intro

myList = ['hello','world','example']
myNumList = [1,[2,3],4]
Empty = []

#Strings are immutable whereas Lists are mutable

#Length
print(len(myNumList))

for i in range(len(myList)):
	print(myList[i])

#Manipulation of Strings

#Concatenation
Num1 = [1,2,3]
Num2 = [4,5,6,1]
Num3 = Num1 + Num2
print(Num3)

#Slicing

print(myList[:2])
print(myList[2:2])
#Append
stuff = list()
stuff.append('Good')
stuff.append('Day')
print(stuff)
stuff.append(10)

print(10 in stuff) #Prints True

#Sort
stuff.append('ABC')
stuff.remove(10)
stuff.sort() #Only works for similar data type

print(stuff)
print(stuff)

#Getting List as input continuously with space
lst1 = [int(item) for item in input("Enter the list items : ").split()] 
print(lst1)

abc = "Three words only"
splitWord = abc.split()
#splitChar = abc.split('') We can't do this
#print(splitChar)
splitChar = list(abc)
print(splitChar)
print(splitWord)


#Dictionary wise list of unique words
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line = line.rstrip()
    l = line.split()
    for lt in l:
        lst.append(lt)
lst = list(set(lst))
lst.sort()
print(lst)


#Python 8.5 Exercise
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
email = list()
for line in fh:
    if line.startswith('From '):
        line = line.rstrip()
        lst = line.split()
        print(lst[1])
        count+=1
        
print("There were", count, "lines in the file with From as the first word")