Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tpl=(1,2,3)
>>> tpl
(1, 2, 3)
>>> tpl =(1,2,3,[1,2,3])
>>> tpl
(1, 2, 3, [1, 2, 3])
>>> tpl[0]
1
>>> tpl[0]=7
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tpl[0]=7
TypeError: 'tuple' object does not support item assignment
>>> type(tpl)
<class 'tuple'>
>>> type(tpl[0])
<class 'int'>
>>> tpl[10]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    tpl[10]
IndexError: tuple index out of range
>>> li=list(tpl)
>>> li
[1, 2, 3, [1, 2, 3]]
>>> tpl_new=1,2,3
>>> typr(tpl_new)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    typr(tpl_new)
NameError: name 'typr' is not defined
>>> type(tpl_new)
<class 'tuple'>
>>> tpl_new
(1, 2, 3)
>>> # this is called pack
>>> tpl_new1=1,3,5
>>> 3pack
SyntaxError: invalid syntax
>>> # pack
>>> tpl_new1
(1, 3, 5)
>>> a,b,c=tpl_new1
>>> a
1
>>> b
3
>>> c
5
>>> # this is unpack
>>> a,b,c=tpl_new
>>> a
1
>>> b
2
>>> c
3
>>> tpl
(1, 2, 3, [1, 2, 3])
>>> for i in tpl:
	print(i,end=' ' )

	
1 2 3 [1, 2, 3] 
>>> li=[1,2,3,[1,2,3]]
>>> li
[1, 2, 3, [1, 2, 3]]
>>> li[3]
[1, 2, 3]
>>> li[2]
3
>>> type(li[3])
<class 'list'>
>>> tpl
(1, 2, 3, [1, 2, 3])
>>> type(tpl[3])
<class 'list'>
>>> type(tpl)
<class 'tuple'>
>>> 
