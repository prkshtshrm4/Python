#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[9]:


##Q3
class MyClass:
    "This is my second class"
    a = 10
    def func(self):
        print('Hello')

print(MyClass.a)
print(MyClass.func)
print(MyClass.__doc__)


# In[8]:


##Q4
class Parent(): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Parent"
          
    # Parent show method 
    def show(self): 
        print(self.value) 
          
# Define child class 
class Child(Parent): 
      
    # Constructor 
    def __init__(self): 
        self.value = "Inside Child"
          
    # Child's show method 
    def show(self): 
        print(self.value) 
          
          
# Driver code 
obj1 = Parent() 
obj2 = Child() 
  
obj1.show() 
obj2.show() 


# In[7]:


##Q5
class Class1: 
    def m(self): 
        print("In Class1")  
        
class Class2(Class1): 
    def m(self): 
        print("In Class2") 
  
class Class3(Class1): 
    def m(self): 
         print("In Class3")      
      
class Class4(Class2, Class3): 
    def m(self): 
        print("In Class4")    
  
obj = Class4() 
obj.m() 
  
Class2.m(obj) 
Class3.m(obj) 
Class1.m(obj) 


# In[ ]:




