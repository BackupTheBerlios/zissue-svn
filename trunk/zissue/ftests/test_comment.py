import unittest
import common


class CommentTest(common.CommentTestCase):

    def testCommentDetails(self):
        self.testAddComment()
        response = self.publish(
            '/zt/mp/cmp/zi/cmm/@@comments.html',
            basic='mgr:mgrpw')
        body = response.getBody()
        self.checkForBrokenLinks(body, '/zt/mp/cmp/zi/cmm/@@comments.html',
                                 basic='mgr:mgrpw')
        self.assert_(body.find('My Comment') > 0)
        pass


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(CommentTest),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
