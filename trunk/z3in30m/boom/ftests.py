#Functional tests for BookMarker
import unittest
from zope.app.testing.functional import BrowserTestCase

class BookMarksTest(BrowserTestCase):

    def testAddBookMarker(self):
        response = self.publish(
            '/+/AddBookMarker.html=bm',
            basic='mgr:mgrpw',
            form={'field.name': u'MyBookMarker',
                  'UPDATE_SUBMIT': 'Add'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/@@contents.html')

    def testAddMark(self):
        self.testAddBookMarker()
        response = self.publish(
            '/bm/+/AddMark.html=mrk',
            basic='mgr:mgrpw',
            form={'field.url': u'http://www.zope.org',
                  'field.description': u'Zope Project Site',
                  'UPDATE_SUBMIT': 'Add'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/bm/@@contents.html')

    def testMarksListing(self):
        self.testAddMark()
        response = self.publish(
            '/bm/@@marks.html',
            basic='mgr:mgrpw')
        body = response.getBody()
        self.checkForBrokenLinks(body, '/bm/@@marks.html',
                                 basic='mgr:mgrpw')
        self.assert_(body.find('Zope Project Site') > 0)


def test_suite():
    return unittest.TestSuite((
        unittest.makeSuite(BookMarksTest),
        ))

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
