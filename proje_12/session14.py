#!/usr/bin/env python
# coding: utf-8

# In[1]:


count = 0
while count >=0 :
    print(count)
    count +=1
    if count ==10 :
        break


# In[2]:


count = 0
while count >=0 :
    print(count)
    count +=1
    if count ==10 :
        count = -1


# In[9]:


print("Say : I love you!")


# In[ ]:


list = ("a", "b", 0)
filtered_list = filter( none, list)
print("elemanlar : ")
for i in filtered_list :
    print (i)


# In[14]:


numara1 = (1,3,79)
 
buyuk_sayilar = max(numara1)
kucuk_sayilar = min(numara1)
print("kucuk sayilar sunlardir: ", kucuk_sayilar)
print("buyuk sayilar sunlardir: ", buyuk_sayilar)


# In[20]:


print(round(10.8883))


# In[22]:


def multiply(a, b):
    print(a*b)
multiply(3, 5)


# In[25]:


def motto() :
    print("nasilsin")
motto()


# In[28]:


def add(a, b):
    print(a+b)
add(-7,14)


# In[34]:


def calculator (x, y, opr):
    if opr == "+":
        print(x + y)
    elif opr == "-":
        print(x - y)
    elif opr == "*":
        print(x * y)
    elif opr == "/":
        print(x / y)
calculator(10,2,"+")
    
    
    


# In[35]:


def calculator (x, y, opr):
    if opr == "+":
        return(x + y)
    elif opr == "-":
        return(x - y)
    elif opr == "*":
        return (x * y)
    elif opr == "/":
        return (x / y)
calculator(10,2,"+")


# In[ ]:




