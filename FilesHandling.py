fh = open('lorem.txt') #by default read
print(fh) #Does not print the files content, but the file handlers specifications
#<_io.TextIOWrapper name='lorem.txt' mode='r' encoding='cp1252'>

#for loop interprets x in fh as sequence of lines
count =0
line = 0
for x in fh:
	if x == '\n':
		count+=1
	print(x)
	line+=1
print(count) #Prints 0 because it interprets a whole line
print("This file has", line)

#To read the whole file into a var
fh = open('lorem.txt')
text = fh.read() #Reads inclusive of all the characters including newline
print(len(text))

print(text[:11])


#Using string functions

fh = open('lorem.txt')
for line in fh:
	line.rstrip()		#Strips off newline at the end of the line
	if line.startswith('Lorem'):
		print(line)


fh = open('lorem.txt')
for line in fh:
	if line.startswith('Lorem'):
		print(line)


#Assignment1
# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.strip()
    print(line.upper())

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
s =0
c=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find('0')
    num=line[pos:].rstrip()
    s+=float(num)
    c+=1
print("Average spam confidence:", s/c)
