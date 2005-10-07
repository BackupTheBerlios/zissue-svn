#Unit tests for BookMarker
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
    
