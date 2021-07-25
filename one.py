#!/usr/bin/env python
# coding: utf-8

# # Q.1 Perform following on Python Shell Window

# In[1]:


5**9


# In[2]:


3//2


# In[3]:


7//3


# In[4]:


7/3


# In[5]:


6==6


# In[8]:


a=20
a += 30
a %= 3
print(a)


# In[9]:


True*False


# In[10]:


True & False


# In[11]:


((6>3) and (7<4) or (18==3)) and (9>3)


# In[12]:


True is False


# In[13]:


False in 'False'


# In[14]:


((True == False) or (False > True)) and (False <= True)


# 3. Try to get following output from two python strings

# In[18]:


s1 = "Nice to have it"
s2 = "here"
s1 + " " + s2


# 4. Given this nested list, use indexing to grab the word "hello"

# In[19]:


a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
a[3][1][2]


# 5. Try to insert above strings s1 and s2 in the list ‘a’ mentioned in que 4, in the
# beginning and end of it respectively

# In[21]:


a.insert(0,s1)


# In[33]:


a += [s2]


# In[35]:


print(a)


# 6. Write a Python program to print all even numbers from a given numbers list in
# the same order and stop the printing if any numbers that come after 237 in the
# sequence.

# In[37]:


numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949,
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445,
742, 717, 958,743, 527]


# In[74]:


for i in numbers:
    if i!=237:
        if i%2== 0:
            print(i)
    else:
        break
  
            
    


# 7. Write a Python program to print out a set containing all the colours from
# color_list_1 which are not present in color_list_2. 

# In[93]:


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])


# In[94]:


color_list_3 = set(color_list_1.difference(color_list_2))


# In[95]:


color_list_3


# 8. WAP to find if the given input string is Pangram or not
# 

# In[2]:


str1 = input("Enter The string: ")
str2 = str1.lower()
str3 = set(str2)
pangram = [i for i in str3 if ord(i) in range(ord('a'), ord('z')+1)]
if len(pangram) ==26:
    print("Pangram")
else:
    print("Not Pangram") 


# 12. Write a Python function to find the name of person obtained highest marks in
# exam from given dictionary
# 

# In[22]:


d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],
'Marks': [57,87,67,79]}
a = d['Student']
b = d['Marks']
c = max(b)
d = b.index(c)
print(a[d])





# In[14]:


help(c.fromkeys)


# In[ ]:





# 13.  13. Write a program that accepts a sentence and calculate the number of letters and digits.
# 

# In[3]:


x = input("Enter the string for calculation: ")
letters = 0
digits = 0
for i in x:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1
print("LETTERS",letters)
print("DIGITS",digits)


# In[ ]:




