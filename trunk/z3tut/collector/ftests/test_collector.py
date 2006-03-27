import unittest
import doctest
from zope.app.testing.functional import FunctionalDocFileSuite

def test_suite():
    flags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    collector = FunctionalDocFileSuite('collector.txt', optionflags=flags)
    return unittest.TestSuite((collector, ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
