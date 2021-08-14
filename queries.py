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
# В) какой товар обеспечивает дает наибольший вклад в выручку за последний год
# Г) топ-3 товаров по выручке и их доля в общей выручке за любой год

cursor.execute("""
SELECT to_char(purchases.purchase_date, 'month') AS month,
ROUND( AVG(items.price ), 2) AS avg_price
FROM purchases
JOIN users ON purchases.userID = users.userID
JOIN items ON purchases.itemID = items.itemID
WHERE users.age >=18 
AND users.age <=25
GROUP BY to_char(purchases.purchase_date, 'month')
""")
while True:
    result = cursor.fetchone()
    print(result)
    if result == None:
        break



cursor.close()
connection.close()