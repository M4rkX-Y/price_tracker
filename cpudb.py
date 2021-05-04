import mysql.connector

def add_cpu(title, url, availability, price):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        cpu = (title, url, availability, price)
        c.execute("INSERT INTO amazon (title, url, availability, price) VALUES (%s, %s, %s, %s)", cpu)
        conn.commit()

def get_url():
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("SELECT id, url FROM amazon")
        links = c.fetchall()
        return links


def update_cpu(title, availability, price, id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        update = (title, availability, price, id)
        c.execute("UPDATE amazon SET title = %s, availability = %s, price = %s , date = NOW() WHERE id = %s", update)
        conn.commit()

def get_all():
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("SELECT id, title, url, availability, price FROM amazon")
        all = c.fetchall()
        return all

def get_ava(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT availability FROM amazon WHERE id = %s", index)
        ava = c.fetchall()
        return ava

def get_price(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT price FROM amazon WHERE id = %s", index)
        price = c.fetchall()
        return price

def add_log(title, pchange):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        cpu = (title, pchange)
        c.execute("INSERT INTO log (title, price_change, date) VALUES (%s, %s, NOW())", cpu)
        conn.commit()

def add_error_log(error):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("INSERT INTO error_log (error, date) VALUES (%s, NOW())", error)
        conn.commit()

#need test here