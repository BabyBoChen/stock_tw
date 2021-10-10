import requests
from typing import Optional
import json
from pprint import *
import sqlite3
import re

def get_companies_by_type(type_code:int) -> Optional[list]:

    params = {
        "filter":type_code
    }

    r = requests.get('https://www.twse.com.tw/zh/api/codeFilters',params=params)

    companies_json = json.loads(r.text)

    companies = []

    for item in companies_json['resualt']:
        company = {
            "id":None,
            "code":None,
            "company_name":None
        }
        code = re.findall(r'\d\d\d\d', item)[0]
        company_name = re.findall(r'(?<=\t)\S+',item)[0]
        company["code"] = code
        company["company_name"] = company_name
        companies.append(company)
    
    return companies

def main() -> None:
    companies = get_companies_by_type(30)

    con = sqlite3.connect('stock_tw.db')
    cur = con.cursor()

    for comp in companies:

        cur.execute(r'''
            INSERT INTO Company(Id, Code, CompanyName) VALUES(?,?,?)'''
            ,(comp["id"], comp["code"], comp["company_name"]))
    
    con.commit()
    con.close()


if __name__ == '__main__':
    main()
    pass
