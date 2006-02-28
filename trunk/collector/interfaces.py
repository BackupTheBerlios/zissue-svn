from zope.interface import Interface
from zope.schema import Text, TextLine, Field

from zope.app.container.constraints import ContainerTypesConstraint
from zope.app.container.constraints import ItemTypePrecondition
from zope.app.container.interfaces import IContained, IContainer

class IComment(Interface):
    """Comment for Ticket"""

    body = Text(
        title=u"Additional Comment",
        description=u"Body of the Comment.",
        default=u"",
        required=True)

class ITicket(IContainer):
    """A ticket object."""

    summary = TextLine(
        title=u"Summary",
        description=u"Short summary",
        default=u"",
        required=True)
    
    description = Text(
        title=u"Description",
        description=u"Full description",
        default=u"",
        required=False)

    def __setitem__(name, object):
        """Add an IComment object."""

    __setitem__.precondition = ItemTypePrecondition(IComment)


class ICollector(IContainer):
    """The collector the base object. It can only
    contain ITicket objects."""

    def __setitem__(name, object):
        """Add an ICollector object."""

    __setitem__.precondition = ItemTypePrecondition(ITicket)

    description = Text(
        title=u"Description",
        description=u"A description of the collector.",
        default=u"",
        required=False)


class ITicketContained(IContained):
    """Interface that specifies the type of objects that can contain
    tickets."""

    __parent__ = Field(
        constraint = ContainerTypesConstraint(ICollector))


class ICommentContained(IContained):
    """Interface that specifies the type of objects that can contain
    comments."""

    __parent__ = Field(
        constraint = ContainerTypesConstraint(ITicket))
