
import unittest
from zope.testing.doctestunit import DocTestSuite

from zope.app.container.tests.test_icontainer import TestSampleContainer

from zissue.zissuetracker.tracker import ZissueTracker


class TestZissueTrackerContainer(TestSampleContainer):
    
    def makeTestObject(self):
        return ZissueTracker()
    
def test_suite():
    return unittest.TestSuite((
        DocTestSuite('zissue.zissuetracker.tracker'),
        unittest.makeSuite(TestZissueTrackerContainer),
        ))
            
if __name__ == '__main__':
    unittest.main(defaultTest='test_suite') 
    
