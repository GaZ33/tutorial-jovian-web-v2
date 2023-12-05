import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:gabriel2012@127.0.0.1/joviancareers?charset=utf8mb4")

