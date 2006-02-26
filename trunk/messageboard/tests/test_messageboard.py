import unittest
from zope.testing.doctestunit import DocTestSuite

from zope.app.container.tests.test_icontainer import TestSampleContainer

from messageboard.messageboard import MessageBoard


class Test(TestSampleContainer):

    def makeTestObject(self):
        return MessageBoard()

def test_suite():
    return unittest.TestSuite((
        DocTestSuite('messageboard.messageboard'),
        unittest.makeSuite(Test),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
