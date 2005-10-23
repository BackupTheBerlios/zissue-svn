
## Copyright 2005 Baiju M <baiju.m.mail@gmail.com>

## This file is part of ZissueTracker.

## ZissueTracker is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## ZissueTracker is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with ZissueTracker; if not, write to the Free Software
## Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from zope.interface import Interface
from zope.schema import Text, TextLine, Field

from zope.app.container.constraints import ContainerTypesConstraint
from zope.app.container.constraints import ItemTypePrecondition
from zope.app.container.interfaces import IContained, IContainer
from zope.app.file.interfaces import IFile

class INote(Interface):
    """Base interface for a comment/reply."""

    note = Text(
        title=u"Additional comment/reply.",
        description=u"Comment/reply by user/programmer.",
        default=u"",
        required=False)


class IComment(INote):
    """Comment is container see below."""
    pass

#class IPatchFile(INote, IFile):
class IPatchFile(INote):
    """PatchFile is a container see below."""
    #FIXME: How to make use IFile, use as adapter? or extend?
    pass


class IZissue(IContainer):
    """This container will collect comments or patch files."""

    def __setitem__(name, obj):
        pass

    __setitem__.precondition = ItemTypePrecondition(IComment, IPatchFile)

    summary = TextLine(
        title=u"Summary/Subject",
        description=u"Summary and/or subject of the zissue.",
        default=u"",
        required=True)


class IComponent(IContainer):

    def __setitem__(name, obj):
        pass

    __setitem__.precondition = ItemTypePrecondition(IZissue)

    name = TextLine(
        title=u"Name of Component",
        description=u"Name of Component.",
        default=u"",
        required=True)

    description = Text(
        title=u"Description",
        description=u"A detailed description of the component.",
        default=u"",
        required=False)

class IProduct(IContainer):

    name = TextLine(
        title=u"Name of Product",
        description=u"Name of Product.",
        default=u"",
        required=True)

    description = Text(
        title=u"Description",
        description=u"A detailed description of the product.",
        default=u"",
        required=False)


class ISubProduct(IProduct):

    def __setitem__(name, obj):
        pass

    __setitem__.precondition = ItemTypePrecondition(IComponent)


class IMainProduct(IProduct):

    def __setitem__(name, obj):
        pass

    __setitem__.precondition = ItemTypePrecondition(ISubProduct, IComponent)


class IZissueTracker(IContainer):

    name = TextLine(
        title=u"Name of Zissue Tracker",
        description=u"Name of Zissue Tracker.",
        default=u"",
        required=True)

    description = Text(
        title=u"Description",
        description=u"A detailed description of the Zissue Tracker.",
        default=u"",
        required=False)

    def __setitem__(name, obj):
        pass

    __setitem__.precondition = ItemTypePrecondition(IMainProduct)

    
class ICommentContained(IContained):

    __parent__ = Field(
        constraint = ContainerTypesConstraint(IComment, IPatchFile, IZissue))


class ICommentContainer(IContainer):
    """Make the comment object a container that can contain
    replies/comments and patch files."""

    def __setitem__(name, object):
        pass

    __setitem__.precondition = ItemTypePrecondition(IComment, IPatchFile)


class IPatchFileContained(IContained):

    __parent__ = Field(
        constraint = ContainerTypesConstraint(IComment, IPatchFile, IZissue))


class IPatchFileContainer(IContainer):
    """Make the patch file object a container that can contain
    replies/comments and other (may be modified) patch files."""

    def __setitem__(name, object):
        pass

    __setitem__.precondition = ItemTypePrecondition(IComment, IPatchFile)


class IZissueContained(IContained):
    """Interface that specifies the type of objs that can contain
    zissues."""

    __parent__ = Field(
        constraint = ContainerTypesConstraint(IComponent))


class IComponentContained(IContained):
    """Interface that specifies the type of objs that can contain
    zissues."""

    __parent__ = Field(
        constraint = ContainerTypesConstraint(ISubProduct, IMainProduct))


class ISubProductContained(IContained):

    __parent__ = Field(
        constraint = ContainerTypesConstraint(IMainProduct))


class IMainProductContained(IContained):

    __parent__ = Field(
        constraint = ContainerTypesConstraint(IZissueTracker))

