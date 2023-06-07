from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# SQLite database file
DATABASE_FILE = 'data.db'

# SQLite connection URL
DATABASE_URL = f'sqlite:///{DATABASE_FILE}'

# Create the engine and bind the Base model to it
engine = create_engine(DATABASE_URL)
Base.metadata.bind = engine

# Create all tables defined in the models
Base.metadata.create_all()

# Create a session factory
Session = sessionmaker(bind=engine)


    