# from stock_tw_context import *

# conn = create_engine("sqlite:///stock_tw.db")
# bind_engine(conn)
# session = Session()

# tsmc = session.query(Company).filter_by(code = '2330').first()

# trans = tsmc.daliy_trans

# print(trans)

import datetime

today = datetime.date.today()
last_season = today + datetime.timedelta(days = -90)

print(today)
print(last_season)