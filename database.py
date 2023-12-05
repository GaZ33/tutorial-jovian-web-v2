import sqlalchemy
from sqlalchemy import create_engine, text
import os

engine = create_engine("mysql+pymysql://root:teste123@127.0.0.1/joviancareers?charset=utf8mb4")
