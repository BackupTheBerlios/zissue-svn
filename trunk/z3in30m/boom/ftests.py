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

"""Functional tests for BookMarker."""

import unittest
from zope.app.testing.functional import BrowserTestCase

class BookMarksTest(BrowserTestCase):

    def testAddBookMarker(self):
        response = self.publish(
            '/+/AddBookMarker.html=bm',
            basic='mgr:mgrpw',
            form={'field.name': u'MyBookMarker',
                  'UPDATE_SUBMIT': 'Add'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/@@contents.html')

    def testAddMark(self):
        self.testAddBookMarker()
        response = self.publish(
            '/bm/+/AddMark.html=mrk',
            basic='mgr:mgrpw',
            form={'field.url': u'http://www.zope.org',
                  'field.description': u'Zope Project Site',
                  'UPDATE_SUBMIT': 'Add'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/bm/@@contents.html')

    def testMarksListing(self):
        self.testAddMark()
        response = self.publish(
            '/bm/@@marks.html',
            basic='mgr:mgrpw')
        body = response.getBody()
        self.checkForBrokenLinks(body, '/bm/@@marks.html',
                                 basic='mgr:mgrpw')
        self.assert_(body.find('Zope Project Site') > 0)


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(BookMarksTest),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
