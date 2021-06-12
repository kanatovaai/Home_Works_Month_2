import sqlite3

connection = sqlite3.connect('db.sqlite3')
cursor = connection.cursor()
try:
    cursor.execute('create table students (id integer primary key, name text, age integer, gender text);')
except sqlite3.OperationalError:
    pass

cursor.execute("insert into students values (1, 'Aidai', 17, 'female');")
cursor.execute("insert into students values (2, 'Igor', 19, 'male');")
students = cursor.execute("select * from students").fetchall()
print(students)
# cursor.execute("update students set age = 20 where id = 2")
connection.commit()
connection.close()


