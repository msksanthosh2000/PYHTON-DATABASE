#!/usr/bin/env python
# coding: utf-8

# ## SQL CONNECTION 

# In[3]:


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291"
)

if db.is_connected():
    print("Database Connected")


# # DATABASE CREATION

# In[4]:


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE Company_db")

print("Database Created Successful !!!")


# ## TABLE CREATION

# In[8]:


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291",
    database="Company_db",
)

cursor = db.cursor()
sql = """CREATE TABLE emp (
  emp_id INT AUTO_INCREMENT PRIMARY KEY,
  emp_name VARCHAR(255),
  email Varchar(255),
  number int,
  position Varchar(255),
  salary int,
  dept varchar(255)
)
"""
cursor.execute(sql)

print("Table Created Successful !!!")


# ## INSERTING ROW

# In[11]:


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291",
    database="Company_db",
)

cursor = db.cursor()
sql = "INSERT INTO emp (emp_name, email,number,position,salary,dept) VALUES (%s, %s, %s, %s, %s, %s)"
val = ("Harry", "harry@gmail.com","876543210","Developer","40000","IT")
cursor.execute(sql, val)

db.commit()

print("{} data added".format(cursor.rowcount))


# ## INSERT MORE ROWS

# In[12]:


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291",
    database="Company_db",
)

cursor = db.cursor()
sql = "INSERT INTO emp (emp_name, email,number,position,salary,dept) VALUES (%s, %s, %s, %s, %s, %s)"
values = [
  ("Harry", "harry@gmail.com","876543210","Developer","40000","IT"),
  ("Kane", "kane@gmail.com","876000000","Testing","30000","IT"),
  ("Linda", "linda@gmail.com","756473839","Manager","50000","HR")
]

for val in values:
  cursor.execute(sql, val)

db.commit()

print("{} data added".format(cursor.rowcount))


# ## FETCH FIRST ROW

# In[14]:


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291",
    database="company_db",
)

cursor = db.cursor()
sql = "SELECT * FROM emp"
cursor.execute(sql)

result = cursor.fetchone()

print(result)


# ## SHOW ALL ROWS

# In[21]:


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291",
    database="company_db",
)

cursor = db.cursor()
sql = "SELECT * FROM emp"
cursor.execute(sql)

results = cursor.fetchall()

for data in results:
  print(data)


# ## DELETE

# In[17]:


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291",
    database="company_db",
)

cursor = db.cursor()
sql = "DELETE FROM emp WHERE emp_id=%s"

num=cursor.rowcount
val = (2, )
cursor.execute(sql, val)

db.commit()

print("{} data deleted".format(cursor.rowcount))


# ## UPDATE

# In[20]:


import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291",
    database="Company_db",
)

cursor = db.cursor()
sql = "UPDATE emp SET position=%s, salary=%s WHERE emp_id=%s"
val = ("Developer", "45000", 3)
cursor.execute(sql, val)

db.commit()

print("{} data changed".format(cursor.rowcount))


# ## CRUD OPERATION

# In[ ]:


import mysql.connector
import os

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="8667444291",
    database="emp_data",
)


def insert_data(db):
  emp_name = input("Enter Name: ")
  email = input("Enter G-mail Address: ")
  number= input("Enter Phone No: ")
  position =input("Enter Position of EMP: ")
  salary = input("Enter Salary of EMP: ")
  dept = input("Enter Department of EMP")
  val = (emp_name, email,number,position,salary,dept)
  cursor = db.cursor()
  sql = "INSERT INTO emp (emp_name, email,number,position,salary,dept) VALUES (%s, %s,%s, %s,%s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("{} data Inserted".format(cursor.rowcount))


def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM emp"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)


def update_data(db):
  cursor = db.cursor()
  show_data(db)
  emp_id = input("Choose id of Employee : ")
  emp_name = input("Enter Name: ")
  email = input("Enter G-mail Address: ")
  number= input("Enter Phone No: ")
  position =input("Enter Position of EMP: ")
  salary = input("Enter Salary of EMP: ")
  dept = input("Enter Department of EMP")
  

  sql = "UPDATE emp SET emp_name=%s, email=%s, number=%s,position=%s,salary=%s,dept=%s WHERE emp_id=%s"
  val = (emp_name, email,number,position,salary,dept, emp_id)
  cursor.execute(sql, val)
  db.commit()
  print("{} data successfully changed".format(cursor.rowcount))


def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  emp_id = input("Choose id Employee : ")
  sql = "DELETE FROM emp WHERE emp_id=%s"
  val = (emp_id,)
  cursor.execute(sql, val)
  db.commit()
  print("{} data successfully deleted".format(cursor.rowcount))


def search_data(db):
  cursor = db.cursor()
  keyword = input("Keyword: ")
  sql = "SELECT * FROM emp WHERE emp_name LIKE %s OR email LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("There is not any data")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("-------------------------------- EMPLOYEE DATABASE PYTHON ------------------------------------------")
  print("1. Insert Data")
  print("2. Show Data")
  print("3. Update Data")
  print("4. Delete Data")
  print("5. Search Data")
  print("0. GO Out")
  print("----------------------------------------------------------------------------------------------------")
  menu = input("Choose menu> ")

  #clear screen
  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu WRONG!")


if __name__ == "__main__":
  while(True):
    show_menu(db)


# In[ ]:




