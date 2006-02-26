from zope.interface import Interface
from zope.schema import Text, TextLine, Field

from zope.app.container.constraints import ContainerTypesConstraint
from zope.app.container.constraints import ItemTypePrecondition
from zope.app.container.interfaces import IContained, IContainer


class IMessage(Interface):
    """A message object."""

    title = TextLine(
        title=u"Title/Subject",
        description=u"Title and/or subject of the message.",
        default=u"",
        required=True)

    body = Text(
        title=u"Message Body",
        description=u"The actual message.",
        default=u"",
        required=False)


class IMessageBoard(IContainer):
    """The message board is the base object. It can only
    contain IMessage objects."""

    def __setitem__(name, object):
        """Add an IMessageBoard object."""

    __setitem__.precondition = ItemTypePrecondition(IMessage)

    description = Text(
        title=u"Description",
        description=u"A description of the content of the board.",
        default=u"",
        required=False)


class IMessageContained(IContained):
    """Interface that specifies the type of objects that can contain
    messages."""
    __parent__ = Field(
        constraint = ContainerTypesConstraint(IMessageBoard, IMessage))


class IMessageContainer(IContainer):
    """We also want to make the message object a container that can contain
    responses (other messages)."""

    def __setitem__(name, object):
        """Add an IMessage object."""

    __setitem__.precondition = ItemTypePrecondition(IMessage)
