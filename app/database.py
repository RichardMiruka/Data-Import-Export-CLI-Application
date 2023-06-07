from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Data

# The database connection URL 
DB_URL = "sqlite:///data.db"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)
    
def seed_data():
    session = Session()
    
       # Checking if the data table is already populated
    existing_data = session.query(Data).count()
    if existing_data > 0:
        session.close()
        return 
    # Seed the data table with initial data
    data_entries = [
        Data(column1='Value 1', column2='Value 2', column3='Value 3'),
        Data(column1='Value 4', column2='Value 5', column3='Value 6'),
        Data(column1='Value 7', column2='Value 8', column3='Value 9'),
    ]
    
    try:
        session.add_all(data_entries)
        session.commit()
        print("Data seeding successful!")
    except Exception as e:
        session.rollback()
        print(f"Data seeding failed: {str(e)}")
    finally:
        session.close()



    