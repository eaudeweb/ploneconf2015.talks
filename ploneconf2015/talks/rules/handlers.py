""" Content rules handlers
"""
from plone.app.contentrules.handlers import execute

def submit_talk(event):
    """ Execute inline comment
    """
    execute(event.object, event)
