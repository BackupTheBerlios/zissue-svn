
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


"""IComment Implementation

An implementation of the IComment using BTreeContainer as base.

$Id$
"""

from zope.interface import implements
from zope.app.container.btree import BTreeContainer
from zissue.interfaces import IComment
from zissue.interfaces import ICommentContained
from zissue.interfaces import ICommentContainer

class Comment(BTreeContainer):
    """Implementation of a IComment using B-Tree Container

    Make sure that the ``Comment`` implements the ``IComment``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(IComment, Comment)
    True

    Make sure that the ``Comment`` implements the ``ICommentContained``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(ICommentContained, Comment)
    True

    Make sure that the ``Comment`` implements the ``ICommentContainer``
    interface:

    >>> from zope.interface.verify import verifyClass
    >>> verifyClass(ICommentContainer, Comment)
    True

    An example of checking the note of Comment:

    >>> cm = Comment()
    >>> cm.note
    u''
    >>> cm.note = u'MyComment'
    >>> cm.note
    u'MyComment'

    """
    
    implements(IComment, ICommentContainer, ICommentContained)

    note = u""

    def sizeForDisplay(self):
        return '1 item'

