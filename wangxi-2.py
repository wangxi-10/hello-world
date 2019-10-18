Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=[1,2,3]
>>> b=[4,5,6]
>>> print(a+b)
[1, 2, 3, 4, 5, 6]
>>> a=a+b
>>> a
[1, 2, 3, 4, 5, 6]
>>> b
[4, 5, 6]
>>> a+b
[1, 2, 3, 4, 5, 6, 4, 5, 6]
>>> 
>>> 
>>> 
>>> a=[1,2,3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=list(range(0,6))
>>> print(a)
[0, 1, 2, 3, 4, 5]
>>> a.reverse()
>>> print(a)
[5, 4, 3, 2, 1, 0]
>>> 
>>> 
>>> 
>>> 
>>> import random
>>> value = random.randint(1,6)
>>> print(value)
2
>>> 
>>> a=list()
>>> for i in range(0,20):
	a.append(random.randint(1,6))

	
>>> print(a)
[6, 4, 5, 4, 5, 3, 4, 1, 5, 5, 1, 3, 5, 6, 6, 6, 1, 4, 5, 3]
>>> a.sort()
>>> 
>>> print(a)
[1, 1, 1, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6]
>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> month=int(input('please input the mouth:'))
please input the mouth:3
>>> day=int(input('please input the day:'))
please input the day:5
>>> count=day
>>> if month>1:
	count+=31

	
>>> if month>2:
	count+=28

	
>>> if month>3:
	count+=31

	
>>> if month>4:
	count+=30

	
>>> print(count)
64
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 

>>> import random
>>> for i in range(0,60000):
	value=random.randint(1,6)

	
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import random
>>> count=[0]*6
>>> for i in range(0,60000):
	value=random.randint(1,6)
	count[value-1]+=1

	
>>> print(count)
[9961, 10204, 9892, 10023, 10004, 9916]
>>> 
