#!/usr/bin/python3.6
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text
from config import config

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(50))
    hosts = Column(Text, default="{'sudo': [], 'no-sudo': []}")

class Host(Base):
    __tablename__ = 'host'
    id = Column(Integer, autoincrement=True, primary_key=True)
    ip = Column(String(50))
    port = Column(Integer, default=22)

class Cmd_log(Base):
    __tablename__ = 'cmd_log'
    id = Column(Integer, autoincrement=True, primary_key=True)
    login_user = Column(String(16))
    share_user = Column(String(16))
    server_ip =Column(String(50))
    shell_command = Column(String(255))
    datetime = Column(String(30))

if __name__ == "__main__":
    engine=create_engine(config.engine_param)
    Base.metadata.create_all(engine)
    