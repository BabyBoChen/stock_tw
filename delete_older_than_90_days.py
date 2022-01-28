from stock_tw_context import *
from datetime import *

def delete_mi_index_older_than_90_days():
    try:
        conn = StockTWContext()
        session = conn.session
        daily_trans = session.query(MI_INDEX).all()
        for i in daily_trans:
            dt_str = i.date
            dt = datetime.strptime(dt_str, "%Y-%m-%d")
            if dt < datetime.now() - timedelta(days=90):
                session.delete(i)
        session.commit()
        conn.close()
    except Exception as ex:
        print(ex)