#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Palindrome number
n = int(input("Enter a number: "))
temp=n
rev=0
while temp>0:
    last=temp%10
    temp=temp//10
    rev=rev*10+last
if rev==n:
    print("number is palindrome")
else:
    print("number is not palindrome")


# In[4]:


#sum of digits of number
n=int(input("Enter a number:"))
temp=n
sum=0
while temp>0:
    last=temp%10
    sum=sum+last
    temp=temp//10
print(f"The sum of digits of {n} is {sum}")


# In[5]:


n=int(input("Enter a number:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[6]:


n=int(input("Enter a number:"))
k=1
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(k,end=" ")
        k=k+1
    print()


# In[7]:


#Armstrong
n=int(input("Enter a number:"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if sum==n:
    print("the no. is armstrong")
else:
    print("the no. is not armstrong")


# In[8]:


#individual digits
n=int(input("Enter a number:"))
no=str(n)
for i in no:
    print(i,end=" ")


# In[ ]:




