import sqlite3
import mysql.connector

# connString = 'stock_tw.db'

# con = sqlite3.connect(connString)
# cur = con.cursor()
# sql = r"SELECT * FROM MI_INDEX ORDER BY [Date] desc, Code"
# cur.execute(sql)
# rows = cur.fetchall()
# con.close()

# my_conn = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# mycur = my_conn.cursor()

# sql2 = r'''
#     INSERT INTO `stock_tw`.`mi_index` 
#     (`Date`, `Code`, `TradeVolume`, `Transaction`, `TradeValue`, 
#     `OpeningPrice`, `HighestPrice`, `LowestPrice`, `ClosingPrice`, 
#     `ChangeRate`, `LastBestBidPrice`, `BestBidVolume`, `BestAskPrice`, 
#     `BestAskVolume`, `PEratio`) 
#     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'''

# for row in rows:
#     parameters = tuple(row[1:])
#     mycur.execute(sql2, parameters)

# my_conn.commit()
# my_conn.close()

# connString = 'stock_tw.db'

# con = sqlite3.connect(connString)
# cur = con.cursor()
# sql3 = r"SELECT * FROM Company ORDER BY Code"
# cur.execute(sql3)
# rows = cur.fetchall()
# con.close()

# my_conn = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password=""
# )

# mycur = my_conn.cursor()

# sql4 = r'''
#     INSERT INTO `stock_tw`.`company` 
#     (`Code`, `CompanyName`) 
#     VALUES (%s,%s);'''

# for row in rows:
#     parameters = tuple(row[1:])
#     mycur.execute(sql4, parameters)

# my_conn.commit()
# my_conn.close()
    
