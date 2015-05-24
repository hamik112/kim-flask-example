# fooder/config.py
# Copyright (C) 2014-2015 the Kim authors and contributors
# <see AUTHORS file>
#
# This module is part of Kim and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from os import path, environ


class Config(object):
    DEBUG = False
    PORT = 5000
    HOST = "0.0.0.0"
    SQLALCHEMY_ECHO = True
    BASE_URL = "http://fooder.com"
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    TEMPLATE_FOLDER = path.join(PROJECT_ROOT, 'templates')


def build_db_url(user=None, password=None, addr=None, name=None):
    tmpl = "postgresql://{DB_USER}:{DB_PASS}@{DB_ADDR}/{DB_NAME}"
    return tmpl.format(DB_USER=user or 'postgres',
                       DB_PASS=password or 'root',
                       DB_ADDR=addr or 'localhost',
                       DB_NAME='postgres')


class DEV(Config):
    DEBUG = True
    SECRET_KEY = "c1893e25-88ec-4ec2-b2fe-4c213413df25"
    SQLALCHEMY_DATABASE_URI = 'sqlite:////usr/src/app/fooder.db'


class TEST(Config):
    SECRET_KEY = "2147d2df-759b-40ac-8013-f6154110a7d0"
    TESTING = True
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = \
        build_db_url(name='postgres_test',
                     addr=environ.get('DB_PORT_5432_TCP_ADDR'))


settings = globals()[environ.get('FOODER_CONFIG', 'DEV')]
