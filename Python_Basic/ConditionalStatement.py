Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> true
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> True
True
>>> False
False
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
>>> bool(True)
True
>>> bool(False)
False
>>> bool(10*0)
False
>>> bool(0.000)
False
>>> bool(0.00001)
True
>>> bool(' ')
True
>>> bool('Prodip')
True
>>> bool('')
False
>>> a= True
>>> a
True
>>> not a
False
>>> b= False
>>> b
False
>>> not b
True
>>> a and b
False
>>> a or b
True
>>> li = [1,2,3,4,5,6]
>>> li in 10
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    li in 10
TypeError: argument of type 'int' is not iterable
>>> 10 in li
False
>>> 3in li
True
>>> 4 in li
True
>>> f in li
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    f in li
NameError: name 'f' is not defined
>>> a=1
>>> b=2
>>> c=3
>>> if a>0
SyntaxError: invalid syntax
>>> if a>0:
	print 'a positive'
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('a positive')?
>>> if b>0:\
    print('b positive')

    
b positive
>>> b>a
True
>>> c<b
False
>>> if a<0:
	print('a negative')
	else:
		
SyntaxError: invalid syntax
>>> if a<0:
	print('a negative')
	else:
		
SyntaxError: invalid syntax
>>> if a<0:
	print('a negative')
	else:print('a positive')
	
SyntaxError: invalid syntax
>>> a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
SyntaxError: multiple statements found while compiling a single statement
>>> a=1
>>> b=2
>>> if a>b:
	print('a is greater than b')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if a>0:
	print('wdwe')
	elif a==0:
		
SyntaxError: invalid syntax
>>> if a>0:
	print ('jjjj')

	
jjjj
>>> if a> 100:
	print('adsa')
	else
	
SyntaxError: invalid syntax
>>> a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else
print("a is greater than b")
SyntaxError: multiple statements found while compiling a single statement
>>> if a> 100:
	print('adsa')
	else:
		
SyntaxError: invalid syntax
>>> if a > 10:
	print('asds')
	else: print('works')
	
SyntaxError: invalid syntax
>>> if a == '1':
        print('1a')
    elif a == '2':
        print('2a')
    else:
        print('3a')
        
SyntaxError: unindent does not match any outer indentation level
>>> a
1
>>> b
2
>>> if a>10:
	print('abcd')
	else:
		
SyntaxError: invalid syntax
>>> if a>10:
	print('abcd')
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if a<10:
	print('scsd')
	else:
		
SyntaxError: invalid syntax
>>> a=10
>>> a
10
>>> if a< 5
SyntaxError: invalid syntax
>>> if a < 5:
	print('abc')

	
>>> 
>>> if a < 5:
	print('abc')
	else: print('bcz')
	
SyntaxError: invalid syntax
>>> if a < 5:
	print("abc")
    else:
	    
SyntaxError: unindent does not match any outer indentation level
>>> if(12>10):
   print(1)
   else :
    print(2)
    
SyntaxError: invalid syntax
>>> if 12>10 :
  print(1)
else :
   print(2)

   
1
>>> if a > 100:
   print('abc')
   else :
	   
SyntaxError: invalid syntax
>>> if a > 100:
	print('abc')
else :
	print('bcd')

	
bcd
>>> a= 5
>>> a
5
>>> b= 3
>>> b
3
>>> if a> 10:
	print('a is greater than 10')
else :\
     print('a is less than 10')

a is less than 10
>>> if a==0:
	print('a is zero')
elif a >10:
	print('a is greater than 10')
else:
	print('a is less than 10')

	
a is less than 10
>>> a
5
>>> if a <3:
	print('a is less than 3')
elif a==0:
	print('a is zero')
else:
	print('a is 3')

	
a is 3
>>> vowels=[a,e,i,o,u]
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    vowels=[a,e,i,o,u]
NameError: name 'e' is not defined
>>> vowels=['a','e','i','o','u']
>>> x= 'z'
>>> if x in vowels:
	print("vowels")
else :
	print("Consonent")

	
Consonent
>>> x in vowels
False
>>> 
>>> 
>>> 
>>> # Some Exercise...........
>>> 
>>> 
>>> a=3
>>> b=5
>>> c=7
>>> if a>b
SyntaxError: invalid syntax
>>> if a>b:
	print('b is greater than a')
elif a==c:
	print('b is greater than a and c')
else
SyntaxError: invalid syntax
>>> if a>b:
	print('b is greater than a')
elif a==c:
	print('b is greater than a and c')
elif c> a:
	print('c is grteater than a)
	      
SyntaxError: EOL while scanning string literal
>>> if a>b:
	print('b is greater than a')
elif a==c:
	print('b is greater than a and c')
elif c> a:
	print('c is grteater than a')
else:
	      print('c is greater than a and b')

	      
c is grteater than a
>>> 
	      
>>> 
	      
>>> a= 10
	      
>>> a % 2 == 0
	      
True
>>> if a % 2 == 1:
	      print('Odd')
else :
	      print('Even')

	      
Even
>>> 
