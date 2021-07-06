from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from data.config import POSTGRES_URI

Base = declarative_base()
engine = create_engine(POSTGRES_URI)
session = sessionmaker(bind=engine, expire_on_commit=False, autoflush=False)




