# import sqlite3 as sq
#
# with sq.connect("profile.db") as con:
#     cur = con.cursor()
#     cur.execute("DROP TABLE users")
#     # cur.execute("""
#     CREATE TABLE IF NOT EXISTS users(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     summa REAL,
#     data TEXT
#     )
#     """)


# import sqlite3 as sq
#
# with sq.connect("users.db") as con:
#     cur = con.cursor()
    # cur.execute("""
    # ALTER TABLE person_table
    # ADD COLUMN address TEXT NO NULL DEFAULT str
    # """)
    # cur.execute("""
    #     ALTER TABLE person_table
    #     RENAME COLUMN address TO home_address
    #     """)
    # cur.execute("""
    #        ALTER TABLE person_table
    #        DROP COLUMN home_address
    #        """)
    # cur.execute("""
    # DROP TABLE person_table
    # """)

    # cur.execute("""
    # CREATE TABLE IF NOT EXISTS person(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # name TEXT NOT NULL,
    # phone BLOB NOT NULL DEFAULT +7909000000,
    # age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
    # email TEXT UNIQUE
    # )
    # """)

# import sqlite3 as sq
#
# with sq.connect("users.db") as con:
#     cur = con.cursor()
#     # cur.execute("""
#     #    CREATE TABLE IF NOT EXISTS person(
#     #    id INTEGER PRIMARY KEY AUTOINCREMENT,
#     #    name TEXT NOT NULL,
#     #    phone BLOB NOT NULL DEFAULT +7909000000,
#     #    age INTEGER NOT NULL CHECK(age > 0 AND age < 100),
#     #    email TEXT UNIQUE
#     #    )
#     #    """)
#     cur.execute("""
#         INSERT INTO person
#         VALUES (10, "Ольга", "79991112233", 29, "test@mail.ru"
#         )
#         """)

# import sqlite3 as sq
#
# with sq.connect("db_4.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     SELECT *
#     FROM Ware
#     ORDER BY Price DESC
#     LIMIT 2, 5
#     """)
#
#     res = cur.fetchone()
#     print(res)
#
#     res2 = cur.fetchmany(4)
#     print(res2)

    # res = cur.fetchall()
    # print(res)

    # for res in cur:
    #     print(res)

# import sqlite3 as sq
#
# cars =[
#     ('BMW', 54000),
#     ('Cevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000)
# ]
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#     );
#     """)
#     cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
#     last_row_id = cur.lastrowid
#     buy_car_id = 2
#     cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))
# con=None
# try:
#     con = sq.connect("cars.db")
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     );
#     BEGIN;
#     INSERT INTO cars VALUES(NULL, "Rrenault", 22000);
#     UPDATE cars SET price=price+100;
#     """)
#     con.commit()
# except sq.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
# finally:
#     if con:
#         con.close()
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#     car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     model TEXT,
#     price INTEGER
#     )
#     """)
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%'; #удалились строки где модель на В
#     UPDATE cars SET price=price+100; # прибавили к стоимости по 100
#     """)
    # cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {'Price':0}) # написание именованного параметра и установка значения
    # cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars) # добавляется картеж как через цикл

    # for car in cars:
    #     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car) # добавляется написанный ранее кортеж через цикл

    # cur.execute('INSERT INTO cars VALUES(1, "Rrenault", 22000)')  #построчно добавили поля
    # cur.execute('INSERT INTO cars VALUES(2, "Mersedes", 45000)')
    # cur.execute('INSERT INTO cars VALUES(3, "Pegiot", 35000)')
    # cur.execute('INSERT INTO cars VALUES(4, "Volvo", 40000)')
    # cur.execute('INSERT INTO cars VALUES(5, "Gaz", 15000)')
    # cur.execute('INSERT INTO cars VALUES(6, "Audi", 30000)')

# con.commit()
# con.close()

import _sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     """)
#
#     cur.execute("SELECT model, price FROM cars")
#
#     # rows = cur.fetchall()
#     # rows = cur.fetchone()
#     # rows = cur.fetchmany(5)
#     # print(rows)
#
#     for res in cur:
#         print(res['model'], res['price'])

# ==============================================================================

# import sqlite3 as sq
# #
# #
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", 'rb') as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#             print(e)
#             return False
#     return True
# with sq.connect("cars.db") as con:
#     con.row_factory = sq.Row
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS users(
#         name TEXT,
#         ava BLOB,
#         score INTEGER
#     );
#     """)
#     cur.execute("SELECT ava FROM users LIMIT 1")
#     img = cur.fetchone()['ava']
#     write_ava("out.png", img)
    # img = read_ava(1)
    # if img:
    #     binary = sq.Binary(img)
    #     cur.execute("INSERT INTO users VALUES('Илья', ?, 1000)", (binary,))

# import sqlite3 as sq
#
# with sq.connect("cars.db") as con:
#     cur = con.cursor()
    #
    # with open("sql_dump.sql", 'r') as f:
    #     sql = f.read()
    #     cur.executescript(sql)

    # with open("sql_dump.sql", "w") as f:
    #     for sql in con.iterdump():
    #         f.write(sql)

    # for sql in con.iterdump():
    #     print(sql)


import sqlite3 as sq

data = [("car", "машина"), ("house", "дом"), ("tree", "дерево"), ("color", "цвет")]

con=sq.connect(":memory:")
with con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS dict(
    eng TEXT,
    rus TEXT
    )""")
    cur.executemany("INSERT INTO dict VALUES(?,?)", data)
    cur.execute("SELECT rus FROM dict WHERE eng LIKE 'c%'")
    print(cur.fetchall())

