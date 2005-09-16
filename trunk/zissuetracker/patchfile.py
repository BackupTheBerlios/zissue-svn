
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

"""IPatchFile Implementation

An implementation of the IPatchFile using BTreeContainer as base.

$Id$
"""

from zope.interface import implements
from zope.app.container.btree import BTreeContainer
from zissue.interfaces import IPatchFile
from zissue.interfaces import IPatchFileContained
from zissue.interfaces import IPatchFileContainer

class PatchFile(BTreeContainer):
    """Implementation of a IPatchFile using B-Tree Container

    Make sure that the ``PatchFile`` implements the ``IPatchFile``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IPatchFile, PatchFile)
    True

    Make sure that the ``PatchFile`` implements the ``IPatchFileContained``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IPatchFileContained, PatchFile)
    True

    Make sure that the ``PatchFile`` implements the ``IPatchFileContainer``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IPatchFileContainer, PatchFile)
    True

    An example of checking the note of PatchFile:

    >>> pf = PatchFile()
    >>> pf.note
    u''
    >>> pf.note = u'MyPatchFile'
    >>> pf.note
    u'MyPatchFile'

    """
    
    implements(IPatchFile, IPatchFileContained, IPatchFileContainer)

    note = u""

