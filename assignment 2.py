#!/usr/bin/env python
# coding: utf-8

# # Question 1

# In[11]:


import re


# In[10]:


text= 'Python Exercises, PHP exercises.'
print(re.sub("[ ,.]", ":", text))


# # Question 2

# In[20]:


re.findall("[ae]\w+", text)


# # Question 3

# In[ ]:


import re

def find_words(input_string):
    pattern = re.compile(r'\b\w{4,}\b')
    words = pattern.findall(input_string)
    return words


# # Question 4

# In[ ]:


import re
def find_words(input_string):
    pattern = re.compile(r'\b\w{3,5}\b')
    words = pattern.findall(input_string)
    return word


# # Question 5

# In[ ]:


import re

def remove_parentheses(["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]):
    pattern = re.compile(r'\s*\(.*?\)')
    new_list = [pattern.sub('', i) for i in input_list]
    return new_list


# # Question 6

# In[ ]:


import re

def remove_parentheses_from_file(["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]):
    pattern = re.compile(r'\s*\(.*?\)')
    with open(file_path, 'r') as file:
        lines = file.readlines()
    new_lines = [pattern.sub('', line) for line in lines]
    with open(file_path, 'w') as file:
        file.writelines(new_lines)


# # Question 7

# In[ ]:


import re
text_1=“ImportanceOfRegularExpressionsInPython”
print(re.findall('[A-Z][^A-Z]*', text_1)


# # Question 8

# In[ ]:


import re
def insert_spaces(“RegularExpression1IsAn2ImportantTopic3InPython"):
    return re.sub(r'(\d)([A-Z])', r'\1 \2', input_string


# # Question 9

# In[ ]:


import re
def insert_spaces(“RegularExpression1IsAn2ImportantTopic3InPython"):
    return re.sub(r'(\d|\w)([A-Z])', r'\1 \2', input_string)


# # Question 10

# In[ ]:


texts=- Hello my name is Data Science and my email address is xyz@domain.com and alternate email address is xyz.abc@sdomain.domain.com
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
print(re.findall(pattern,texts))


# # Question 11

# In[ ]:


print(re.matchr('^[a-zA-Z0-9_]+$'),text)


# # Question 12

# In[ ]:


def check_starting_number(string, number):
  if string.startswith(str(number)):
  return True
  else:
  return False


# # Question 13

# In[ ]:


import re
ip = "180.09.094.226"
string = re.sub('\.[0]*', '.', ip)
print(re.sub('\.[0]*', '.', ip))


# # Question 14

# In[ ]:


import re
text = "On August 15th 1947 that India was declared independent from British colonialism, and the reins of control were handed over to the leaders of the Country’."
pattern = r'\b([A-Z][a-z]+) (\d{1,2})(st|nd|rd|th)? (\d{4})\b'
result = re.findall(pattern, text)


# # Question 15

# In[5]:


import re
text='The quick brown fox jumps over the lazy dog.'
print(re.search("['fox','dog']",text))


# # Question 16

# In[2]:


import re
text = 'The quick brown fox jumps over the lazy dog.'
print(re.search("fox",text))


# # Question 17

# In[6]:


import re 
text='Python exercises, PHP exercises, C# exercises'
print(re.findall('exercises',text))


# # Question 18

# In[8]:


import re 
text='Python exercises, PHP exercises, C# exercises'
pattern = 'exercises'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print(f'Found "{text[s:e]}" at {s}:{e}')


# # Question 19

# In[9]:


import re
from datetime import datetime

date_string = '2023-10-07'
date_object = datetime.strptime(date_string, '%Y-%m-%d')
new_date_string = datetime.strftime(date_object, '%d-%m-%Y')

print(f'Original date: {date_string}')
print(f'New date: {new_date_string}')


# # Question 20

# In[19]:


import re
Text: "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
pattern = re.compile(r'\b\d+\.\d{1,2}\b')
result = pattern.findall(text)


# # Question 21

# In[20]:


import re
text = "01.12 0132.123 2.31875 145.8 3.01 27.25 0.25"
print("Numbers and their positions in the string:")
for m in re.finditer(r"\d+", text):
    print(f"Number: {m.group(0)}, Position: {m.start()}")


# # Question 22

# In[21]:


import re
text = "My marks in each semester are: 947, 896, 926, 524, 734, 950, 642"
numbers = re.findall(r"\d+", text)
max_number = max(map(int, numbers))
print(f"The maximum numeric value in the string is {max_number}.")


# # Question 23

# In[25]:


import re

def insert_spaces(s):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", s)

text = "RegularExpressionIsAnImportantTopicInPython"
print(insert_spaces(text))


# # Question 24

# In[26]:


import re
text = "RegularExpressionIsAnImportantTopicInPython"
print(re.findall(r"[A-Z][a-z]+", text))


# # Question 25

# In[29]:


import re
text = "Hello hello world world"
print("Original text:", text)
# Remove continuous duplicate words
text = re.sub(r"\b(\w+)(\s+\1)+\b", r"\1", text)

print("Modified text:", text)


# # Question 26

# In[ ]:


import re

def check_string(s):
    if re.search(r"\w$", s):
        print("The string ends with an alphanumeric character.")
    else:
        print("The string does not end with an alphanumeric character.")

text = input("Enter a string: ")
check_string(text)


# # Question 27

# In[ ]:


import re
Text: """RT @kapil_kausik: #Doltiwal I mean #xyzabc is "hurt" by #Demonetization as the same has rendered USELESS <ed><U+00A0><U+00BD><ed><U+00B1><U+0089> "acquired funds" No wo"""
print(re.findall("#\w+",Text))


# # Question 28

# In[ ]:


import re

text = "@Jags123456 Bharat band on 28??<ed><U+00A0><U+00BD><ed><U+00B8><U+0082>Those who  are protesting #demonetization  are all different party leaders"
text = re.sub(r"<U\+[0-9A-Fa-f]{4}>", "", text)
print(text)


# # Question 29

# In[ ]:


import re

filename = input("Enter the filename: ")
with open(filename, "r") as f:
    text = f.read()
    dates = re.findall(r"\d{2}-\d{2}-\d{4}", text)
    print("Dates in the given text:")
    for date in dates:
        print(date)


# # Question 30

# In[ ]:


import re

def remove_words(s):
    pattern = re.compile(r"\b\w{2,4}\b")
    return pattern.sub("", s)

text = "The following example creates an ArrayList with a capacity of 50 elements. 4 elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(remove_words(text))


# In[ ]:




