#!/usr/bin/env python3
"""
User Model
"""

from sqlalchemy.ext.declaratative import declaratative_base
from sqlalchemy import Column, Integer, String

Base = declaratative_base()


class User(Base):
    """User model"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

