# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

Session = sessionmaker(bind=engine)

#session = Session()

Base = declarative_base()