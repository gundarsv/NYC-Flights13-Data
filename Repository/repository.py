from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from urllib import parse


class Repository:
    Base = automap_base()
    Airlines = None
    Planes = None
    Flights = None
    Engine = None

    def __init__(self, connection_string):
        params = parse.quote_plus(connection_string)
        self.Engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params, fast_executemany=True)
        self.Base.prepare(self.Engine, reflect=True)
        self.Airlines = self.Base.classes.Airlines
        self.Planes = self.Base.classes.Planes
        self.Flights = self.Base.classes.Flights

    def get_all_airlines(self):
        session = Session(self.Engine)
        all_airlines = session.query(self.Airlines).all()
        session.close()
        return all_airlines
