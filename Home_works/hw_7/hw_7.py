import sqlite3


class Author:

    def __init__(self):
        self.connection = sqlite3.connect('new.db')
        pass

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table author (id integer PRIMARY KEY, name text , surname text, work_pace text);')
        except sqlite3.OperationalError:
            print('Таблица уже существует')
        self.connection.commit()

    def insert(self, id, name, surname, work_place):
        cursor = self.connection.cursor()
        cursor.execute("insert into author values (?, ?, ?, ?)", (id, name, surname, work_place))
        self.connection.commit()

    def select (self, id, name=None, surname=None, work_place=None):
        cursor = self.connection.cursor()
        cursor.execute(f"select * from author where id = {id}")
        self.connection.commit()

    def update(self, id, name=None, surname=None, work_place=None):
        cursor = self.connection.cursor()
        cursor.execute(f"update author set name = 'kkk' where id = {id}")
        self.connection.commit()

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"delete from author where id = {id}")
        self.connection.commit()

    def link(self):
        cursor = self.connection.cursor()
        cursor.execute()


author = Author()
author.create_table()
author.insert(1, 'Piter', 'Parker', 'Daily Bugle')
author.insert(2, 'Clark', 'Kent', 'Daily Planet')


class Post:

    def __init__(self):
        self.connection = sqlite3.connect('new.db')
        pass

    def create_table(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute('create table post (id integer PRIMARY KEY, title text , description text,'
                           ' date_1 text, authors_id integer , foreign key (author_id) references author(id);')
        except sqlite3.OperationalError:
            print('Таблица уже существует')
        self.connection.commit()

    def insert(self, id, title, description, date_1, authors_id):
        cursor = self.connection.cursor()
        cursor.execute("insert into post values (?, ?, ?, ?, ?)", (id, title, description, date_1, authors_id))
        self.connection.commit()

    def select(self, id, title=None, description=None, date_1=None, authors_id=None):
        cursor = self.connection.cursor()
        cursor.execute(f"select * from post where id = {id}")
        self.connection.commit()

    def update(self, id, title=None, description=None, date_1=None, authors_id=None):
        cursor = self.connection.cursor()
        cursor.execute(f"update post set name = 'Eggs' where id = {id}")
        self.connection.commit()

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"delete from post where id = {id}")
        self.connection.commit()

post = Post()
post.create_table()
post.insert(1, 'awesome Spider-Man', 'kjkjkj', '2008.07.01', 1)
post.insert(2, 'Spaider-Man saves the city', 'jkjkjl', '2008.07.11', 1)
post.insert(3, 'super-Man спасает бабушку от грузовика', 'klklkl', '2020.09.01', 2)
post.insert(4, 'super-Man dead', 'klklkl', '2020.12.12', 2)

