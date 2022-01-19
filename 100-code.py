#!/usr/bin/env python
# coding: utf-8

# In[5]:


a=[]
for i in range(2000, 3200):
    if (i%7==0) and (i%5!=0):
        a.append(str(i))

print(','.join(a))


# In[6]:


def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)

x=int(input())
print(factorial(x))


# In[10]:


n = int(input())
a = dict()
for i in range(1,n+1):
    a[i] = i * i

print(a)


# In[12]:


values = input()
a = values.split(',')
b = tuple(a)
print(a)
print(b)


# In[20]:


class InputOutputString(object):
    def __init__(n):
        n.s = ""

    def getString(n):
        n.s = input()
    
    def printString(n):
        print(n.s.upper())

strObj = InputOutputString()
strObj.getString()
strObj.printString()


# In[21]:


import math
c = 50
h = 30
value = []
items = [x for x in input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2 * c * float(d)/h)))))

print(','.join(value))


# In[22]:


input_string = input()
dimensions = [int(x) for x in input_string.split(',')]

rownumber = dimensions[0]
colnumber = dimensions[1]
multilist = [[0 for col in range(colnumber)] for row in range(rownumber)]

for row in range(rownumber):
    for col in range(colnumber):
        multilist[row][col] = row * col

print(multilist)


# In[24]:


names = [x for x in input().split(',')]
names.sort()
print(','.join(names))


# In[28]:


lines = []
while True:
    n = input()
    if n:
        lines.append(n.upper())
    else:
        break;

for sentence in lines:
    print(sentence)


# In[30]:


n = input()
words = [word for word in n.split(" ")]

print(" ".join(sorted(list(set(words)))))


# In[1]:


value = []
items=[x for x in input().split(',')]
for p in items:
    intp = int(p, 2)
    if not intp%5:
        value.append(p)

print(','.join(value))


# In[2]:


values = []
for i in range(1000, 3001):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0) and (int(s[3])%2==0):
        values.append(s)
print(",".join(values))


# In[4]:


s = input()
d={"DIGITS":0, "LETTERS":0}
for c in s:
    if c.isdigit():
        d["DIGITS"]+=1
    elif c.isalpha():
        d["LETTERS"]+=1
    else:
        pass
print("LETTERS", d["LETTERS"])
print("DIGITS", d["DIGITS"])


# In[5]:


s = input()
d={"UPPER CASE":0, "LOWER CASE":0}
for c in s:
    if c.isupper():
        d["UPPER CASE"]+=1
    elif c.islower():
        d["LOWER CASE"]+=1
    else:
        pass
print("UPPER CASE", d["UPPER CASE"])
print("LOWER CASE", d["LOWER CASE"])


# In[7]:


a = input()
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )
print(n1+n2+n3+n4)


# In[8]:


values = input()
numbers = [x for x in values.split(",") if int(x)%2!=0]
print(",".join(numbers))


# In[13]:


netAmount = 0
while True:
    s = input()
    if not s:
        break
    values = s.split(" ")
    operation = values[0]
    amount = int(values[1])
    if operation=="D":
        netAmount+=amount
    elif operation=="W":
        netAmount-=amount
    else:
        pass
print(netAmount)


# In[14]:


import re
value = []
items=[x for x in input().split(',')]
for p in items:
    if len(p)<6 or len(p)>12:
        continue
    else:
        pass
    if not re.search("[a-z]",p):
        continue
    elif not re.search("[0-9]",p):
        continue
    elif not re.search("[A-Z]",p):
        continue
    elif not re.search("[$#@]",p):
        continue
    elif re.search("\s",p):
        continue
    else:
        pass
    value.append(p)
print(",".join(value))


# In[32]:


a = []


a.append(["Tom", 19, 80])
a.append(["John",  20, 90])
a.append(["Jony", 17, 91])
a.append(["Jony", 17, 93])   

