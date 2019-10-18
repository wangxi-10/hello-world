Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(1,10):
	print('{}^3={}',format(i,i**3))

	
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    print('{}^3={}',format(i,i**3))
TypeError: format() argument 2 must be str, not int
>>> for i in range(1,10):
	print('{}^3={}'.format(i,i**3))

	
1^3=1
2^3=8
3^3=27
4^3=64
5^3=125
6^3=216
7^3=343
8^3=512
9^3=729
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i in range(0,10):
	print(' '*(9-i),'*'*(2*i+1))

	
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> for i in range(0,10):
	print(' '*(9-i),'*'*(2*i+1),sep='')

	
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=list(range(1,10))
>>> print(a)
[1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> del a[0]
>>> print(a)
[2, 3, 4, 5, 6, 7, 8, 9]
>>> a.clear()
>>> print(a)
[]
>>> a=list(range(1,4))
>>> b=a
>>> print('a:',a)
a: [1, 2, 3]
>>> print('b:',b)
b: [1, 2, 3]
>>> del b[0]
>>> print('a:',a)
a: [2, 3]
>>> print('b:',b)
b: [2, 3]
>>> 

>>> 
>>> a=range(1,4)
>>> b=a.copy()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    b=a.copy()
AttributeError: 'range' object has no attribute 'copy'
>>> 
>>> 
>>> 
>>> a=list(range(1,4))
>>> b=a.copy
>>> print('a:',a)
a: [1, 2, 3]
>>> print('b:',b)
b: <built-in method copy of list object at 0x000001D752CE4BC8>
>>> 
>>> 
>>> 
>>> 
>>> a=list(range(1,4))
>>> b=a.copy()
>>> print('a:',a)
SyntaxError: multiple statements found while compiling a single statement
>>> 
>>> 
>>> 
>>> 
>>> a=list(range(1,4))
>>> b=a.copy()
>>> print(a)
[1, 2, 3]
>>> print(b)
[1, 2, 3]
>>> b.append(4)
>>> print(b)
[1, 2, 3, 4]
>>> print(a)
[1, 2, 3]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> a=[1,2,3,[4,5]]
>>> a[3][0]
4
>>> b=a.copy()
>>> print(a)
[1, 2, 3, [4, 5]]
>>> print(b)
[1, 2, 3, [4, 5]]
>>> a[3][0]=4.1
>>> print(a)
[1, 2, 3, [4.1, 5]]
>>> print(b)
[1, 2, 3, [4.1, 5]]
>>> 
>>> a[0]=0
>>> print(a)
[0, 2, 3, [4.1, 5]]
>>> print(b)
[1, 2, 3, [4.1, 5]]
>>> 
>>> 
>>> 
>>> 
>>> import copy
>>> a=[1,2,3,[4,5]]
>>> 
>>> 
>>> 
>>> 

>>> 
>>> from copy import deepcopy
>>> b=deepcopy(a)
>>> print(a）
	  
SyntaxError: invalid character in identifier
>>> print(a)
	  
[1, 2, 3, [4, 5]]
>>> print(b)
	  
[1, 2, 3, [4, 5]]
>>> 
	  
>>> 
	  
>>> 
	  
>>> 
	  
>>> end
	  
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    end
NameError: name 'end' is not defined
>>> 
	  
>>> 
	  
>>> 
	  
>>> 
	  
>>> 
	  
>>> 
