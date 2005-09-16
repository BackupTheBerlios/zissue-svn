
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

"""ISubProduct Implementation

An implementation of the ISubProduct using BTreeContainer as base.

$Id$
"""

from zope.interface import implements
from zope.app.container.btree import BTreeContainer
from zissue.interfaces import ISubProduct
from zissue.interfaces import ISubProductContained

class SubProduct(BTreeContainer):
    """Implementation of a ISubProduct using B-Tree Container

    Make sure that the ``SubProduct`` implements the ``ISubProduct``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(ISubProduct, SubProduct)
    True

    Make sure that the ``SubProduct`` implements the ``ISubProductContained``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(ISubProductContained, SubProduct)
    True

    An example of checking the name of Sub Product:

    >>> mp = SubProduct()
    >>> mp.name
    u''
    >>> mp.name = u'MySubProduct'
    >>> mp.name
    u'MySubProduct'

    An example of checking the description of Sub Product:

    >>> mp = SubProduct()
    >>> mp.description
    u''
    >>> mp.description = u'MySubProduct'
    >>> mp.description
    u'MySubProduct'
    
    """
    
    implements(ISubProduct, ISubProductContained)

    name = u""
    description = u""

