import mysql.connector

def add_amz_cpu(title, url, availability, price):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        cpu = (title, url, availability, price)
        c.execute("INSERT INTO amz (title, url, availability, price) VALUES (%s, %s, %s, %s)", cpu)
        conn.commit()

def get_amz_url():
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("SELECT id, url FROM amz")
        links = c.fetchall()
        return links


def update_amz_cpu(availability, price, id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        update = (availability, price, id)
        c.execute("UPDATE amz SET availability = %s, price = %s , date = NOW() WHERE id = %s", update)
        conn.commit()

def get_amz_all():
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("SELECT id, title, url, availability, price FROM amz")
        all = c.fetchall()
        return all

def get_amz_ava(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT availability FROM amz WHERE id = %s", index)
        ava = c.fetchall()
        return ava

def get_amz_price(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT price FROM amz WHERE id = %s", index)
        price = c.fetchall()
        return price

def update_amz_time(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        web = (id, )
        c.execute("UPDATE amz SET date = NOW() WHERE id = %s", web)
        conn.commit()

def get_amz_time(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT date FROM amz WHERE id = %s", index)
        date = c.fetchall()
        return date

def add_amz_cpu(title, url):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        cpu = (title, url)
        c.execute("INSERT INTO amz (title, url) VALUE (%s, %s)", cpu)
        conn.commit()







def add_log(title, pchange, website, date):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        log = (title, pchange, website, date)
        c.execute("INSERT INTO log (title, price_change, website, date) VALUES (%s, %s, %s, %s)", log)
        conn.commit()

def add_error_log(error, website):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        error = (error, website)
        c.execute("INSERT INTO error_log (error, website, date) VALUES (%s, %s, NOW())", error)
        conn.commit()
#need test here









def add_nwe_url(url):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        cpu = (url,)
        c.execute("INSERT INTO nwe (url) VALUE (%s)", cpu)
        conn.commit()

def get_nwe_url():
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("SELECT id, url FROM nwe")
        links = c.fetchall()
        return links

def update_nwe_cpu(availability, price, id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        update = (availability, price, id)
        c.execute("UPDATE nwe SET availability = %s, price = %s , date = NOW() WHERE id = %s", update)
        conn.commit()

def get_nwe_price(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT price FROM nwe WHERE id = %s", index)
        price = c.fetchall()
        return price

def get_nwe_ava(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT availability FROM nwe WHERE id = %s", index)
        ava = c.fetchall()
        return ava

def get_nwe_all():
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        c.execute("SELECT url, availability, price FROM nwe")
        all = c.fetchall()
        return all

def add_nwe_cpu(title, url):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        cpu = (title, url)
        c.execute("INSERT INTO nwe (title, url) VALUE (%s, %s)", cpu)
        conn.commit()

def update_nwe_time(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        web = (id, )
        c.execute("UPDATE nwe SET date = NOW() WHERE id = %s", web)
        conn.commit()

def get_nwe_time(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT date FROM nwe WHERE id = %s", index)
        date = c.fetchall()
        return date
        





def get_cpulist(id):
        conn = mysql.connector.connect(host="localhost", user="root", password="Bj64989865", database="cpu")
        c = conn.cursor()
        index = (id, )
        c.execute("SELECT title, price FROM cpulist WHERE id = %s", index)
        all = c.fetchall()
        return all