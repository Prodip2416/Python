Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> "Bangladesh"
'Bangladesh'
>>> type("Bangladesh")
<class 'str'>
>>> country = "Bangladesh"
>>> print(country)
Bangladesh
>>> type(country)
<class 'str'>
>>> country = 'Bangldesh"
SyntaxError: EOL while scanning string literal
>>> country= " Bangladesh'
SyntaxError: EOL while scanning string literal
>>> str = "Prodip's Da"
>>> str
"Prodip's Da"
>>> str = 'Prodip's Da'
SyntaxError: invalid syntax
>>> str
"Prodip's Da"
>>> str= "Adam\'s"
>>> str
"Adam's"
>>> str = "Prodip/"s"
SyntaxError: invalid syntax
>>> str = "Prodip\"s"
>>> str
'Prodip"s'
>>> country
'Bangladesh'
>>> country [0]
'B'
>>> country [1]
'a'
>>> len(country)
10
>>> country[0]=y
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    country[0]=y
NameError: name 'y' is not defined
>>> country.find('B')
0
>>> country.find('a')
1
>>> country('m')
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    country('m')
TypeError: 'str' object is not callable
>>> country.find('m')
-1
>>> country.fin('dk')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    country.fin('dk')
AttributeError: 'str' object has no attribute 'fin'
>>> country.find('dk')
-1
>>> country.
SyntaxError: invalid syntax
>>> country.replace('Bangladesh','BANGLADESH')
'BANGLADESH'
>>> coutry
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    coutry
NameError: name 'coutry' is not defined
>>> country
'Bangladesh'
>>> country
'Bangladesh'
>>> country.replace('Bangladesh','bangladesh')
'bangladesh'
>>> country
'Bangladesh'
>>> country
'Bangladesh'
>>> country.replace('Bangladesh','bangladesh1')
'bangladesh1'
>>> country
'Bangladesh'
>>> str = 'bcd '
>>> str
'bcd '
>>> str.strip()
'bcd'
>>> str2=str.strip()
>>> str2
'bcd'
>>> country
'Bangladesh'
>>> country1=counrty.replace('Bangladesh','bangla')
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    country1=counrty.replace('Bangladesh','bangla')
NameError: name 'counrty' is not defined
>>> country1=country.replace('Bangladesh','bangla')
>>> country1
'bangla'
>>> str = ' a b c d'
>>> str
' a b c d'
>>> str = ' a b c d '
>>> str
' a b c d '
>>> str1=str.strip()
>>> str1
'a b c d'
>>> str
' a b c d '
>>> str.lstrip()
'a b c d '
>>> str.rstrip()
' a b c d'
>>> str='Prodip'
>>> str.lower()
'prodip'
>>> str.upper()
'PRODIP'
>>> str
'Prodip'
>>> str1= 'pro'
>>> str2= 'Dip'
>>> str1,str2
('pro', 'Dip')
>>> str1,str2=str2,str1
>>> str1,str2
('Dip', 'pro')
>>> #Revarse a string.......
>>> str1
'Dip'
>>> str1[::-1]
'piD'
>>> str2= 'Dip'