import operator
a.sort(key=operator.itemgetter(0,1,2))    


print(a)


# In[ ]:


def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

for i in reversed(100):
    print(i)


# In[6]:


import math
pos = [0,0]
while True:
    s = input()
    if not s:
        break
    movement = s.split(" ")
    direction = movement[0]
    steps = int(movement[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass

print(int(round(math.sqrt(pos[1]**2+pos[0]**2))))


# In[ ]:


freq = {}   # frequency of words in text
line = input()
for word in line.split():
    freq[word] = freq.get(word,0)+1

words = freq.keys()
words.sort()

for w in words:
    print("%s:%d" % (w,freq[w]))


# In[41]:


def square(num):
    return num ** 2

print(square(2))
print(square(3))


# In[42]:


print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)

def square(num):
    '''Return the square value of the input number.
    
    The input number must be integer.
    '''
    return num ** 2

print(square(2))
print(square.__doc__)


# In[43]:


class Person:
    # Define the class parameter "name"
    name = "Person"
    
    def __init__(self, name = None):
        # self.name is the instance parameter
        self.name = name

jeffrey = Person("Jeffrey")
print("%s name is %s" % (Person.name, jeffrey.name))

nico = Person()
nico.name = "Nico"
print("%s name is %s" % (Person.name, nico.name))


# In[44]:


def SumFunction(number1, number2):
	return number1+number2

print(SumFunction(1,2))


# In[45]:


def printValue(n):
    print(str(n))

printValue(3)


# In[46]:


def printValue(n):
    print(str(n))

printValue(3)


# In[47]:


def printValue(s1,s2):
    print(int(s1)+int(s2))

printValue("3","4")


# In[48]:


def printValue(s1,s2):
    print(s1+s2)

printValue("3","4") #34


# In[49]:


def printValue(s1,s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2:
        print(s1)
    elif len2>len1:
        print(s2)
    else:
        print(s1)
        print(s2)
        
printValue("one","three")


# In[51]:


def checkValue(n):
    if n%2 == 0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
checkValue(7)


# In[52]:


def printDict():
    d=dict()
    d[1]=1
    d[2]=2**2
    d[3]=3**2
    print(d)
        
printDict()


# In[53]:


def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    print(d)

printDict()


# In[54]:


def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for (k,v) in d.items():	
        print(v)

printDict()


# In[55]:


def printDict():
    d=dict()
    for i in range(1,21):
        d[i]=i**2
    for k in d.keys():	
        print(k)

printDict()


# In[56]:


def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li)

printList()


# In[57]:


def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[:5])

printList()


# In[58]:


def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(li[-5:])

printList()


# In[67]:


def printList():
    li=list()
    for i in range(1,21):
        li.append(i**2)
        print (li[5:])
    

printList()


# In[68]:


def printTuple():
    li=list()
    for i in range(1,21):
        li.append(i**2)
    print(tuple(li))

printTuple()


# In[69]:


tp=(1,2,3,4,5,6,7,8,9,10)
tp1=tp[:5]
tp2=tp[5:]
print(tp1)
print(tp2)


# In[71]:


tp=(1,2,3,4,5,6,7,8,9,10)
li=list()
for i in tp:
    if tp[i]%2==0:
            li.append(tp[i])

tp2=tuple(li)
print(tp2)


# In[78]:


s
if s=="yes" or s=="YES" or s=="Yes":
    print("Yes")
else:
    print("No")


# In[12]:


li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = lambda x: x%2==0, li
print(evenNumbers)


# In[13]:


li = [1,2,3,4,5,6,7,8,9,10]
squaredNumbers = map(lambda x: x**2, li)
print(squaredNumbers)


# In[14]:


li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = map(lambda x: x**2, filter(lambda x: x%2==0, li))
print(evenNumbers)


# In[15]:


evenNumbers = filter(lambda x: x%2==0, range(1,21))
print(evenNumbers)


