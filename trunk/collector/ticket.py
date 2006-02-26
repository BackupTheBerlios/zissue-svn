from zope.interface import implements
from zope.interface import classProvides
from zope.app.container.btree import BTreeContainer

from interfaces import ITicket
from interfaces import ITicketContained, ITicketContainer

class Ticket(BTreeContainer):
    """A simple implementation of a ticket.

    Make sure that the ``Ticket`` implements the ``ITicket`` interface::

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(ITicket, Ticket)
      True

    Here is an example of changing the summary and description of the ticket::

      >>> ticket = Ticket()
      >>> ticket.summary
      u''
      >>> ticket.summary
      u''
      >>> ticket.summary = u'Ticket Summary'
      >>> ticket.description = u'Ticket Description'
      >>> ticket.summary
      u'Ticket Summary'
      >>> ticket.description
      u'Ticket Description'
    """

    implements(ITicket, ITicketContained, ITicketContainer)

    summary = u''
    description = u''
