from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from modules.table_init import *
from config.config import engine_param

engine=create_engine(engine_param)

Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()