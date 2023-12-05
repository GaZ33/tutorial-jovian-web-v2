import sqlalchemy
from sqlalchemy import create_engine, text
import os

db_connection = os.environ['DB_CONNECTION']
engine = create_engine(db_connection)

#"mysql+pymysql://root:gabriel2012@127.0.0.1/joviancareers?charset=utf8mb4"