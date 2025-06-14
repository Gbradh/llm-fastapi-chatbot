from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Use SQLite file-based DB
DATABASE_URL = "sqlite:///./customers.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Create tables
def create_tables():
    Base.metadata.create_all(bind=engine)
