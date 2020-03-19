
import sqlite3

db = sqlite3.connect('Login.db')
cur = db.cursor()
cur.execute("INSERT INTO users VALUES (?,?)",("m1","1234"))
cur.execute("INSERT INTO users VALUES (?,?)",("m2","1234"))
cur.execute("INSERT INTO users VALUES (?,?)",("m3","1234"))
cur.execute("SELECT * FROM users")

users = {}
[users.update({row[0]:row[1]}) for row in cur]

db.commit()
db.close()