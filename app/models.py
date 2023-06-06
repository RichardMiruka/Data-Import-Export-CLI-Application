from sqlalchemy import Column, Integer, String
from app.database import Base

# Defining the Data model that inherits from BaseData
class Data(Base):
    __tablename__ = 'data'

    id = Column(Integer, primary_key=True)
    column1 = Column(String)
    column2 = Column(String)
    column3 = Column(String)