# In[16]:


squaredNumbers = map(lambda x: x**2, range(1,21))
print(squaredNumbers)


# In[17]:


class American(object):
    @staticmethod
    def printNationality():
        print("America")

anAmerican = American()
anAmerican.printNationality()
American.printNationality()


# In[18]:


class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)


# In[21]:


class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius**2*3.14
    aCircle = Circle(2)
    print aCircle.area()


# In[22]:


class Rectangle(object):
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def area(self):
        return self.length*self.width

aRectangle = Rectangle(2,10)
print(aRectangle.area())


# In[23]:


class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, l):
        Shape.__init__(self)
        self.length = l

    def area(self):
        return self.length*self.length

aSquare= Square(3)
print(aSquare.area())


# In[27]:


def throws():
    return 5/0
try:
    throws()
except ZeroDivisionError:
    print("division by zero!")
except Exception:
    print('Caught an exception')
finally:
    print('In finally block for cleanup')


# In[35]:


import re
emailAddress = input()
pat2 = "(\w+)@((\w+\.)+(com))"
r2 = re.match(pat2,emailAddress)
print(r2.group(1))


# In[36]:


import re
emailAddress = input()
pat2 = "(\w+)@(\w+)\.(com)"
r2 = re.match(pat2,emailAddress)
print(r2.group(2))


# In[37]:


import re
s = input()
print(re.findall("\d+",s))


# In[38]:


unicodeString = u"hello world!"
print(unicodeString)


# In[40]:


s = input()
u = unicode( s ,"utf-8")
print(u)


# In[42]:


# -*- coding: utf-8 -*-


# In[43]:


n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)


# In[44]:


def f(n):
    if n==0:
        return 0
    else:
        return f(n-1)+100

n=int(input())
print(f(n))


# In[45]:


def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
print(f(n))


# In[46]:


def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(input())
values = [str(f(x)) for x in range(0, n+1)]
print(",".join(values))


# In[47]:


def EvenGenerator(n):
    i=0
    while i<=n:
        if i%2==0:
            yield i
        i+=1


n=int(input())
values = []
for i in EvenGenerator(n):
    values.append(str(i))

print(",".join(values))


# In[48]:


def NumGenerator(n):
    for i in range(n+1):
        if i%5==0 and i%7==0:
            yield i

n=int(input())
values = []
for i in NumGenerator(n):
    values.append(str(i))

print(",".join(values))


# In[50]:


expression = input()
print(eval(expression))


# In[51]:


import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))


# In[52]:


import math
def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index

li=[2,5,7,9,11,17,222]
print(bin_search(li,11))
print(bin_search(li,12))


# In[53]:


import random
print(random.random()*100)


# In[54]:


import random
print(random.random()*100-5)


# In[55]:


import random
print(random.choice([i for i in range(11) if i%2==0]))


# In[56]:


import random
print(random.choice([i for i in range(201) if i%5==0 and i%7==0]))


# In[57]:


import random
print(random.sample(range(100), 5))


# In[58]:


import random
print(random.sample([i for i in range(100,201) if i%2==0], 5))


# In[59]:


import random
print(random.sample([i for i in range(1,1001) if i%5==0 and i%7==0], 5))


# In[60]:


import random
print(random.randrange(7,16))


# In[61]:


import zlib
s = b'hello world!hello world!hello world!hello world!'
t = zlib.compress(s)
print(t)
print(zlib.decompress(t))


# In[62]:


from timeit import Timer
t = Timer("for i in range(100):1+1")
print(t.timeit())


# In[63]:


li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i%2!=0]
print(li)


# In[64]:


li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print(li)


# In[65]:


li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)


# In[66]:


import itertools
print(list(itertools.permutations([1,2,3])))


# In[67]:


s=input()
s = s[::2]
print(s)


# In[69]:


s=input()
s = s[::-1]
print(s)


# In[ ]:




