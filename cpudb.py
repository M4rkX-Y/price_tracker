import mysql.connector

def add_cpu(title, url, availability, price):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        cpu = (title, url, availability, price)
        c.execute("INSERT INTO amazon (title, url, availability, price) VALUES (%s, %s, %s, %s)", cpu)
        conn.commit()

def get_amz_url():
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("SELECT id, url FROM amazon")
        links = c.fetchall()
        return links


def update_amz_cpu(title, availability, price, id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        update = (title, availability, price, id)
        c.execute("UPDATE amazon SET title = %s, availability = %s, price = %s , date = NOW() WHERE id = %s", update)
        conn.commit()

def get_amz_all():
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("SELECT id, title, url, availability, price FROM amazon")
        all = c.fetchall()
        return all

def get_amz_ava(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT availability FROM amazon WHERE id = %s", index)
        ava = c.fetchall()
        return ava

def get_amz_price(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT price FROM amazon WHERE id = %s", index)
        price = c.fetchall()
        return price





def add_log(title, pchange, website):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        log = (title, pchange, website)
        c.execute("INSERT INTO log (title, price_change, website, date) VALUES (%s, %s, %s, NOW())", log)
        conn.commit()

def add_error_log(error, website):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        error = (error, website)
        c.execute("INSERT INTO error_log (error, website, date) VALUES (%s, ,%s, NOW())", error)
        conn.commit()
#need test here





def add_nwe_url(url):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        cpu = (url,)
        c.execute("INSERT INTO newegg (url) VALUE (%s)", cpu)
        conn.commit()

def get_nwe_url():
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("SELECT id, url FROM newegg")
        links = c.fetchall()
        return links

def update_nwe_cpu(title, availability, price, id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        update = (title, availability, price, id)
        c.execute("UPDATE newegg SET title = %s, availability = %s, price = %s , date = NOW() WHERE id = %s", update)
        conn.commit()

def get_nwe_price(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT price FROM newegg WHERE id = %s", index)
        price = c.fetchall()
        return price

def get_nwe_ava(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT availability FROM newegg WHERE id = %s", index)
        ava = c.fetchall()
        return ava