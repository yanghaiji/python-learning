from sqlalchemy import create_engine

"""
创建数据库连接引擎
"""
# mysql
engine = create_engine('mysql+pymysql://cookiemonster:chocolatechip'
                       '@mysql01.monster.internal/cookies', pool_recycle=3600)

# pgsql
engine_pg = create_engine('postgresql+psycopg2://username:password@localhost:5432/mydb')

# sqlite
engine_sql = create_engine('sqlite:///cookies.db')
engine2 = create_engine('sqlite:///:memory:')
engine3 = create_engine('sqlite:////home/cookiemonster/cookies.db')
engine4 = create_engine('sqlite:///c:\\Users\\cookiemonster\\cookies.db')
