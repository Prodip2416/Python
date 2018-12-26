Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a= set()
>>> a
set()
>>> type(a)
<class 'set'>
>>> a=set(1,2,3)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a=set(1,2,3)
TypeError: set expected at most 1 arguments, got 3
>>> a=set(1)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    a=set(1)
TypeError: 'int' object is not iterable
>>> tpl=(1,2,3,4,5)
>>> a=set(tpl)
>>> a
{1, 2, 3, 4, 5}
>>> li=[1,2,3,4]
>>> b=set(li)
>>> b
{1, 2, 3, 4}
>>> a
{1, 2, 3, 4, 5}
>>> a&b
{1, 2, 3, 4}
\
>>> a&b
{1, 2, 3, 4}
>>> a|b
{1, 2, 3, 4, 5}
>>> a ^ b
{5}
>>> 8 in a\

    
False
>>> 8 in b
False
>>> 1 in a\]
SyntaxError: unexpected character after line continuation character
>>> 1 in a
True
>>> 1 in b
True
>>> c = set(abcd)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    c = set(abcd)
NameError: name 'abcd' is not defined
>>> c= set('abcd')
>>> c
{'b', 'c', 'd', 'a'}
>>> li=[1,1,2,3,3,4,4,5]
>>> li
[1, 1, 2, 3, 3, 4, 4, 5]
>>> set(li)
{1, 2, 3, 4, 5}
>>> li=list(set(li))
>>> li
[1, 2, 3, 4, 5]
>>> z= set(li)
>>> z
{1, 2, 3, 4, 5}
>>> a= set(1,3,5)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a= set(1,3,5)
TypeError: set expected at most 1 arguments, got 3
>>> li=[1,3,5]
>>> a= set(li)
>>> a
{1, 3, 5}
>>> li=[2,4,6]
>>> b=set(li)
>>> b
{2, 4, 6}
>>> a & b
set()
>>> a| b
{1, 2, 3, 4, 5, 6}
>>> a ^ b
{1, 2, 3, 4, 5, 6}
>>> 
