#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[4]:


get_ipython().system('pip install PySimpleGUI')


# In[5]:


import PySimpleGUI as simplegui


# In[6]:


c_score = 0
h_score = 0
c_choice = ""
h_choice = ""


# In[7]:


def choice_to_number(choice):
    rps_dict = {'rock':0, 'paper':1, 'scissors':2}
    return rps_dict[choice]


# In[8]:


def number_to_choice(number):
    rps_dict = {0:'rock', 1:'paper', 2:'scissors'}
    return rps_dict[number]


# In[9]:


def random_computer_choice():
    return random.choice(['rock','paper','scissors'])


# In[10]:


def choice_result(human_choice, computer_choice):
    global c_score
    global h_score
    
    h_num = choice_to_number(human_choice)
    c_num = choice_to_number(computer_choice)
    
    if (h_num - c_num)%3 == 1:
        c_score +=1
    elif h_num == c_num:
        print('TIE')
    else:
        h_num +=1


# In[11]:


def test_choice_to_number():
    assert choice_to_number('rock') == 0
    assert choice_to_number('paper') == 1
    assert choice_to_number('scissors') == 2
    
def test_number_to_choice():
    assert number_to_choice('rock') == 0
    assert number_to_choice('paper') == 1
    assert number_to_choice('scissors') == 2
    
def test_all():
    test_choice_to_number()
    test_number_to_choice
    
    


# In[13]:


test_all()


# In[ ]:




