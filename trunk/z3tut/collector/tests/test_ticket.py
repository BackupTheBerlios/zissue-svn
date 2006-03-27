import unittest
from zope.testing.doctestunit import DocTestSuite

from zope.app.container.tests.test_icontainer import TestSampleContainer

from collector.ticket import Ticket


class Test(TestSampleContainer):

    def makeTestObject(self):
        return Ticket()

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('collector.ticket'),
        unittest.makeSuite(Test),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
