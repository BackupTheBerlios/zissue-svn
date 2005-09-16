
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


"""IMainProduct Implementation

An implementation of the IMainProduct using BTreeContainer as base.

$Id$
"""

from zope.interface import implements
from zope.app.container.btree import BTreeContainer
from zissue.interfaces import IMainProduct
from zissue.interfaces import IMainProductContained

class MainProduct(BTreeContainer):
    """Implementation of a IMainProduct using B-Tree Container

    Make sure that the ``MainProduct`` implements the ``IMainProduct``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IMainProduct, MainProduct)
    True

    Make sure that the ``MainProduct`` implements the ``IMainProductContained``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IMainProductContained, MainProduct)
    True

    An example of checking the name of Main Product:

    >>> mp = MainProduct()
    >>> mp.name
    u''
    >>> mp.name = u'MyMainProduct'
    >>> mp.name
    u'MyMainProduct'

    An example of checking the description of Main Product:

    >>> mp = MainProduct()
    >>> mp.description
    u''
    >>> mp.description = u'MyMainProduct'
    >>> mp.description
    u'MyMainProduct'
    
    """
    
    implements(IMainProduct, IMainProductContained)

    name = u""
    description = u""

