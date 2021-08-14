import psycopg2
import uuid
from random import randint
import random
import psycopg2.extras
import datetime

# SQL база с таблицами:
# 1) Users(userId, age)
# 2) Purchases (purchaseId, userId, itemId, date)
# 3) Items (itemId, price).

connection = psycopg2.connect(user="postgres",
                            password="secret",
                            host="127.0.0.1",
                            port="5432",
                            database="stage")
cursor = connection.cursor()

userID_list = []
itemID_list = []
psycopg2.extras.register_uuid()

def generate_users():
    for i in range (1000):
        userID = uuid.uuid4()
        userID_list.append(userID)
        cursor.execute("INSERT INTO users (userID, age) VALUES (%s, %s)", (userID, randint(18, 80)))
        connection.commit()
        print('User added')

def generate_items():
    for i in range (1000):
        itemID = uuid.uuid4()
        itemID_list.append(itemID)
        cursor.execute("INSERT INTO items (itemID, price) VALUES (%s, %s)", (itemID, round(random.uniform(50, 50000), 2)))
        connection.commit()
        print('Item added')

def generate_purchases():
    for i in range (10000):
        purchaseID = uuid.uuid4()
        userID = random.choice(userID_list)
        itemID = random.choice(itemID_list)
        # purchase date
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2021, 8, 16)
        days = (end_date - start_date).days
        random_days = random.randrange(days)
        purchase_date = start_date + datetime.timedelta(days=random_days)

        cursor.execute("INSERT INTO purchases (purchaseID, userID, itemID, purchase_date) VALUES (%s, %s, %s, %s)", (purchaseID, userID, itemID, purchase_date))
        connection.commit()
        print('Purchase added')

def show_table(table_name):
    cursor.execute("SELECT * FROM {}".format(table_name))
    while True:
        result = cursor.fetchone()
        print(result)
        if result == None:
            break
    

generate_users()
generate_items()
generate_purchases()

cursor.close()
connection.close()
