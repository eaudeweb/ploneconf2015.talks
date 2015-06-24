""" Content interfaces
"""
from zope import schema
from zope.interface import Interface
from plone.supermodel import model


class ITalk(model.Schema):
    """ Talk schema
    """
    title = schema.Text(
        title=u"Title",
        default=u"",
    )

    summary = schema.Text(
        title=u"Summary",
        default=u"",
    )

    author_name = schema.TextLine(
        title=u"Author name",
        default=u""
    )

    author_email = schema.TextLine(
        title=u"Author email",
        default=u""
    )

    about = schema.TextLine(
        title=u"About the author",
        default=u""
    )