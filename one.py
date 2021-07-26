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
print(s1 + " " + s2)


# 4. Given this nested list, use indexing to grab the word "hello"

# In[19]:


a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2])


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


print(color_list_3)


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





# 9. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn

# In[1]:


n = int(input())
value = n + ((n*10)+n) +((n*100)+(n*10)+n)
value


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


# 10. Write a python program to take input from console in following fashion
# 23 54 12#98 3 17
# and generate the corresponding two list having integers inside (not string)

# In[ ]:


str1 = input()
a = str1.index("#")
a1 = str1[0:a].split()
a2 = str1[a+1:].split()
list1 = [eval(i) for i in a1]
list2 = [eval(i) for i in a2]
print(list1)
print(list2)





# In[ ]:
# 11. Write a program that accepts a comma separated sequence of words as input and 
# prints the words in a comma-separated sequence after sorting them alphabetically.

a = input("Enter the string seperated with comma: ")
b = a.split(",")
b.sort()
",".join(b)
print(b)





# In[ ]:
# 14. Write a python function which creates a new dictionary of students from a given 
# Dataset of various subject to a specific subject or topic only.

d = {'Name': ['Akash', 'Soniya', 'Vishakha' , 'Akshay', 'Rahul', 'Vikas'],
'Subject': ['Python', 'Java', 'Python', 'C', 'Python', 'Java'],
'Ratings': [8.4, 7.8, 8, 9, 8.2, 5.6]}

i = input()
list1 = list(zip(d['Name'],d['Subject'],d['Ratings']))
list2 = []
for j in range(0,len(list1)):
    if (list1[j][0] == i) or (list1[j][1] == i) or (list1[j][2] == i):
        list2.append(list1[j])
x = list(zip(*list2))
new_data["Name"] = list(x[0])
new_data["Subject"] = list(x[1])
new_data["Ratings"] = list(x[2])
print(new_data)






# In[ ]:
# 15. Define a class with a generator which can iterate the numbers, which are divisible 
# by 7, between a given range 0 and n.

n = eval(input())
number_divisible_by_7 = (i for i in range(0,n+1) if i%7==0)
print(list(number_divisible_by_7))








# In[ ]:

# 16. . A robot moves in a plane starting from the original point (0,0). The robot can 
# move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot 
# movement is shown as the following:
# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2
# The numbers after the direction are steps. Please write a program to compute the 
# distance from current position after a sequence of movement and original point. 
# If the distance is a float, then just print the nearest integer.
import math
x = 0
y = 0
UP = eval(input("UP: "))
DOWN = eval(input("DOWN: "))
LEFT = eval(input("LEFT: "))
RIGHT = eval(input("RIGHT: "))
x = x + UP - DOWN
y = y + RIGHT - LEFT
distance = int(math.sqrt(x**2 + y**2))
print(distance)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




