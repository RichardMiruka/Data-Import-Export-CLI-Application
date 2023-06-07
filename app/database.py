from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# Update the database connection URL accordingly
DB_URL = "sqlite:///data.db"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)



    