Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li=[1,2,3,4,5,6,7]
>>> li
[1, 2, 3, 4, 5, 6, 7]
>>> print(li)
[1, 2, 3, 4, 5, 6, 7]
>>> li.reverse()
>>> li
[7, 6, 5, 4, 3, 2, 1]
>>> li.reverse()
>>> li
[1, 2, 3, 4, 5, 6, 7]
>>> li.reverse()
>>> li
[7, 6, 5, 4, 3, 2, 1]
>>> li.sort()
>>> li
[1, 2, 3, 4, 5, 6, 7]
>>> li.append(8)
>>> li
[1, 2, 3, 4, 5, 6, 7, 8]
>>> li.insert(0,0)
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8]
>>> li2=range(10,20)
>>> li2
range(10, 20)
>>> li2
range(10, 20)
>>> li.extend(li2)
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
>>> li.count(0)
1
>>> li.count(90)
0
>>> li.remove(19)
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17, 18]
>>> li.pop()
18
>>> li
[0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17]
>>> li.pop(0)
0
>>> li
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17]
>>> li
[1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15, 16, 17]
>>> li=0*100
>>> li
0
>>> li=[0]*100
>>> li
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>> li1
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    li1
NameError: name 'li1' is not defined
>>> li2
range(10, 20)
>>> li1=li2
>>> li1
range(10, 20)
>>> li2
range(10, 20)
>>> stack = []
>>> styack,append(2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    styack,append(2)
NameError: name 'styack' is not defined
>>> stack.append(2)
>>> stack
[2]
>>> stack.append(3)
>>> stack.append(4)
>>> stack.append(5)
>>> stack.append(7)
>>> stack
[2, 3, 4, 5, 7]
>>> stack,pop()
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    stack,pop()
NameError: name 'pop' is not defined
>>> stack.pop()
7
>>> stack
[2, 3, 4, 5]
>>> li=range(1,21)
>>> li
range(1, 21)
>>> for i in li:\
    if i %2==0:
	
SyntaxError: invalid syntax
>>> even=[]
>>> for i in li:
	if i% 2==0:
		even.append(i)

		
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
>>> odd=[i for iin li if i% 2==1]
SyntaxError: invalid syntax
>>> odd=[i for in li if i% 2==1]
SyntaxError: invalid syntax
>>> odd
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    odd
NameError: name 'odd' is not defined
>>> odd=[i for i in li if i% 2==1]
>>> odd
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
>>> 
