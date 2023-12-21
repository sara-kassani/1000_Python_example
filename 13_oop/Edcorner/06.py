"""
1. Create a Container class. Display the value of the module attribute of the Container class to the console.

2. Create an instance of the Container class and assign it to the container variable. Print the type of
container variable to the console.

3. print the _class_ attribute value of the container instance

4. display the type of dictionary attribute _dict_ for the Container class and for the container instance.
"""

class Container:
    pass
#-------------------------------------------
# 1
print(Container.__module__)   ## __main__
#-------------------------------------------
# 2
container= Container()
print(type(container))  ## <class '__main__.Container'>
#-------------------------------------------
# 3
print(container.__class__)  ## <class '__main__.Container'>
#-------------------------------------------
# 4
print(Container.__dict__)   
## {'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Container' objects>, '__weakref__': <attribute '__weakref__' of 'Container' objects>, '__doc__': None}

print(container.__dict__)
## {}


