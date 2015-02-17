Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  6 2014, 22:16:31) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 10 + 5
15
>>> 10 / 6
1.6666666666666667
>>> import math
>>> Round 35.5
SyntaxError: invalid syntax
>>> math.floor(35.5)
35
>>> ================================ RESTART ================================
>>> 
writing
swiming
raining
>>> ','.join(['foo','bar'])
'foo,bar'
>>> mystring = 'hello world'
>>> mylist = mystring.split()
>>> print mylist
SyntaxError: Missing parentheses in call to 'print'
>>> print (mylist)
['hello', 'world']
>>> foo = [25, 68, 'bar', 89.45, 789, 'spam', 0, 'last item']
>>> print foo
SyntaxError: Missing parentheses in call to 'print'
>>> print (foo)
[25, 68, 'bar', 89.45, 789, 'spam', 0, 'last item']
>>> foo.last
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    foo.last
AttributeError: 'list' object has no attribute 'last'
>>> print (foo.lst)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print (foo.lst)
AttributeError: 'list' object has no attribute 'lst'
>>> Traceback (most recent call last):
	
SyntaxError: invalid syntax
>>> print (foo[0])
25
>>> print (foo[7])
last item
>>> 
>>> print (foo[:3])
[25, 68, 'bar']
>>> print (foo[2:])
['bar', 89.45, 789, 'spam', 0, 'last item']
>>> print(foo[1:-1])
[68, 'bar', 89.45, 789, 'spam', 0]
>>> bar = foo
>>> print(bar)
[25, 68, 'bar', 89.45, 789, 'spam', 0, 'last item']
>>> foo[0] = 7
>>> print(bsr)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(bsr)
NameError: name 'bsr' is not defined
>>> print(bar)
[7, 68, 'bar', 89.45, 789, 'spam', 0, 'last item']
>>> foo[0] = 25
>>> foo.copy
<built-in method copy of list object at 0x00000000029AC7C8>
>>> bar = foo.copy
>>> print(bar)
<built-in method copy of list object at 0x00000000029AC7C8>
>>> bar.copy(foo)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    bar.copy(foo)
AttributeError: 'builtin_function_or_method' object has no attribute 'copy'
>>> delete bar
SyntaxError: invalid syntax
>>> remove bar
SyntaxError: invalid syntax
>>> bar = null
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    bar = null
NameError: name 'null' is not defined
>>> bar = void
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    bar = void
NameError: name 'void' is not defined
>>> bar = []
>>> print(bar)
[]
>>> bar.copy(foo)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    bar.copy(foo)
TypeError: copy() takes no arguments (1 given)
>>> bar.copy
<built-in method copy of list object at 0x0000000003748808>
>>> foo[0] = 12
>>> foo[0] * 2
24
>>> if ham in foo
SyntaxError: invalid syntax
>>> if 'ham' in foo
SyntaxError: invalid syntax
>>> if ham in foo:
	print(yes)

	
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    if ham in foo:
NameError: name 'ham' is not defined
>>> if 'ham' in foo:
	print('yes')

	
>>> if 'ham' not in foo:
	print('no')

	
no
>>> 
>>> 
>>> foo.count
<built-in method count of list object at 0x00000000029AC7C8>
>>> foo.count
<built-in method count of list object at 0x00000000029AC7C8>
>>> print(foo.count)
<built-in method count of list object at 0x00000000029AC7C8>
>>> print(foo.count())
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print(foo.count())
TypeError: count() takes exactly one argument (0 given)
>>> print(foo.count(x))
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(foo.count(x))
NameError: name 'x' is not defined
>>> print(foo.len)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(foo.len)
AttributeError: 'list' object has no attribute 'len'
>>> len(foo)
8
>>> foo.append(24)
>>> foo.insert(3,'twenty')
>>> foo.index('spam')
6
>>> x = foo.pop
>>> print(x)
<built-in method pop of list object at 0x00000000029AC7C8>
>>> print(foo)
[12, 68, 'bar', 'twenty', 89.45, 789, 'spam', 0, 'last item', 24]
>>> foo.pop
<built-in method pop of list object at 0x00000000029AC7C8>
>>> x = foo.pop()
>>> print(x)
24
>>> sent1 = 'The quick brown fox jumps over the lazy dog'
>>> list1 = sent1.split()
>>> sent2 = ' '.join(list1)
>>> set1 = set(list1)
>>> print(set1)
{'fox', 'jumps', 'lazy', 'brown', 'The', 'quick', 'over', 'the', 'dog'}
>>> set2 = set(sent2.split())
>>> print(set2)
{'fox', 'jumps', 'lazy', 'brown', 'The', 'quick', 'over', 'the', 'dog'}
>>> print(list2[2][2])
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    print(list2[2][2])
NameError: name 'list2' is not defined
>>> print(list1[2][2])
o
>>> for line in open ('C:/Users')
SyntaxError: invalid syntax
>>> for line in open ('C:/Users/panboy/Dropbox/AI2/password.txt',r):
	user, pw = line.split()
	passwd[user]=pw

	
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    for line in open ('C:/Users/panboy/Dropbox/AI2/password.txt',r):
NameError: name 'r' is not defined
>>> for line in open ('C:/Users/panboy/Dropbox/AI2/password.txt','r'):
	user, pw = line.split()
	passwd[user]=pw

	
Traceback (most recent call last):
  File "<pyshell#86>", line 3, in <module>
    passwd[user]=pw
NameError: name 'passwd' is not defined
>>> passwd = {}
>>> for line in open ('C:/Users/panboy/Dropbox/AI2/password.txt','r'):
	user, pw = line.split()
	passwd[user]=pw

	
>>> passwd
{'mike': 'morepassword', 'adam': 'password', 'fred': 'otherpassword'}
>>> 
