Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(10):
	if i%2==0:
		print(i)
		break

	
0
>>> for i in range(20):
	if i>10:
		break
	else
	
SyntaxError: invalid syntax
>>> for i in range(20):
	if i>10:
		break
	else:
		print(i,end=' ')

		
0 1 2 3 4 5 6 7 8 9 10 
>>> i =5
>>> if i%2==0:
	print('Even')
else:
	print('Odd')

	
Odd
>>> for i in range(20):
	if i%2==0:
		print(i,end=' ')
	else:
		continue

	
0 2 4 6 8 10 12 14 16 18 
>>> i=1
>>> while i<=20:
	if i%2==0:
		print(i,end=' ')
	else:
		continue

	

=============================== RESTART: Shell ===============================
>>> for i in range(20):
	if i% ==1:
		
SyntaxError: invalid syntax
>>> for i in range(20):
	if i % 2==1:
		print(i,end=' ' )
	else:
		continue

	
1 3 5 7 9 11 13 15 17 19 
>>> for i in range(20):
	if i % 2==1:
		print(i)
	else:
		continue

	
1
3
5
7
9
11
13
15
17
19
>>> 
