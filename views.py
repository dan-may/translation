import random

from flask import render_template, jsonify, request, Blueprint
from flask.ext.babelex import gettext, ngettext, pgettext, npgettext, _
from flask.json import dumps
from __init__ import babel, create_app
from config import LANGUAGES

trans = Blueprint("trans", __name__)

print 'running through views'


@babel.localeselector
def get_locale():
    print "hi"
    # for testing, hard code the language to show
    # return 'fr'
    print request.accept_languages
    # in production use the below to change language based on http 'accept-languages' header:
    return request.accept_languages.best_match(LANGUAGES.keys())


@trans.route('/')
def hello_world():
    return _(u'Hello World!')


@trans.route('/fruits')
@trans.route('/fruits/<int:number>')
def fruits(number=1):
    # some server side data (analogous to title strings in card_generators)

    # NOTE: this is a comment the translators will see; directing them to not translate the replacement string
    singular = gettext(u'Here is a basic string to translate')
    # however comments without the 'NOTE:' comment tag will not be processed into the POT file

    # notice that singular strings that use gettext() are aliased to _() for brevity
    singular_replacement = _(u'Here is a string that has a %(replacement)s string', replacement=u'replacement')

    # when we have a plural, we have to use ngettext()
    num_pears = random.randint(1, 10)
    plural = ngettext(u'Here is %(num)s pear', u'Here are %(num)s pears', num=num_pears)

    # we can also send a context to the translator to give them more info on what they are translating
    singular_context = pgettext(u'This text is part of a button used for exiting a pop-up', u'Cancel')

    plural_context = npgettext(u'This is part of a spinner on a fruit wheel',
                               u'%(num)s orange',
                               u'%(num)s oranges',
                               num=(number or 1))

    # NOTE: part a
    comment_test = _(u'first part')

    # NOTE: part b
    comment_test_2 = _(u'second part')

    context_test = pgettext(u'One', u'first part')
    context_test2 = pgettext(u'Two', u'second part')


    data = {
               'fruits': [
                   {
                       'fruit': _(u'lime'),
                       'type': _(u'continental')
                   },
                   {
                       'fruit': _(u'starfruit'),
                       'type': _(u'exotic')
                   },
                   {
                       'fruit': _(u'strawberry'),
                       'type': _(u'native')
                   }
               ],
                'list': [
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
                ]
           }

    return render_template('fruits.html', number=number, data=data)


@trans.route('/fruits-json')
@trans.route('/fruits-json/<int:number>')
def fruits_json(number=1):
    # duplicating the strings already set in the first view, to test how babel handles duplication

    # NOTE: this is a comment the translators will see; directing them to not translate the replacement string
    singular = gettext(u'Here is a basic string to translate')
    # however comments without the 'NOTE:' comment tag will not be processed into the POT file

    # notice that singular strings that use gettext() are aliased to _() for brevity
    singular_replacement = _(u'Here is a string that has a %(replacement)s string', replacement=u'replacement')

    # when we have a plural, we have to use ngettext()
    num_pears = random.randint(1, 10)
    plural = ngettext(u'Here is %(num)s pear', u'Here are %(num)s pears', num=num_pears)

    # we can also send a context to the translator to give them more info on what they are translating
    singular_context = pgettext(u'This text is part of a button used for exiting a pop-up', u'Cancel')

    plural_context = npgettext(u'This is part of a spinner on a fruit wheel',
                               u'%(num)s orange',
                               u'%(num)s oranges',
                               num=(number or 1))

    data = {
           'fruits': [
               {
                   'fruit': _(u'lime'),
                   'type': _(u'continental')
               },
               {
                   'fruit': _(u'starfruit'),
                   'type': _(u'exotic')
               },
               {
                   'fruit': _(u'strawberry'),
                   'type': _(u'native')
               }
           ],
            'list': [
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
            ]
       }

    # JSON Response
    return jsonify(data)


@trans.route('/fruits-angular')
def fruits_angular():
    return render_template('fruits-angular.html')

