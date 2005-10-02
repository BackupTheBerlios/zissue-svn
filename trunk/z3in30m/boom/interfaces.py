## Copyright 2005 Baiju M <baiju.m.mail@gmail.com>

## This file is part of BookMarker.

## BookMarker is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.

## BookMarker is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with BookMarker; if not, write to the Free Software
## Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""BookMarker interfaces
"""

from zope.interface import Interface
from zope.schema import Text, TextLine, Field

from zope.app.container.constraints import ContainerTypesConstraint
from zope.app.container.constraints import ItemTypePrecondition
from zope.app.container.interfaces import IContained, IContainer

class IMark(Interface):
    """This is a book mark."""

    url = TextLine(
        title=u"URL/Link",
        description=u"URL of the website",
        default=u"http://www.zope.org",
        required=True)

    description = Text(
        title=u"Description",
        description=u"Description of the website",
        default=u"",
        required=False)

class IBookMarker(IContainer):
    """This is the container for all Marks."""

    name = TextLine(
        title=u"Name of BookMarker",
        description=u"Name of BookMarker",
        default=u"",
        required=True)

    def __setitem__(name, obj):
        pass

    __setitem__.precondition = ItemTypePrecondition(IMark)


class IMarkContained(IContained):
    """An Mark can only put in a BookMarker"""

    __parent__ = Field(
        constraint = ContainerTypesConstraint(IBookMarker))
