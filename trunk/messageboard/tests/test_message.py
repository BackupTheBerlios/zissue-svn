import unittest
from zope.testing.doctestunit import DocTestSuite

from zope.app.container.tests.test_icontainer import TestSampleContainer

from messageboard.message import Message


class Test(TestSampleContainer):

    def makeTestObject(self):
        return Message()

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('messageboard.message'),
        unittest.makeSuite(Test),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
