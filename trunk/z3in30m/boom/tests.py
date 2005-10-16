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

"""Unit tests for BookMarker."""

import unittest
from zope.testing.doctestunit import DocTestSuite

from zope.app.container.tests.test_icontainer import TestSampleContainer

from boom.bookmarker import BookMarker, Mark


class BookMarkerContainerTest(TestSampleContainer):
    
    def makeBookMarkerObject(self):
        return BookMarker()

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('boom.bookmarker'),
        unittest.makeSuite(BookMarkerContainerTest),
        ))
            
if __name__ == '__main__':
    unittest.main(defaultTest='test_suite') 
    
