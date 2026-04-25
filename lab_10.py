import sqlite3

conn = sqlite3.connect('hw.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL,
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
""")
conn.commit()



def insert_products():
    cursor.execute("DELETE FROM products")

    products = [
        ("Ноутбук", 55000.0, 5),
        ("Смартфон", 30000.0, 8),
        ("Наушники", 2500.0, 15),
        ("Клавиатура", 1500.0, 12),
        ("Мышь", 800.0, 20),
        ("Монитор", 12000.0, 6),
        ("Флешка 64GB", 700.0, 25),
        ("Жесткий диск 1TB", 4500.0, 7),
        ("Веб-камера", 2000.0, 9),
        ("Колонки", 3500.0, 10),
        ("Роутер", 2800.0, 11),
        ("Принтер", 9000.0, 4),
        ("Сканер", 7500.0, 3),
        ("Игровой геймпад", 2200.0, 13),
        ("Микрофон", 1800.0, 14),
    ]

    cursor.executemany(
        "INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)",
        products
    )
    conn.commit()



def update_quantity(product_id, new_quantity):
    cursor.execute(
        "UPDATE products SET quantity = ? WHERE id = ?",
        (new_quantity, product_id)
    )
    conn.commit()



def update_price(product_id, new_price):
    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (new_price, product_id)
    )
    conn.commit()



def delete_product(product_id):
    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )
    conn.commit()



def get_all_products():
    cursor.execute("SELECT * FROM products")
    for p in cursor.fetchall():
        print(p)



def get_cheap_products():
    cursor.execute("""
    SELECT * FROM products
    WHERE price < 10000 AND quantity > 5
    """)
    for p in cursor.fetchall():
        print(p)



def search_products(keyword):
    cursor.execute("""
    SELECT * FROM products
    WHERE product_title LIKE ?
    """, ('%' + keyword + '%',))
    for p in cursor.fetchall():
        print(p)



if __name__ == "__main__":
    insert_products()

    print("\nВсе товары:")
    get_all_products()

    print("\nДешевые товары:")
    get_cheap_products()

    print("\nПоиск 'ноут':")
    search_products("ноут")

    print("\nОбновление количества (id=1):")
    update_quantity(1, 99)
    get_all_products()

    print("\nОбновление цены (id=2):")
    update_price(2, 50000)
    get_all_products()

    print("\nУдаление товара (id=3):")
    delete_product(3)
    get_all_products()

    conn.close()