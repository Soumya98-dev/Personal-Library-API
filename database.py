# imports
from sqlalchemy import create_engine

from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 1. Database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./library.db"

# 2. Create the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args= {"check_same_thread": False}
)

# 3. Create session factory
SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

# 4. Create Base
class Base(DeclarativeBase):
    pass

# 5. Function to provide database sessions
def get_db():
    with SessionLocal() as db:
        yield db