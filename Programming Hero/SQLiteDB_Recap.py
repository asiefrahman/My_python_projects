import sqlite3

conn = sqlite3.connect('facebook.db')
cursor = conn.cursor()

# conn.execute("CREATE TABLE facebook (Id INTEGER UNIQUE, Email TEXT UNIQUE, Password TEXT, Friends INTEGER)")

conn.execute("INSERT INTO facebook VALUES(5, 'fr@abc.com', 'iAMyoung', 40)")
conn.execute("INSERT INTO facebook VALUES(6, 'sf@abc.com', 'uAREyoung', 70)")
conn.execute("INSERT INTO facebook VALUES(7, 'ho@abc.com', 'iopyoung', 76)")
conn.execute("INSERT INTO facebook VALUES(8, 'cr@abc.com', 'iAMyoungik', 30)")


cursor.execute("SELECT * FROM facebook")

users = cursor.fetchall()
for row in users:
    print(row)

conn.commit()
conn.close()
