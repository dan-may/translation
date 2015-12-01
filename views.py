from flask import Flask, render_template, json, request, jsonify
from flask.ext.babel import Babel, gettext, ngettext, pgettext, npgettext, lazy_gettext, lazy_pgettext, _, get_locale
from config import LANGUAGES

import random

app = Flask(__name__)
# config
app.debug = True
# insert i18n into Jinja template
# env = Environment(extensions=['jinja2.ext.i18n'])

# init babel (sets up Jinja extension for Flask)
# more info: https://pythonhosted.org/Flask-Babel/#id1
babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'fr'
    # return request.accept_languages.best_match(LANGUAGES.keys())


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/fruits')
@app.route('/fruits/<int:number>')
def fruits(number=1):
    # some server side data (analogous to titles in card_generators)

    # NOTE: this is a comment the translators will see; directing them to not translate the replacement string
    singular = gettext('Here is a basic string to translate')
    # however comments without the 'NOTE:' comment tag will not be processed into the POT file

    # notice that singular strings that use gettext() are aliased to _() for brevity
    singular_replacement = _('Here is a string that has a %(replacement)s string', replacement='replacement')

    # when we have a plural, we have to use ngettext()
    num_pears = random.randint(1, 10)
    plural = ngettext('Here is %(num)s pear', 'Here are %(num)s pears', num=num_pears)

    # we can also send a context to the translator to give them more info on what they are translating
    singular_context = pgettext('This text is part of a button used for exiting a pop-up', 'Cancel')

    plural_context = npgettext('This is part of a spinner on a fruit wheel',
                               'A lovely pair of oranges',
                               'A lovely trio of oranges',
                               number or 1)

    data = [
        {
            'fruit': _('lime'),
            'type': _('continental')
        },
        {
            'fruit': _('starfruit'),
            'type': _('exotic')
        },
        {
            'fruit': _('strawberry'),
            'type': _('native')
        },
        {'list': [
            {
                'string': singular
            },
            {
                'string': singular_replacement
            },
            {
                'string': plural
            },
            {
                'string': singular_context
            },
            {
                'string': plural_context
            }
        ]}
    ]
    print data
    return render_template('fruits.html', number=number, data=data)


@app.route('/fruits-angular')
def fruits_angular():
    return render_template('fruits-angular.html')


if __name__ == '__main__':
    app.run()
