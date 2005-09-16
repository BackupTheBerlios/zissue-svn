
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

"""IZissueTracker Implementation

An implementation of the IZissueTracker using BTreeContainer as base.

$Id$
"""

from zope.interface import implements
from zope.app.container.btree import BTreeContainer
from zissue.interfaces import IZissueTracker

class ZissueTracker(BTreeContainer):
    """Implementation of a IZissueTracker using B-Tree Container

    Make sure that the ``ZissueTracker`` implements the ``IZissueTracker``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IZissueTracker, ZissueTracker)
    True

    An example of changing the name of Zissue Tracker:

    >>> zit = ZissueTracker()
    >>> zit.name
    u''
    >>> zit.name = u'MyZissueTracker'
    >>> zit.name
    u'MyZissueTracker'

    An example of changing the description of Zissue Tracker:

    >>> zit = ZissueTracker()
    >>> zit.description
    u''
    >>> zit.description = u'My Zissue Tracker'
    >>> zit.description
    u'My Zissue Tracker'
    """

    implements(IZissueTracker)

    name = u""
    description = u""
