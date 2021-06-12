import sqlite3


class Product:

    def __init__(self):
        self.connection = sqlite3.connect('db.sqlite3')
        pass

    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('create table if not exists {} (id integer PRIMARY KEY, name text , price text'.format('products'))
        self.connection.commit()

    def insert(self, id, name, price):
        cursor = self.connection.cursor()
        cursor.execute("insert into products values (?, ?, ?)", (id, name, price))
        self.connection.commit()
        print("Row inserted")

    def select (self, id, name=None, price=None):
        cursor = self.connection.cursor()
        cursor.execute(f"select * from products where id = {id}")
        self.connection.commit()
        print('Row selected')

    def update(self, id, name=None, price=None):
        cursor = self.connection.cursor()
        cursor.execute(f"update products set name = 'Eggs' where id = {id}")
        self.connection.commit()
        print("Row updated")

    def delete(self, id):
        cursor = self.connection.cursor()
        cursor.execute(f"delete from products where id = {id}")
        self.connection.commit()
        print("Row deleted")


product = Product()
product.create_table()
product.insert(1, 'Cheese', 115)
product.insert(2, 'cabbage', 80)
product.insert(3, 'potato', 67)
product.select(1)
product.update(3)
product.delete(2)



