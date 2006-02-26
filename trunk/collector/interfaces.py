from zope.interface import Interface
from zope.schema import Text, TextLine, Field

from zope.app.container.constraints import ContainerTypesConstraint
from zope.app.container.constraints import ItemTypePrecondition
from zope.app.container.interfaces import IContained, IContainer


class ITicket(Interface):
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
        constraint = ContainerTypesConstraint(ICollector, ITicket))


class ITicketContainer(IContainer):
    """We also want to make the ticket object a container that can contain
    tickets."""

    def __setitem__(name, object):
        """Add an ITicket object."""

    __setitem__.precondition = ItemTypePrecondition(ITicket)
