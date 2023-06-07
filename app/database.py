from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///data.db')
Base = declarative_base()
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
Base.query = Session.query_property()


    