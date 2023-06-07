from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Defining the Data model that inherits from BaseData
class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)
    column3 = Column(String)
class Table1(Base):
    __tablename__ = 'table1'

    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)
    column3 = Column(String)
    
class Table2(Base):
    __tablename__ = 'table2'

    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)
    column3 = Column(String)
    
       
    
    