
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

"""IZissue Implementation

An implementation of the IZissue using BTreeContainer as base.

$Id$
"""

from zope.interface import implements
from zope.app.container.btree import BTreeContainer
from zissue.interfaces import IZissue
from zissue.interfaces import IZissueContained

class Zissue(BTreeContainer):
    """Implementation of a IZissue using B-Tree Container

    Make sure that the ``Zissue`` implements the ``IZissue``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IZissue, Zissue)
    True

    Make sure that the ``Zissue`` implements the ``IZissueContained``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IZissueContained, Zissue)
    True

    An example of checking the summary of Zissue:

    >>> mp = Zissue()
    >>> mp.summary
    u''
    >>> mp.summary = u'MyZissue'
    >>> mp.summary
    u'MyZissue'

    """
    
    implements(IZissue, IZissueContained)

    summary = u""

