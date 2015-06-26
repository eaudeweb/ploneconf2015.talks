""" Talks interfaces
"""
from ploneconf2015.talks.content.interfaces import ITalk, ISpeaker, ITalkStorage
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

class IPloneconf2015TalksLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""
