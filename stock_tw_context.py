from sqlalchemy import Column, String, Integer, Float, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()
Session = sessionmaker()

def bind_engine(engine):
    Base.metadata.bind = engine
    Session.configure(bind=engine)

class Company(Base):
    __tablename__ = 'Company'
    id = Column('Id', Integer, primary_key=True)
    code = Column('Code', String)
    company_name = Column('CompanyName', String)

    daliy_trans = relationship("DailyTrans", backref="Company")

    def __repr__(self):
        print_str = f"<Company(id={self.id}, code='{self.code}', company_name='{self.company_name}')>"
        return  print_str

class DailyTrans(Base):
    __tablename__ = 'MI_INDEX'
    id = Column('Id', Integer, primary_key=True)
    date = Column('Date', String)
    code = Column('Code', String, ForeignKey('Company.Code'))
    trade_volume = Column('TradeVolume', Integer)
    transaction = Column('Transaction', Integer)
    tradevalue = Column('TradeValue', Integer)
    openingprice = Column('OpeningPrice', Float)
    highestprice = Column('HighestPrice', Float)
    lowestprice = Column('LowestPrice', Float)
    closingprice = Column('ClosingPrice', Float)
    change = Column('Change', Float)
    lastbestbidprice = Column('LastBestBidPrice', Float)
    bestbidvolume = Column('BestBidVolume', Integer)
    bestaskprice = Column('BestAskPrice', Float)
    bestaskvolume = Column('BestAskVolume', Integer)
    peratio = Column('PEratio', Float)

    def __repr__(self):
        print_str = f'''<DailyTrans(id='{self.id}', date='{self.date}', code='{self.code}', trade_volume='{self.trade_volume}', transaction='{self.transaction}', tradevalue='{self.tradevalue}', openingprice='{self.openingprice}', highestprice='{self.highestprice}', lowestprice='{self.lowestprice}', closingprice='{self.closingprice}', change='{self.change}', lastbestbidprice='{self.lastbestbidprice}', bestbidvolume='{self.bestbidvolume}', bestaskprice='{self.bestaskprice}', bestaskvolume='{self.bestaskvolume}', peratio='{self.peratio}')>'''
        return  print_str

