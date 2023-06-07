from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Data


# Defining the database connection URL
db_url = 'sqlite:///data.db'

# Create the database engine
engine = create_engine(db_url)

# Create a session factory
Session = sessionmaker(bind=engine)

    