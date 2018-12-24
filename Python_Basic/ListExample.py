Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # List exercise
>>> li = ['lamp', 'laptop','phone','pen']
>>> li
['lamp', 'laptop', 'phone', 'pen']
>>> type(li)
<class 'list'>
>>> len(li)
4
>>> li[2]
'phone'
>>> li[90]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    li[90]
IndexError: list index out of range
>>> li[-1]
'pen'
>>> li[-2]
'phone'
>>> li[-3]
'laptop'
>>> l9[-4]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    l9[-4]
NameError: name 'l9' is not defined
>>> li[-4]
'lamp'
>>> li[-5]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    li[-5]
IndexError: list index out of range
>>> li2=['Bangla',12,13.6]
>>> li2
['Bangla', 12, 13.6]
>>> type(li2]
SyntaxError: invalid syntax
>>> type(li[2])
<class 'str'>
>>> type(li2[2])
<class 'float'>
>>> li
['lamp', 'laptop', 'phone', 'pen']
>>> li[0:2]
['lamp', 'laptop']
>>> li[2:4]
['phone', 'pen']
>>> li[-1:]
['pen']
>>> li[0:4:2]
['lamp', 'phone']
>>> li{-1]
SyntaxError: invalid syntax
>>> li[-1]
'pen'
>>> li
['lamp', 'laptop', 'phone', 'pen']
>>> li[2]
'phone'
>>> li[2]='cell phone'
>>> li
['lamp', 'laptop', 'cell phone', 'pen']
>>> li= li + ['apple']
>>> li
['lamp', 'laptop', 'cell phone', 'pen', 'apple']
>>> li
['lamp', 'laptop', 'cell phone', 'pen', 'apple']
>>> li2
['Bangla', 12, 13.6]
>>> li2=li2+[100]
>>> li2
['Bangla', 12, 13.6, 100]
>>> 
