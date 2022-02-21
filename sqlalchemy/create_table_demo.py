"""
创建表
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, session

# 创建 declarative_base 对象
Base = declarative_base()


class Cookie(Base):  # 继承自Base
    __tablename__ = 'cookies'  # 定义表名
    # 定义主键
    cookie_id = Column(Integer(), primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer())
    unit_cost = Column(Numeric(12, 2))


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True)
    # 要求此列非空 要求值是唯一的
    username = Column(String(15), nullable=False, unique=True)
    email_address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    # 指定默认时间
    created_on = Column(DateTime(), default=datetime.now)
    # 修改时也将值为当前时间
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer(), primary_key=True)
    # 外键
    user_id = Column(Integer(), ForeignKey('users.user_id'))
    shipped = Column(Boolean(), default=False)
    # 建立关联关系
    user = relationship("User", backref=backref('orders', order_by=order_id))

