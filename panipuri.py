#!C:\Users\ACER\AppData\Local\Programs\Python\Python310\python
from ast import Break
import cgi
import pymysql
print("content-type:text/html")
print()
try:
    form=cgi.FieldStorage()
    Name=form.getvalue("nm")
    Item_Name=form.getvalue("puri")
    Plates=int(form.getvalue("item"))
    date=form.getvalue("date")
    
    con=pymysql.connect(host="b9ub01ym8sg6cnvyrbc0-mysql.services.clever-cloud.com",user="u2cu7q0msp84ih9j",password="aW99oY1iOPOVvMlxeznu",database="b9ub01ym8sg6cnvyrbc0")
    curs=con.cursor()
    curs.execute("insert into puri values('%s','%s',%d,'%s')"%(Name,Item_Name,Plates,date))
    con.commit()
    con.close()
    
    print("<body style='background-color:pink'><br><h1>congradulations!! Order Placed</h1></body>")
except Exception as e:
    print('unable to place this order ',e) 
    print("<br>")  
print("<a href='indexx.html'>Home</a>") 

      