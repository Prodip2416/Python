Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dt={1:90,2:92,3:90}
>>> dt[3]
90
>>> dt[1]
90
>>> dt={'rafi':90}
>>> dt
{'rafi': 90}
>>> dt[1]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dt[1]
KeyError: 1
>>> dt['rafi']
90
>>> li=[1,2,3]
>>> dt={1:li}
>>> dt[1]
[1, 2, 3]
>>> type(dt)
<class 'dict'>
>>> dt={1:78}
>>> dt[1]
78
>>> dt={1:56,2:67,3:78}
>>> dt
{1: 56, 2: 67, 3: 78}
>>> del dt[3]
>>> dt
{1: 56, 2: 67}
>>> dt[3]=78
>>> dt
{1: 56, 2: 67, 3: 78}
>>> for i in dt
SyntaxError: invalid syntax
>>> for i in dt:
	print(i)

	
1
2
3
>>> for i in dt:
	print(i),dt[i]

	
1
(None, 56)
2
(None, 67)
3
(None, 78)
>>> for i in dt:
	print(i,end=' ' ),dt[i]

	
1 (None, 56)
2 (None, 67)
3 (None, 78)
>>> dt.keys()
dict_keys([1, 2, 3])
>>> for i in dt.keys():
	print dt[i]
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(dt[i])?
>>> 
>>> for i in dt.keys():
	print(dt[i])

	
56
67
78
>>> for key,value in dt.iteritems():
	print(key,value)

	
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    for key,value in dt.iteritems():
AttributeError: 'dict' object has no attribute 'iteritems'
>>> dt.iteritems()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    dt.iteritems()
AttributeError: 'dict' object has no attribute 'iteritems'
>>> dt.keys()
dict_keys([1, 2, 3])
>>> dt.iteritems()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    dt.iteritems()
AttributeError: 'dict' object has no attribute 'iteritems'
>>> 
