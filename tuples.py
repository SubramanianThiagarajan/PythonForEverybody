# tuples are represented in () Immutable 

myTuple = ('Hello', 'World', 'Python', 'is', 'awesome')

#Things not to do with tuples
# tuple.sort()
# tuple.append(5)
# tuple.reverse()

#Simulataneous assignment
(x,y) = (10,20)
print(x)

#dictionary.items() gives a list of tuples

if (0,1,2) < (3,2,1):  #returns True because compares only the first element in the tuple
	print('yes')

#To sort a dictionary
d = dict()
d['one']=1
d['two']=2
d['three']=3

print(d)
print(sorted(d.items())) #Because d.items() is a list of tuples
print(d)

#Output of Above Code
'''
{'one': 1, 'two': 2, 'three': 3}
[('one', 1), ('three', 3), ('two', 2)]
{'one': 1, 'two': 2, 'three': 3}
'''

for k,v in sorted(d.items()):
	print(k,v)

#Sort by values
c = {'a':10,'c':20,'b':5}
tmp = list()
for k,v in c.items():
	tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=True)
print(tmp)


#The above code can be done using list comprehension
print(sorted([(v,k) for k,v in c.items()], reverse=True))
#It creates a dynamic list


#10.2 Exercise
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
time = list()
for line in handle:
    if line.startswith('From '):
        line = line.rstrip()
        lst = line.split()
        time.append(lst[-2][:2])
count = dict()
for i in time:
    count[i] = count.get(i,0) + 1

for k,v in sorted(count.items()):
    print(k,v)