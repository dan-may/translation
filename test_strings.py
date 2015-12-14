from flask.ext.babel import Babel, gettext, ngettext, pgettext, npgettext, _

def test_strings():

    # NOTE: part a1
    comment_test = _(u'first part')

    # NOTE: part b1
    comment_test_2 = _(u'second part')

    context_test = pgettext(u'Three', u'first part')
    context_test2 = pgettext(u'Four', u'second part')
