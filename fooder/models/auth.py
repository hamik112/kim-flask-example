# fooder/models/auth.py
# Copyright (C) 2014-2015 the Kim authors and contributors
# <see AUTHORS file>
#
# This module is part of Kim and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from sqlalchemy import Column, String
from passlib.hash import bcrypt

from .base import Base, BaseMixin


class User(Base, BaseMixin):
    __tablename__ = 'users'

    name = Column(String(300), nullable=False)
    email = Column(String(300), unique=True, nullable=False)
    password = Column(String, nullable=False)

    def set_password(self, password, rounds=12):
        """Hash a plain text password and set the encrypted version against
        this instance.
        :param password: hashable str
        :param rounds: Specify the number of rounds bcrypt will perform
        :returns: None
        """
        self.password = bcrypt.encrypt(password, rounds=rounds)

    def verify_password(self, password):
        """Verify an encrypted password using ``password`` as a salt.
        :param password: hashable str
        :returns: True when valid, false otherwise
        """

        if not self.password:
            return False
        return bcrypt.verify(password, self.password)
