#!/usr/bin/env python
# coding: utf-8

# In[3]:


#1

class triangle:
    a=9
    b=4
    c=7
    st="Triangle created"
    
    def create_triangle(self):
        print(self.st)
    def print_side(self):
        print(self.a)
        print(self.b)
        print(self.c)

t=triangle()
t.print_side()
t.create_triangle()


# In[4]:


#2
class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()


# In[5]:


#3
class rectangle():
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length
a=int(input("Enter length of rectangle: "))
b=int(input("Enter breadth of rectangle: "))
obj=rectangle(a,b)
print("Area of rectangle:",obj.area())
 
print()


# In[6]:



#4
import math
class circle():
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    def perimeter(self):
        return 2*math.pi*self.radius
 
r=int(input("Enter radius of circle: "))
obj=circle(r)
print("Area of circle:",round(obj.area(),2))
print("Perimeter of circle:",round(obj.perimeter(),2))


# In[7]:


#5
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




