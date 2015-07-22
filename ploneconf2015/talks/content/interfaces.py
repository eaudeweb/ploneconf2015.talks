""" Content interfaces
"""
from zope import schema
from zope.interface import Interface
from plone.namedfile import field as namedfile
from plone.supermodel import model

class ITalkStorage(Interface):
    """ Marker interface for talks storage
    """


class ITalk(model.Schema):
    """ Talk schema
    """
    target_audience = schema.List(
        title=u"Target audience",
        value_type=schema.TextLine(title=u"Target Audience Tag",
                                   default=u""),
        required=True
    )

    room = schema.TextLine(
        title=u"Room",
        default=u"",
        required=False
    )


class ISpeaker(model.Schema):
    """ Speaker schema
    """
    email = schema.TextLine(
        title=u"E-mail Address",
        default=u"",
        required=True
    )

    country = schema.TextLine(
        title=u"Country",
        default=u"",
        required=True
    )

    company = schema.TextLine(
        title=u"Company / Organization",
        default=u"",
        required=False
    )

    twitter = schema.TextLine(
        title=u"Twitter",
        default=u"",
        required=False
    )

    git = schema.TextLine(
        title=u"GitHub account",
        default=u"",
        required=False
    )

    linkedin = schema.TextLine(
        title=u"LinkedIn",
        default=u"",
        required=False
    )

    image = namedfile.NamedBlobImage(
        title=u"Picture",
        description=u"",
        required=False,
    )

    first_time = schema.Bool(
        title=u"First Time",
        description=u"",
        default=False,
        required=False
    )

    buddy = schema.Bool(
        title=u"Buddy",
        description=u"",
        default=False,
        required=False
    )