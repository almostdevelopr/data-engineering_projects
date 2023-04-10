#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip3 install psycopg2')


# In[2]:


import psycopg2


# In[3]:


# Create a connection to the database
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=postgres user=postgres password=root")
except psycopg2.Error as e:
    print("Error: Could not make connection to the postgres database")
    print(e)


# In[4]:


# print(conn)


# In[5]:


try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: could not get cursor to the database")
    print(e)


# In[6]:


conn.set_session(autocommit=True)


# In[7]:


try:
    cur.execute('create database myfirstdb')
except psycopg2.Error as e:
    print(e)


# In[8]:


try:
    conn.close()
except psycopg2.Error as e:
    print(e)
    
try:
    conn = psycopg2.connect("host=127.0.0.1 dbname=myfirstdb user=postgres password=root")
except psycopg2.Error as e:
    print("Error: Cannot connect to database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: could not get cursor to the database")
    print(e)
    
conn.set_session(autocommit=True)


# In[9]:


try:
    cur.execute("CREATE TABLE IF NOT EXISTS students (student_id int, name varchar,     age int, gender varchar, subject varchar, marks int);")
except psycopg2.Error as e:
    print("Error: issue creating table")
    print(e)


# In[10]:


try:
    cur.execute('describe table students;')
except psycopg2.Error as e:
    print(e)


# In[11]:


try:
    cur.execute('insert into students (student_id, name, age, gender, subject, marks)    values(%s, %s, %s, %s, %s, %s)',               (1, "Raj", 23, "Male", "Python", 85))
except psycopg2.Error as e:
    print("Error: inserting rows")
    print(e)
    
try:
    cur.execute('insert into students (student_id, name, age, gender, subject, marks)    values(%s, %s, %s, %s, %s, %s)',               (2, "Priya", 22, "Female", "Python", 86))
except psycopg2.Error as e:
    print("Error: inserting rows")
    print(e)


# In[12]:


try:
    cur.execute("select * from students")
except psycopg2.Error as e:
    print(e)
row = cur.fetchone()

while row:
    print(row)
    row = cur.fetchone()


# In[13]:


cur.close()
conn.close()


# In[ ]:




