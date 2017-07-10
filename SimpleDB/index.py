import sqlite3

conn = sqlite3.connect('SimpleDB.sqlite')

cursor = conn.cursor()

sqlstr = 'INSERT INTO user ("id", "username") VALUES ("1", "leo")'

#cursor.execute(sqlstr)

#cursor = conn.execute('SELECT * FROM user')
#rows = cursor.fetchall()

cursor = conn.execute('UPDATE user SET username="JASON" WHERE username="leo"')

#cursor = cursor.execute('DELETE FROM user WHERE username="JASON"')

#print(rows)

conn.commit()

conn.close()