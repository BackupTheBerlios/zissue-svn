from zope.interface import implements
from zope.interface import classProvides
from zope.app.container.btree import BTreeContainer

from interfaces import IMessage
from interfaces import IMessageContained, IMessageContainer

class Message(BTreeContainer):
    """A simple implementation of a message.

    Make sure that the ``Message`` implements the ``IMessage`` interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IMessage, Message)
    True

    Here is an example of changing the title and description of the message:

    >>> message = Message()
    >>> message.title
    u''
    >>> message.body
    u''
    >>> message.title = u'Message Title'
    >>> message.body = u'Message Body'
    >>> message.title
    u'Message Title'
    >>> message.body
    u'Message Body'
    """
    
    implements(IMessage, IMessageContained, IMessageContainer)
    #classProvides(IAttributeAnnotatable, IContentContainer)

    # See messageboard.interfaces.IMessage
    title = u''

    # See messageboard.interfaces.IMessage
    body = u''
