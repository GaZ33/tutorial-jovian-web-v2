import sqlalchemy
from sqlalchemy import create_engine, text
import os
secreto = os.environ.get('DB_CONNECTION_MYSQL')
for key, value in os.environ.items():
    print(f"{key}: {value}")
print(secreto)
#db_connection = os.environ.get['DB_CONNECTION_MYSQL']
#engine = create_engine(secreto)

#"mysql+pymysql://root:gabriel2012@127.0.0.1/joviancareers?charset=utf8mb4"