import mysql.connector
import sqlite3
import datetime
from os import path
ROOT = path.dirname(path.realpath(__file__))

class Company:

    def __init__(self) -> None:
        self.id = None
        self.code = None
        self.company_name = None

class DailyTrans:

    def __init__(self) -> None:
        self.id = -1
        self.date = None
        self.code = None
        self.trade_volume = None
        self.transaction = None
        self.trade_value = None
        self.opening_price = None
        self.highest_price = None
        self.lowest_price = None
        self.closing_price = None
        self.change = None
        self.last_best_bid_price = None
        self.best_bid_volume = None
        self.best_ask_price = None
        self.best_ask_volume = None
        self.p_eratio = None

class Db_context:

    connString = path.join(ROOT, "stock_tw.db")

    def get_all_companies(self) -> list[Company]:
        
        con = sqlite3.connect(Db_context.connString)
        cur = con.cursor()
        cur.execute(r'SELECT * FROM company ORDER BY Code')
        rows = cur.fetchall()
        con.close()
        companies = []
        for row in rows:
            company = Company()
            company.id = int(row[0])
            company.code = row[1]
            company.company_name = row[2]
            companies.append(company)
        return companies

    def get_history_by_code(self, code:str) -> list[DailyTrans]:
        
        con = sqlite3.connect(Db_context.connString)
        cur = con.cursor()
        cur.execute(r'SELECT * FROM mi_index WHERE Code=?',(code,))
        rows = cur.fetchall()
        con.close()
        daily_trans = []
        for row in rows:
            trans = DailyTrans()
            trans.id = row[0]
            trans.date = row[1]
            trans.code = row[2]
            trans.trade_volume = row[3]
            trans.transaction = row[4]
            trans.trade_value = row[5]
            trans.opening_price = row[6]
            trans.highest_price = row[7]
            trans.lowest_price = row[8]
            trans.closing_price = row[9]
            trans.change = row[10]
            trans.last_best_bid_price = row[11]
            trans.best_bid_volume = row[12]
            trans.best_ask_price = row[13]
            trans.best_ask_volume = row[14]
            trans.p_eratio = row[15]
            daily_trans.append(trans)
        return daily_trans

    def get_season_by_code(self, code:str, desc:bool=False) -> list[DailyTrans]:
        today = datetime.date.today()
        last_season = today + datetime.timedelta(days = -90)
        
        con = sqlite3.connect(Db_context.connString)
        cur = con.cursor()
        sql = r"SELECT * FROM mi_index WHERE CODE=? AND (strftime([Date]) BETWEEN strftime(?) AND strftime(?))"
        if desc == True:
            sql += r" ORDER by [Date] desc"
        cur.execute(sql,(code,last_season,today))
        rows = cur.fetchall()
        con.close()
        daily_trans = []
        for row in rows:
            trans = DailyTrans()
            trans.id = row[0]
            trans.date = row[1]
            trans.code = row[2]
            trans.trade_volume = row[3]
            trans.transaction = row[4]
            trans.trade_value = row[5]
            trans.opening_price = row[6]
            trans.highest_price = row[7]
            trans.lowest_price = row[8]
            trans.closing_price = row[9]
            trans.change = row[10]
            trans.last_best_bid_price = row[11]
            trans.best_bid_volume = row[12]
            trans.best_ask_price = row[13]
            trans.best_ask_volume = row[14]
            trans.p_eratio = row[15]
            daily_trans.append(trans)
        return daily_trans


