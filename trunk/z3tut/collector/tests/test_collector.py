import unittest
from zope.testing.doctestunit import DocTestSuite

from zope.app.container.tests.test_icontainer import TestSampleContainer

from collector.ticketcollector import Collector


class Test(TestSampleContainer):

    def makeTestObject(self):
        return Collector()

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('collector.ticketcollector'),
        unittest.makeSuite(Test),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
