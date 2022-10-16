#!C:\Users\ACER\AppData\Local\Programs\Python\Python310\python
import pymysql
print("content-type:text/html")
print()
print("<link rel='stylesheet' href='bootstrap.min.css'>")
print("<div class='container'>")
print("<br><br><h3 class='display-6'>Order Details</h3><hr>")
con=pymysql.connect(host="b9ub01ym8sg6cnvyrbc0-mysql.services.clever-cloud.com",user="u2cu7q0msp84ih9j",password="aW99oY1iOPOVvMlxeznu",database="b9ub01ym8sg6cnvyrbc0")
curs=con.cursor()
curs.execute("select * from puri")
data=curs.fetchall()
#print(data)
print("<table class='table table-bordered table-hover'>")
print("<tr style='background-color:steelblue'>")
print("<th>Name")
print("<th>Item_Name")
print("<th>Plates")
print("<th>Date")
print("</tr>")
for rec in data:
    print("<tr>")
    print("<td>%s" %rec[0])
    print("<td>%s" %rec[1])
    print("<td>%d" %rec[2])
    print("<td>%s" %rec[3])
    print("</tr>")

print("</table>")


con.close()
print("<br>")
print("<a href='indexx.html'>Home</a>")

