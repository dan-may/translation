from flask import Flask
from flask.ext.babelex import Babel

babel = Babel()


def create_app():
    print 'init file'

    app = Flask(__name__)
    # config

    # insert i18n into Jinja template
    # env = Environment(extensions=['jinja2.ext.i18n'])

    # init babel (sets up Jinja extension for Flask)
    # more info: https://pythonhosted.org/Flask-Babel/#id1

    babel.init_app(app)

    from views import trans
    app.register_blueprint(trans)

    app.debug = True

    return app
