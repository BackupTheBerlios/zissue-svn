import unittest
import common

class CommentTest(common.CommentTestCase):
    pass

def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(CommentTest),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
