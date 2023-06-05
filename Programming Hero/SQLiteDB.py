
# import sqlite3 package to introduce database system in python environment

import sqlite3

# creating a database under a variable
conn = sqlite3.connect('test.db')

# creating cursor to execute queries
c = conn.cursor()

# creating a table
'''c.execute("""CREATE TABLE IF NOT EXIST test(
    First_name text,
    Last_name text,
    email_id text)
    """)'''

# taking input from user and putting it into the database
'''a = str(input('First name: '))
b = str(input('Last Name: '))
d = str(input('Email ID: '))
c.execute("""INSERT INTO test VALUES(?, ?, ?)""", (a, b, d))
c.execute("SELECT * FROM test")
# c.execute("DELETE FROM test WHERE First_name = 'a'")
print(c.fetchall())
conn.commit()
conn.close()'''

# checking an input if it is in the table
user_email = input('Provide your email: ')
c.execute("SELECT * FROM TEST where email_id = :email_id", {'email_id': user_email})
user = c.fetchone()

if user is not None:
    print('You are a member')
else:
    print("Invalid user")

conn.commit()
conn.close()

c.execute('SELECT * FROM TEST')
all_user = c.fatchone()
print(all_user)
