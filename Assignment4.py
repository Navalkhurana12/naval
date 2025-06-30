import csv

from urllib3.filepost import writer

data=[    ["name","addres","mobile","eamil"],
    ["naval","sgnr","3333","nnn@gamil.com"],
["nitesh","sgnnnr","33dd33","kk@gamil.com"],
["lavish","sgnr","3333","khi@gamil.com"]
]
with open("insert.csv","w",newline="")as file:
    writter=csv.writer(file)
    for x in data:
        writter.writerow(x)

with open("insert.csv","r",)as file:
    reader=csv.reader(file)
    for x in data:
        print(x)


print("questrion 2")
import requests
def wheather(city):
    url=(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3105bacf4b2769752da555b01961dedc")

    try:
        response =requests.get(url)
        response.raise_for_status()
        data=response.json()
        temperature=data["main"]["temp"]
        humidity=data["main"]["humidity"]
        feels_like=data["main"]["feels_like"]
        print(f"tempearture:{temperature}c(fells like:{feels_like})")
        print(f"humidity:{humidity}")

    except requests.exceptions.RequestException as e:
        print("error fetching weather data :{e}")

city=input("enter your city")
wheather(city)
print("question 3")
import sqlite3

conn=sqlite3.connect("mydatabas")
cursor=conn.cursor()
cursor.execute(
    '''
    create table if not exists users (
    userid  INTEGER PRIMARY KEY AUTOINCREMENT,
    NAME TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL)
    '''
)
cursor.execute(
    '''
    create table if not exists  products (
    product_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    product_email TEXT UNIQUE NOT NULL)
    '''
)
cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    order_date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(product_id) REFERENCES products(product_id)
)
''')

# Commit and close
conn.commit()
conn.close()

print("Tables created successfully!")
import sqlite3

# Connect to the database
conn = sqlite3.connect("mydatabas")
cursor = conn.cursor()

# Insert users
cursor.execute("INSERT INTO users(NAME,email)VALUES(?,?)", ("NAVAL", "nn@gmail.com"))
cursor.execute("INSERT INTO users(NAME,email)VALUES(?,?)", ("HELO", "kk@gmail.com"))

# Insert products
cursor.execute("INSERT INTO products(product_name,product_email)VALUES(?,?)", ("laptop", "laptommp@gmail.com"))
cursor.execute("INSERT INTO products(product_name,product_email)VALUES(?,?)", ("mobile", "mobimle@gmail.com"))

# Insert orders (use valid date format: YYYY-MM-DD)
cursor.execute("INSERT INTO orders(user_id,product_id,quantity,order_date)VALUES(?,?,?,?)", (1, 1, 1, "2023-05-09"))
cursor.execute("INSERT INTO orders(user_id,product_id,quantity,order_date)VALUES(?,?,?,?)", (1, 2, 2, "2023-04-15"))

# Confirm insertion
print("Data inserted successfully.\n")

# Show all users
print("Users:")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Show all products
print("\nProducts:")
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

# Show all orders
print("\nOrders:")
cursor.execute("SELECT * FROM orders")
for row in cursor.fetchall():
    print(row)

# Commit and close connection
conn.commit()
conn.close()
import sqlite3

conn = sqlite3.connect("mydatabas")
cursor = conn.cursor()

# Example: Update user name
cursor.execute("UPDATE users SET NAME = ? WHERE email = ?", ("NAVAL KHURANA", "nn@gmail.com"))

# Example: Update product
cursor.execute("UPDATE products SET product_name = ? WHERE product_id = ?", ("Gaming Laptop", 1))

# Example: Update order quantity
cursor.execute("UPDATE orders SET quantity = ? WHERE order_id = ?", (10, 1))

# Commit changes
conn.commit()

# Show updated users
print("Updated Users:")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Show updated products
print("\nUpdated Products:")
cursor.execute("SELECT * FROM products")
for row in cursor.fetchall():
    print(row)

# Show updated orders
print("\nUpdated Orders:")
cursor.execute("SELECT * FROM orders")
for row in cursor.fetchall():
    print(row)

conn.close()
