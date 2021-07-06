from sqlalchemy import Table, Column, DateTime, ForeignKey, func, Integer, String, Boolean, Text, Float, Date
from sqlalchemy.orm import relationship

from src.connection import Base

import datetime


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    title = Column(String) 


class SubCategory(Base):
    __tablename__ = 'sub_categories'

    id = Column(Integer, primary_key=True)
    title = Column(String) 
    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'))


class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(Text)
    price = Column(Float, nullable=False)
    image_url = Column(String)
    sub_category_id = Column(Integer, ForeignKey('sub_categories.id', ondelete='SET NULL'))


class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False, default=1)
    ordered = Column(Boolean, nullable=False, default=False)

    cart_id = Column(Integer, ForeignKey('carts.id', ondelete='CASCADE'))
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))
    item_id = Column(Integer, ForeignKey('items.id', ondelete='CASCADE'))


class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True)
    ordered = Column(Boolean, nullable=False, default=False)
    shipped = Column(Boolean, nullable=False, default=False)
    added_date = Column(Date, nullable=False, default=datetime.datetime.now())
    
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    cart_items = relationship('CartItem', backref='cart', lazy=False)
     

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)
    admin = Column(Boolean, nullable=False, default=False)



