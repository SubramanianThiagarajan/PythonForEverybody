#Dictionary

myDictionary = dict()
myDictionary['Web'] = 'HTTP'
myDictionary['Mail'] = 'SMTP'
myDictionary['File'] = 'FTP'

print(myDictionary)

# Dicts are represented in {}

#Counting words in a list
count = dict()
lst = ['one','second','one','one','third']
for name in lst:
	if name in count:
		count[name]+=1
	else:
		count[name]=1
print(count)

'''
counts.get(name,0) 
It searches for the name key in the dict count, if the key doesn't exit it returns 0
'''
count=dict()
for name in lst:
	count[name] = count.get(name,0)+1
print(count)

#For loop
for key in count:
	print(key, count[key], sep='#') #Separated Key and count key with #
	print(key,count[key],end='#')	#Ends the line with # Does not do \n

#When you convert a dictionary to a list, only key comes into it
#Keys() and values() method

print(count.keys(),end='\n\n')
print(count.values(),end='\n\n')
print(count.items()) #returns a tuple of key and value pairs dict_items([('one', 3), ('second', 1), ('third', 1)])

#Iterate through for loop
for k,v in count.items():
	print(k,v)

print('#'.center(5,' '))

count.update( {'Welcome' : 23} )
print(count)

#9.4 Exercise

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
email = list()
for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        lst = line.split()
        email.append(lst[1])
count = dict()
maxemail = None
maxcount = None
for i in email:
    count[i] = count.get(i,0) + 1
    if maxcount is None or maxcount<count[i]:
        maxemail = i
        maxcount = count[i]
        
print(maxemail, maxcount)