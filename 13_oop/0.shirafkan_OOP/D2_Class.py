print('---- init ----')    

class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def mul(self):
        return self.a * self.b
    
ob1 = Test(2, 3) 
   
print(ob1.a)     # 2
print(ob1.b)     # 3

print(ob1.add()) # 5
print(ob1.mul()) # 6

ob2 = Test(6,1)
x = ob2.add()
print(x)    # 7

print('-------------')

class Book:
    def __init__(self,author, title):
        self.author = author
        self.title = title
        
    def info(self):
       print(self.title + ':' + self.author)
       
x = Book('shirafkan','C++')
x.info()                     # C++:shirafkan

print('-------------')

class Student:
    def __init__(self, name, score=None):
        self.d = {}
        self.d['name'] = name
        self.d['score'] = score
        
    def get_stu(self):
         return self.d

lst = []        

ob1 = Student('mahsa',20)
ob2 = Student('ali',17)

lst.append(ob1.get_stu())
lst.append(ob2.get_stu())

print(lst) # [{'name': 'mahsa', 'score': 20}, {'name': 'ali', 'score': 17}]

print(lst[0]) # {'name': 'mahsa', 'score': 20}

print('-------------')

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return self.r ** 2 * 3.14
    
x = Circle(8)    
print(x.area())   # 200.96

print(isinstance(x, Circle))  # True


print('-------------')

d = dict()
print(type(d))  # <class 'dict'>

a = 2
print(type(a)) # <class 'int'>

print('-------------')

class Counter:
    def __init__(self, x):
        self.x = x
        
    def up(self):
        self.x += 1        
        
    def down(self):
        self.x -= 1                

ob = Counter(4)        
print(ob.x)    # 4
ob.up()
ob.up()
print(ob.x)   # 6
ob.down()
print(ob.x)   # 5

print('-------------')

class C():
    def __init__(self):
        self.s = ''
    
    def get_string(self):
        self.s = input('input: ')
  
    def show(self):
       print(self.s.upper())        
       
#ob = C()       
#ob.get_string() 
#ob.show()

print('-------------')

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

x = Complex(2,4)        
print(x.r)        # 2
print(x.i)        # 4

print('-------------')

class Machine:
    model = 'peugeot'
    
    def __init__(self, t):
        self.t = t

m1 = Machine('206')        
m2 = Machine('207')        

print(m1.model)  # peugeot
print(m2.model)  # peugeot
print(m1.t)      # 206
print(m2.t)      # 207

print('-------------')

class C:
    lst = []
    
    def __init__(self, name):
        self.name = name
        
    def f(self, x):
        self.lst.append(x)         

ob1 = C('A')     
ob2 = C('B')   

ob1.f(1)
ob1.f(2)
ob1.f(3)

print(ob1.lst)   # [1, 2, 3]     
print(ob2.lst)   # [1, 2, 3]   

ob2.f(4)
print(ob1.lst)   # [1, 2, 3, 4]     
print(ob2.lst)   # [1, 2, 3, 4]   
    
print('-------------')

class C:
    def __init__(self, name):
        self.name = name
        self.lst = []
        
    def f(self, x):
        self.lst.append(x)         

ob1 = C('A')     
ob2 = C('B')   

ob1.f(1)
ob1.f(2)
ob1.f(3)

print(ob1.lst)   # [1, 2, 3]     
print(ob2.lst)   # []   

ob2.f(4)
print(ob1.lst)   # [1, 2, 3]     
print(ob2.lst)   # [4]   
 
print('-----')

class Student:
    stream = 'cse'   # class variable
    
    def __init__(self, name , score):
        self.name = name      # instance variable
        self.score = score    # instance variable

# objects of student class
s1 = Student('ali', 19)        
s2 = Student('sara', 18) 

print(s1.name)    # ali    
print(s2.name)    # sara

print(s1.stream)  #cse
print(s2.stream)  #cse 

print(Student.stream)   # cse
# print(Student.name)   # AttributeError

print('-----')

class Dog:
    animal = 'dog'
    
    def __init__(self, b , c):
        self.b = b
        self.c = c

d1 = Dog('pug' , 'brown')        
d2 = Dog('bulldog' , 'black')        

print(d1.animal)   # dog
print(d2.animal)   # dog

print(d1.c)   # brown
print(d2.c)   # black

print('----')    

# private

class Test:
    def __init__(self, a, b):
        self.a = a     # public
        self.__b = b   # private

    def f(self):
        self.__b += 1
        print(self.__b)
    
ob = Test(1, 2)        
print(ob.a)          # 1
#print(ob.__b)       # AttributeError

ob.f()               # 3   

print(ob.__dict__)   # {'a': 1, '_Test__b': 3}
print(ob._Test__b)   # 3     name mangling

ob._Test__b  = 8    
print(ob._Test__b)   # 8  

print('----')  

class S:
    def __init__(self, x):
        self.__a = x
        
    def f(self):
        print(self.__a, end=' ')
        self.__a += 1
        return(self.__a)
        
    def g(self, m):
       print( m + self.f())        
       
ob = S(1) 
print(ob.__dict__)   # {'_S__a': 1}
print(ob.f())        # 1 2
ob.g(5)              # 2 8

print('----')  
        
class AB:
    __x = 3
    
    def show(self):
        print(self.__x)


ob = AB()        
ob.show()        # 3
print(ob._AB__x) # 3

print('----')  

# private method

class ABC:
    def __f(self):  
        print(1)
    
    def g(self):
        return (self.__f())

ob = ABC()    
ob.g()      # 1
# ob.__f()  # AttributeError

ob._ABC__f() # 1

    
    
    
    
    
    
    
    
    
    
    
    

       
    
    
    
    
    
    
    
    
    
    
    
    
    
