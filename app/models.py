from sqlalchemy import Column, Integer, String, ForeignKey, LargeBinary
from sqlalchemy.orm import relationship
from app.database import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    contact = Column(String(100))

    orders = relationship("Order", back_populates="customer")


class Bag(Base):
    __tablename__ = 'bags'

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    category = Column(String(100))
    description = Column(String(255))
    price = Column(Integer)
    image = Column(LargeBinary)  # ✅ STORE IMAGE AS BINARY

    orders = relationship("Order", back_populates="bag")


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    bag_id = Column(Integer, ForeignKey('bags.id'))

    customer = relationship("Customer", back_populates="orders")
    bag = relationship("Bag", back_populates="orders")