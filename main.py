#!"[Location of Python Application]"
print("Content-Type: text/html\n\n")

import cgi
form=cgi.FieldStorage()
id=form.getvalue("id")
email=form.getvalue("email")

import sys
sys.path.append("[Location of SQL Connector]")
import mysql.connector

con=mysql.connector.connect(user='root', password='', host='localhost', database='[database name]')
cur=con.cursor()

cur.execute("insert into [table name] values(%s,%s)", (id,email))
con.commit()

cur.close()
con.close()

print("<h3>Your record has been inserted into the SQL Database successfuly.</h3>")
print("<a href='http://localhost/index.html'><h3>Click here to return to the website!</h3></a>")
