import psycopg2

connection = psycopg2.connect(user="postgres",
                            password="secret",
                            host="127.0.0.1",
                            port="5432",
                            database="stage")
cursor = connection.cursor()

# А) какую сумму в среднем в месяц тратит:
# - пользователи в возрастном диапазоне от 18 до 25 лет включительно
# - пользователи в возрастном диапазоне от 26 до 35 лет включительно
# Б) в каком месяце года выручка от пользователей в возрастном диапазоне 35+ самая большая
# В) какой товар обеспечивает наибольший вклад в выручку за последний год

def average_per_month_18_25():
    cursor.execute("""
    SELECT 
        to_char(purchases.purchase_date, 'month') AS month,
        ROUND( AVG(items.price ), 2) AS avg_price
    FROM purchases
    JOIN users ON purchases.userID = users.userID
    JOIN items ON purchases.itemID = items.itemID
    WHERE 
        users.age >=18 
        AND users.age <=25
    GROUP BY to_char(purchases.purchase_date, 'month')
    """)
    while True:
        result = cursor.fetchone()
        if result == None:
            break
        else:
            print(result)

def average_per_month_26_35():
    cursor.execute("""
    SELECT 
        to_char(purchases.purchase_date, 'month') AS month,
        ROUND( AVG(items.price ), 2) AS avg_price
    FROM purchases
    JOIN users ON purchases.userID = users.userID
    JOIN items ON purchases.itemID = items.itemID
    WHERE 
        users.age >=26
        AND users.age <=35
    GROUP BY to_char(purchases.purchase_date, 'month')
    """)
    while True:
        result = cursor.fetchone()
        if result == None:
            break
        else:
            print(result)

def max_money_month_35():
    cursor.execute("""
    SELECT 
        to_char(purchases.purchase_date, 'month') AS month,
        date_part('year', purchases.purchase_date) AS year,
        SUM(items.price ) AS sum_price
    FROM purchases
    JOIN users ON purchases.userID = users.userID
    JOIN items ON purchases.itemID = items.itemID
    WHERE users.age >=35
    GROUP BY 
        to_char(purchases.purchase_date, 'month'), 
        date_part('year', purchases.purchase_date)
    ORDER BY sum_price DESC
    LIMIT 1
    """)
    while True:
        result = cursor.fetchone()
        if result == None:
            break
        else:
            print(result)


def max_money_share_item():
    cursor.execute("""
    SELECT COUNT(purchases.itemID) * items.price AS item_sum, items.itemID
    FROM items
    LEFT JOIN purchases ON purchases.itemID = items.itemID
    WHERE date_part('year', purchases.purchase_date) = date_part('year', now())
    GROUP BY items.itemID
    ORDER BY item_sum DESC
    LIMIT 1
    """)
    while True:
        result = cursor.fetchone()
        if result == None:
            break
        else:
            print(result)


# average_per_month_18_25()
# average_per_month_26_35()
# max_money_month_35()
# max_money_share_item()


cursor.close()
connection.close()
