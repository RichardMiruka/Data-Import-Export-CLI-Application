from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# The database connection URL
DATABASE_URL = "sqlite:///data.db"

# The engine
engine = create_engine(DATABASE_URL)

# The session factory
Session = sessionmaker(bind=engine)
