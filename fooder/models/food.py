# fooder/models/food.py
# Copyright (C) 2014-2015 the Kim authors and contributors
# <see AUTHORS file>
#
# This module is part of Kim and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from sqlalchemy import Column, String, ForeignKey
from .base import Base, BaseMixin, db_session


class Food(Base, BaseMixin):

    __tablename__ = 'food'

    name = Column(String(300), unique=True, nullable=False)
    description = Column(String(300), nullable=False)
    type = Column(String(50), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'food',
        'polymorphic_on': 'type'
    }


class Vegetable(Food):

    __tablename__ = 'vegetable'

    id = Column(String(22), ForeignKey('food.id'), primary_key=True)
    category = Column(String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'vegetable',
    }


def get_vegetables():
    """Return all the ``Vegetables`` stored in the database.
    """

    return db_session.query(Vegetable).all()


class Fruit(Food):

    __tablename__ = 'fruit'

    id = Column(String(22), ForeignKey('food.id'), primary_key=True)
    contains_seeds = Column(String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'fruit',
    }
