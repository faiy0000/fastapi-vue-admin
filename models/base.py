
# -*- coding: utf-8 -*-
# Create time: 2021-12-12 16:21
# Project: fastapi-vue
# File: base
# Creator: faiy0000

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool


Base = declarative_base()

# 密码加密算法
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class ZcylData(object):
    def __init__(self):

        # host = zcyl_database[environment]['host']
        # user = zcyl_database[environment]['user']
        # password = zcyl_database[environment]['password']
        # database = zcyl_database[environment]['database']
        # charset = zcyl_database[environment]['charset']
        host = "127.0.0.1"
        user = "root"
        password = "123321"
        port = "3306"
        database = "fast"
        charset = "utf8"
        url = f"mysql+pymysql://{user}:{password}@{host}/{database}"
        # self.engine = create_engine(url, connect_args={'charset': charset}, pool_pre_ping=True)
        self.engine = create_engine(url, connect_args={'charset': charset}, poolclass=NullPool, pool_pre_ping=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

def base_createTable_main():
    base_data = ZcylData()
    Base.metadata.drop_all(base_data.engine)
    Base.metadata.create_all(base_data.engine)


base_data = ZcylData()

if __name__ == "__main__":
    base_createTable_main()
    #base_createTable_users()
    # check_db_result()