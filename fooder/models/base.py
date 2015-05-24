# fooder/models/base.py
# Copyright (C) 2014-2015 the Kim authors and contributors
# <see AUTHORS file>
#
# This module is part of Kim and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

import arrow


from flask import request
from sqlalchemy import Column, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:////usr/src/app/fooder.db')  # TODO defer this and pull from app config object!
db_session = scoped_session(sessionmaker(bind=engine), scopefunc=request)

Base = declarative_base()

utc_now = lambda x: arrow.utcnow().datetime


class PrimaryKeyMixin(object):

    id = Column(String(22), primary_key=True)


class CreatedUpdatedMixin(object):

    created_at = Column(DateTime, default=utc_now, nullable=False)
    updated_at = Column(
        DateTime, default=utc_now,
        onupdate=utc_now, nullable=False)

    # hack to move the timestamp columns to the end
    created_at._creation_order = 9998
    updated_at._creation_order = 9999


class BaseMixin(PrimaryKeyMixin, CreatedUpdatedMixin):
    pass
