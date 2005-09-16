
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


"""IComponent Implementation

An implementation of the IComponent using BTreeContainer as base.

$Id$
"""

from zope.interface import implements
from zope.app.container.btree import BTreeContainer
from zissue.interfaces import IComponent
from zissue.interfaces import IComponentContained

class Component(BTreeContainer):
    """Implementation of a IComponent using B-Tree Container

    Make sure that the ``Component`` implements the ``IComponent``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IComponent, Component)
    True

    Make sure that the ``Component`` implements the ``IComponentContained``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IComponentContained, Component)
    True

    An example of checking the name of Sub Product:

    >>> mp = Component()
    >>> mp.name
    u''
    >>> mp.name = u'MyComponent'
    >>> mp.name
    u'MyComponent'

    An example of checking the description of Sub Product:

    >>> mp = Component()
    >>> mp.description
    u''
    >>> mp.description = u'MyComponent'
    >>> mp.description
    u'MyComponent'
    
    """
    
    implements(IComponent, IComponentContained)

    name = u""
    description = u""

