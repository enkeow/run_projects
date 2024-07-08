from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
  

engine = create_engine('postgresql://postgres:Konako325@localhost:5432/postgres')
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()
