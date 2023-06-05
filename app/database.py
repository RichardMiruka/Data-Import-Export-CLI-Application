from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# The database connection URL
DATABASE_URL = "sqlite:///data.db"

# The engine
engine = create_engine(DATABASE_URL)

# The session factory
Session = sessionmaker(bind=engine)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'
    
    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)
    column3 = Column(String)
    