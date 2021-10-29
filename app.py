from flask import Flask, render_template
from flask_cors import CORS
from db_context import *

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    db = Db_context()
    companies = db.get_all_companies()
    return render_template('index.html',model=companies)

@app.route("/history/<code>")
def history(code:str):
    db = Db_context()
    trans = db.get_season_by_code(code, desc=True)
    return render_template('tb_trans.html',model=trans)

@app.route("/api/history/<code>")
def api_history(code:str):
    db = Db_context()
    trans = db.get_season_by_code(code)
    trans_list = []
    for tran in trans:
        item = {}
        item["date"] = tran.date[5:]
        item["closing_price"] = float(tran.closing_price)
        trans_list.append(item)
    json_data = {"data":trans_list}
    return json_data