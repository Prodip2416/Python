Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> i = 1
>>> while i<=10:
	print(i)
	i= i+ 1

	
1
2
3
4
5
6
7
8
9
10
>>> while i <=10:
	print(i)
	i++
	
SyntaxError: invalid syntax
>>> while i <=10:
	print(i)
	i +=1

	
>>> fib_1=0
>>> fib_2=1
>>> while fib_2 <20:
	print(fib_2)
	fib_1,fib_2=fib_2,fib_1+fib_2

	
1
1
2
3
5
8
13
>>> while fib_2 <20:
	print(fib_2),fib_1,fib_2=fib_2,fib_1+fib_2
	
SyntaxError: can't assign to function call
>>> while fib_2 <20:
	print(fib_2),
	fib_1,fib_2=fib_2,fib_1+fib_2

	
>>> while fib_2 <20:
	print(fib_2),
	fib_1,fib_2=fib_2,
	fib_1+fib_2

	
>>> while i<=10:
	print(i),
	i= i+1

	
>>> while i<=10:
	print(i, sep=' ',end='',flush=True)
	i = i+ 1

	
>>> while i<=10:
	print(i)


	
	i= i+1

	
>>> 
>>> while i<=10:
	print(i)
	i= i+1

	
>>> while i <=10:
	print(i)
	i = i+ 1

	
>>> i
11
>>> i = 1
>>> 
>>> i
1
>>> while i<=10:
	print(i, sep=' ',end='',flush=True)
	i = i+ 1

	
12345678910
>>> while i<=10:
	print(i),
	i= i+1

	
>>> i
11
>>> i=1
>>> i
1
>>> while i <=10:
	print(i),
	i = i+1

	
1
(None,)
2
(None,)
3
(None,)
4
(None,)
5
(None,)
6
(None,)
7
(None,)
8
(None,)
9
(None,)
10
(None,)
>>> i
11
>>> i=1
>>> while i<=10:
	print(i, sep='  ',end='',flush=True)
	i = i+ 1

	
12345678910
>>> i=1
>>> while i <=10:
	print(i,sep='',end='',flush=True)
	i=i+1

	
12345678910
>>> i=1
>>> while i<=10:
	print(i,sep='',end=' ',flush=True)
	i= i+1

	
1 2 3 4 5 6 7 8 9 10 
>>> i=1
>>> while i<=10:
	print(i,end=',')
	i=i+1

	
1,2,3,4,5,6,7,8,9,10,
>>> i=1
>>> while i<=10:
	print(i\n)
	
SyntaxError: unexpected character after line continuation character
>>> i=i+1
>>> i
2
>>> while i<=10:
	print(i,end=' ')
	i=i+1

	
2 3 4 5 6 7 8 9 10 
>>> i=1
>>> while i<=10:
	if i%2==0:
		print(i)

		

=============================== RESTART: Shell ===============================
>>> i
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    i
NameError: name 'i' is not defined
>>> i=1
>>> i
1
>>> vowels =['a','e','i','o','u']
>>> for ch in vowels:
	print(ch)

	
a
e
i
o
u
>>> for i in range(10):
	print(i,end=' ')

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(20):
	print(i,end=' ')
	if i>10:
		break

	
0 1 2 3 4 5 6 7 8 9 10 11 
>>> i=1
>>> while i<=10:
	print(i,end=' ')
	i= i+1
	if i>5:
		break

	
1 2 3 4 5 
>>> i=1
>>> while i<=10:
	if i% 2==0:
		print(i,end=' ' )
		continue

	

=============================== RESTART: Shell ===============================
>>> i=1
>>> while i<=10:
	print(i,end=' ')
	if i % 2==0:
		print(i)
		i=i+1

		
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
=============================== RESTART: Shell ===============================
>>> i=1
>>> for i in range(5,100)
SyntaxError: invalid syntax
>>> for i in range(5,120):
	print(i,end= ' \')
	      
SyntaxError: EOL while scanning string literal
>>> for i in range(5,20):
	      print(i)

	      
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
>>> for i in range(5,20):
	      print(i,end=' ')

	      
5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 
>>> for i in range(7,30):
	      if i>15:
	      continue
	      
SyntaxError: expected an indented block
>>> for i in range(7,30):
	      if i>15:
	      continue
	      
SyntaxError: expected an indented block
>>> for i in range(7,30):
	      print(i,end=' ')
	      if i>15:
	      continue
	      
SyntaxError: expected an indented block
>>> for i in range(20):
	      print(i,end=' ')
	      if i>5:
	      continue
	      
SyntaxError: expected an indented block
>>> for i in range(20):
	      print(i,end=' ')
	      if i>5:
	      break
	      
SyntaxError: expected an indented block
>>> for i in range(10):
	      print(i)

	      
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10):
	      print(i,end=' ')
	      if i>5:
	      break
	      
SyntaxError: expected an indented block
>>> for i in range(20):
	print(i,end=' ')
	if i>10:
		break

	      
0 1 2 3 4 5 6 7 8 9 10 11 
>>> for i in range(5,20):
	      print(i,end=' ')
	      if i >15:
	               break

	      
5 6 7 8 9 10 11 12 13 14 15 16 
>>> for i in range (20):
	      if i% 2 ==0:
	                  print(i,end= ' ')

	      
0 2 4 6 8 10 12 14 16 18 
>>> for i in range(20):
	      if i>10:
	             print(i,end= ' ')

	      
11 12 13 14 15 16 17 18 19 
>>> i=1
	      
>>> i
	      
1
>>> while i<=10:
	      if i% 2==0:
		       print(i,end=' ')

	      

=============================== RESTART: Shell ===============================
>>> 1
	      
1
>>> while i <=10:
            print(i)
	      i=i+i
	      
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> while i<=10:
	      print(i)
	      i=i+1
	      if i>6:
	      break
	      
SyntaxError: expected an indented block
>>> while i<=10:
	      print(i)
	      i=i+1
	      if i>6:
		      break

	      
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    while i<=10:
NameError: name 'i' is not defined
>>> 
	      
>>> i
	      
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    i
NameError: name 'i' is not defined
>>> i=1
	      
>>> while i<=10:
	      print(i)
	      i=i+1
	      if i>6:
		      break

1
2
3
4
5
6
>>> i=1
	      
>>> while i<=10:
	     
	      i=i+1
	      if i>6:
		      break
	       print(i)
	      
SyntaxError: unindent does not match any outer indentation level
>>> i
	      
1
>>> while i<=10:
	      if i>6:
		      break
	      print(i,end=' ')
	      i=i+1

	      
1 2 3 4 5 6 
>>> print(', '.join([str(i) for i in range(10)]))
	      
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
>>> 
