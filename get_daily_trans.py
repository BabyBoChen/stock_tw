from typing import Optional
import datetime
import time
import json
from pprint import *
import requests
import sqlite3
import re
from os import path
ROOT = path.dirname(path.realpath(__file__))

def int_try_parse(s:str) -> Optional[int]:
    res = None
    try:
        s = s.replace(",","")
        res = int(s)
    except Exception as ex:
        # print(ex)
        pass
    return res

def float_try_parse(s:str) -> Optional[float]:
    res = None
    try:
        s = s.replace(",","")
        res = float(s)
    except Exception as ex:
        # print(ex)
        pass
    return res

def get_daily_stock_data(target_date:datetime.date, stock_type:int) -> Optional[list]:

    date_str = f'{target_date:%Y%m%d}'
    date_db = f'{target_date:%Y-%m-%d}'

    params = {
        'response':'json',
        'date':date_str,
        'type': stock_type,
    }

    r = requests.get('https://www.twse.com.tw/exchangeReport/MI_INDEX', params=params)

    print(f"Get {target_date}!")

    time.sleep(5)

    if '很抱歉' in r.text or '查詢日期大於今日' in r.text:
        print(f"No data on {target_date}!")
        return []
    
    stock_json = json.loads(r.text)
    # pprint(stock_json['data1'])

    stock_daily = []
    for code in stock_json['data1']:
        record = {
            'Code':'',
            'Date': date_db,
            'TradeVolume' : None,
            'Transaction': None,
            'TradeValue': None,
            'OpeningPrice': None,
            'HighestPrice': None,
            'LowestPrice': None,
            'ClosingPrice': None,
            'Change': None,
            'LastBestBidPrice': None,
            'BestBidVolume':None,
            'BestAskPrice':None,
            'BestAskVolume':None,
            'PEratio':None
        }
        record['Code'] = code[0]
        record['TradeVolume'] = int_try_parse(code[2])
        record['Transaction'] = int_try_parse(code[3])
        record['TradeValue'] = int_try_parse(code[4])
        record['OpeningPrice'] = float_try_parse(code[5])
        record['HighestPrice'] = float_try_parse(code[6])
        record['LowestPrice'] = float_try_parse(code[7])
        record['ClosingPrice'] = float_try_parse(code[8])
        up_or_down = re.findall(r'(?<=[>]).*(?=[<])', code[9])[0]
        up_or_down_rate = 0
        if up_or_down == '+':
            up_or_down_rate = 1
        elif up_or_down == '-':
            up_or_down_rate = -1
        else:
            pass
        record['Change'] = float_try_parse(code[10]) * up_or_down_rate
        record['LastBestBidPrice'] = float_try_parse(code[11])
        record['BestBidVolume'] = int_try_parse(code[12])
        record['BestAskPrice'] = float_try_parse(code[13])
        record['BestAskVolume'] = int_try_parse(code[14])
        record['PEratio'] = float_try_parse(code[15])
        stock_daily.append(record)        
    
    return stock_daily

def main() -> None:

    start = datetime.date(2021,10,5)
    end = datetime.date(2021,10,10)
    for_db = []

    while start <= end:
        for_db.extend(get_daily_stock_data(start, 24))
        for_db.extend(get_daily_stock_data(start, 30))
        start = start + datetime.timedelta(days = 1)

    con = sqlite3.connect(path.join(ROOT, "stock_tw.db"))
    cur = con.cursor()

    for record in for_db:    
        cur.execute('''
            INSERT INTO MI_INDEX(
                Id,
                Code,
                [Date],
                TradeVolume,
                [Transaction],
                TradeValue,
                OpeningPrice,
                HighestPrice,
                LowestPrice,
                ClosingPrice,
                Change,
                LastBestBidPrice,
                BestBidVolume,
                BestAskPrice,
                BestAskVolume,
                PEratio
            ) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', 
            (
                None,
                record['Code'],
                record['Date'],
                record['TradeVolume'],
                record['Transaction'],
                record['TradeValue'],
                record['OpeningPrice'],
                record['HighestPrice'],
                record['LowestPrice'],
                record['ClosingPrice'],
                record['Change'],
                record['LastBestBidPrice'],
                record['BestBidVolume'],
                record['BestAskPrice'],
                record['BestAskVolume'],
                record['PEratio']
            )
        )
        continue

    con.commit()
    con.close()

if __name__ == '__main__':
    # main()
    pass


