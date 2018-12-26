Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=raw_input()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    a=raw_input()
NameError: name 'raw_input' is not defined
>>> x=input()
99
>>> x
'99'
>>> type(x)
<class 'str'>
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'x']
>>> dir(_name_)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    dir(_name_)
NameError: name '_name_' is not defined
>>> dir('_name_')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir('_builtins_')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> sqrt(25)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    sqrt(25)
NameError: name 'sqrt' is not defined
>>> import math
>>> math.sqrt(25)
5.0
>>> sqrt(25)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    sqrt(25)
NameError: name 'sqrt' is not defined
>>> def add (n1,n2):
	return n1+n2

>>> add(3,4)
7
>>> def add(n1,n2):
	sum=n1 + n2
	return sum

>>> v=add(2,4)
>>> v
6
>>> def NameCalculate(fname,lname):
	fullName=fname+lname
	return fullName

>>> NameCalculate(Pro,dip)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    NameCalculate(Pro,dip)
NameError: name 'Pro' is not defined
>>> Namcalculate('Pro','dip')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    Namcalculate('Pro','dip')
NameError: name 'Namcalculate' is not defined
>>> nam=NameCalculate('Pro','dip')
>>> nam
'Prodip'
>>> 
