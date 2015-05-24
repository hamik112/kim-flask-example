#!/usr/bin/python
# -*- coding: utf-8 -*-

from urllib.parse import urlparse

import subprocess

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from fooder.app import create_app
from fooder.models.base import db_session

app = create_app()
migrate = Migrate(app, db_session)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.command
def dbshell():

    url = urlparse(app.config['SQLALCHEMY_DATABASE_URI'])
    cmd = 'sqlite3 {0}'.format(url.path)
    subprocess.call(cmd, shell=True)


if __name__ == "__main__":
    manager.run()
