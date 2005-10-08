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

__docformat__ = 'restructuredtext'

from zope.interface import implements
from zope.app.container.btree import BTreeContainer
from zope.app.container.contained import Contained

from boom.interfaces import IMark, IMarkContained, IBookMarker

class Mark(Contained):
    """Implementation of IMark

    Make sure that the `Mark` implements the `IMark` interface::

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IMark, Mark)
      True

    Make sure that the `Mark` implements the `IMarkContained` interface:

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IMarkContained, Mark)
      True

    An example of checking the url of Mark::

      >>> mk = Mark()
      >>> mk.url
      u'http://www.zope.org'
      >>> mk.url = u'http://www.python.org'
      >>> mk.url
      u'http://www.python.org'
    
    An example of checking the description of Mark::

      >>> mk = Mark()
      >>> mk.description
      u''
      >>> mk.description = u'Zope Project Web Site'
      >>> mk.description
      u'Zope Project Web Site'
    """

    implements(IMark, IMarkContained)

    url = u"http://www.zope.org"
    description = u""


class BookMarker(BTreeContainer):
    """Implementation of IBookMarker using B-Tree Container

    Make sure that the `BookMarker` implements the `IBookMarker` interface::

      >>> from zope.interface.verify import verifyClass
      >>> verifyClass(IBookMarker, BookMarker)
      True

    An example of changing the name of BookMarker::

      >>> bm = BookMarker()
      >>> bm.name
      u''
      >>> bm.name = u'MyBookMarker'
      >>> bm.name
      u'MyBookMarker'
    """

    implements(IBookMarker)

    name = u""

