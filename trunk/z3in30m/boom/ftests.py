#Functional tests for BookMarker
import unittest
from zope.app.testing.functional import BrowserTestCase

class MarkTest(BrowserTestCase):

    def testMarkDetails(self):
        pass


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(MarkTest),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
