import unittest
from zope.app.testing.functional import BrowserTestCase


class CommentTestCase(BrowserTestCase):
    #zt - ZissueTracker
    #mp - MainProduct
    #sp - SubProduct
    #cmp - Component
    #zi - Zissue
    #cmm - Comment
    def testAddZissueTracker(self):
        response = self.publish(
            '/+/AddZissueTracker.html=zt',
            basic='mgr:mgrpw',
            form={'field.name': u'MyZissueTracker',
                  'field.description': u'My Zissue Tracker',
                  'UPDATE_SUBMIT': 'Add'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/@@contents.html')

    def testAddMainProduct(self):
        self.testAddZissueTracker()
        response = self.publish(
            '/zt/+/AddMainProduct.html=mp',
            basic='mgr:mgrpw',
            form={'field.name': u'MyMainProduct',
                  'field.description': u'My Main Product',
                  'UPDATE_SUBMIT': 'Add'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/zt/@@contents.html')

    def testAddComponent(self):
        self.testAddMainProduct()
        response = self.publish(
            '/zt/mp/+/AddComponent.html=cmp',
            basic='mgr:mgrpw',
            form={'field.name': u'MyComponent',
                  'field.description': u'My Component',
                  'UPDATE_SUBMIT': 'Add'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/zt/mp/@@contents.html')

    def testAddZissue(self):
        self.testAddComponent()
        response = self.publish(
            '/zt/mp/cmp/+/AddZissue.html=zi',
            basic='mgr:mgrpw',
            form={'field.summary': u'MyZissue',
                  'UPDATE_SUBMIT': 'Add'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/zt/mp/cmp/@@contents.html')

    def testAddComment(self):
        self.testAddZissue()
        response = self.publish(
            '/zt/mp/cmp/zi/+/AddComment.html=cmm',
            basic='mgr:mgrpw',
            form={'field.note': u'My Comment',
                  'UPDATE_SUBMIT': 'Add'})
        self.assertEqual(response.getStatus(), 302)
        self.assertEqual(response.getHeader('Location'),
                         'http://localhost/zt/mp/cmp/zi/@@contents.html')
        
        pass

