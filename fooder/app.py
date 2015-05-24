# fooder/app.py
# Copyright (C) 2014-2015 the Kim authors and contributors
# <see AUTHORS file>
#
# This module is part of Kim and is released under
# the MIT License: http://www.opensource.org/licenses/mit-license.php

from os import environ

from flask import Flask, url_for, redirect

from fooder.models.base import db_session
from fooder.api.views import api_mod


def create_app(config_name='DEV'):
    """Flask app factory.

    Useage::

        from fooder.app import create_app
        def run():
            app = create_app(config_name='STAGE')
            app.run(host='0.0.0.0', port=5000, debug=app.debug)

        if __name__=="__main__":
            run()

    :param config_name: manually provide the name of the config object to use
        when creating the :py:class:``flask.Flask`` instance.  Defaults to
        os.environ['fooder_CONFIG']

    :rtype: :py:class:``flask.Flask``
    :returns: A new :py:class:``flask.Flask`` application instance
    """
    global db_session

    app = Flask(__name__)

    if config_name is not None:
        environ['FOODER_CONFIG'] = config_name

    app.config.from_object('fooder.config.settings')
    app.template_folder = app.config.get('TEMPLATE_FOLDER', 'templates')
    app.register_blueprint(api_mod, url_prefix='/v1')

    # Close the db session as app request context is torn down.
    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return redirect(url_for('api.home'))

    return app
