#Functional tests for BookMarker
import unittest
from zope.app.testing.functional import BrowserTestCase

class BookMarksTest(BrowserTestCase):

    def testMarksListing(self):
        pass


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(BookMarksTest),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
