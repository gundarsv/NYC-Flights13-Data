from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import or_

from urllib import parse

import Repository.read_csv as read_csv
import Repository.load_data as load_data

Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
connecting_string = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:nycflights13.database.windows.net,1433;Database=nycflights13;Uid=nycflights;Pwd=flights13!;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'
params = parse.quote_plus(connecting_string)

engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params, fast_executemany=True)

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Airlines = Base.classes.Airlines
Planes = Base.classes.Planes


session = Session(engine)


# load_data.load_planes(read_csv.get_all_planes(), engine)
# load_data.load_airlines(read_csv.get_all_airlines(), engine)

for plane in session.query(Planes.model).all():
    print(plane)

session.close()
