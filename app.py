from flask import Flask, render_template, send_from_directory
from db_context import *
import os
from stock_tw_context import *
from sqlalchemy import desc

app = Flask(__name__)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def index():
    db = Db_context()
    companies = db.get_all_companies()
    return render_template('index.html',model=companies)

@app.route("/history/<code>")
def history(code:str):
    # db = Db_context()
    # trans = db.get_season_by_code(code, desc=True)
    conn = StockTWContext()
    session = conn.session
    trans = session.query(MI_INDEX).filter(MI_INDEX.code == code).order_by(desc(MI_INDEX.date)).all()
    conn.close()
    return render_template('tb_trans.html',model=trans)

@app.route("/api/history/<code>")
def api_history(code:str):
    conn = StockTWContext()
    session = conn.session
    trans = session.query(MI_INDEX).filter(MI_INDEX.code == code).order_by(MI_INDEX.date).limit(90).all()
    # db = Db_context()
    # trans = db.get_season_by_code(code)
    trans_list = []
    for tran in trans:
        item = {}
        item["date"] = tran.date[5:]
        if tran.closingprice is None:
            continue
        item["closing_price"] = float(tran.closingprice)
        trans_list.append(item)
    json_data = {"data":trans_list}
    return json_data

# if __name__ == '__main__':
#     app.run()