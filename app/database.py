from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, Data, Table1, Table2

DB_URL = "sqlite:///data.db"
engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)

def seed_data():
    session = Session()

    existing_data = session.query(Data).count()
    if existing_data > 0:
        session.close()
        return

    data_entries = [
        Data(column1='Value 1', column2='Value 2', column3='Value 3'),
        Data(column1='Value 4', column2='Value 5', column3='Value 6'),
        Data(column1='Value 7', column2='Value 8', column3='Value 9'),
    ]

    table1_entries = [
        Table1(column1='Table1 Value 1', column2='Table1 Value 2'),
        Table1(column1='Table1 Value 3', column2='Table1 Value 4'),
        Table1(column1='Table1 Value 5', column2='Table1 Value 6'),
    ]

    table2_entries = [
        Table2(column1='Table2 Value 1', column2='Table2 Value 2'),
        Table2(column1='Table2 Value 3', column2='Table2 Value 4'),
        Table2(column1='Table2 Value 5', column2='Table2 Value 6'),
    ]

    try:
        session.add_all(data_entries)
        session.add_all(table1_entries)
        session.add_all(table2_entries)
        session.commit()
        print("Data seeding successful!")
    except Exception as e:
        session.rollback()
        print(f"Data seeding failed: {str(e)}")
    finally:
        session.close()



    