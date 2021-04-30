import sqlite3
 
def backup_url():
    conn = sqlite3.connect('backup_url.db')
    c = conn.cursor()
    c.execute("SELECT link, rowid FROM products")   
    links = c.fetchall()
    conn.close()  
    return links

