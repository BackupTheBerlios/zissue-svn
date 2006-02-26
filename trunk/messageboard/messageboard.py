from zope.interface import implements
from zope.interface import classProvides
from zope.app.container.btree import BTreeContainer

from interfaces import IMessageBoard

class MessageBoard(BTreeContainer):
    """A very simple implementation of a message board using B-Tree Containers

    Make sure that the ``MessageBoard`` implements the ``IMessageBoard``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IMessageBoard, MessageBoard)
    True
    
    Here is an example of changing the description of the board:

    >>> board = MessageBoard()
    >>> board.description
    u''
    >>> board.description = u'Message Board Description'
    >>> board.description
    u'Message Board Description'
    """

    implements(IMessageBoard)

    # See messageboard.interfaces.IMessageBoard
    description = u''
