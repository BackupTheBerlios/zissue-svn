
from zope.formlib import form
from zope.formlib import namedtemplate
from zope.app.pagetemplate import ViewPageTemplateFile

from collector.interfaces import IComment
from collector.comment import Comment

class AddComment(form.AddForm):

    form_fields = form.Fields(IComment)

    template = namedtemplate.NamedTemplate('comment')

    def create(self, data):
        import pdb
        pdb.set_trace()
        comment = Comment()
        comment.body = data['body']
        return comment
    
    def nextURL(self):
        return "../../@@CollectorMain.html"
    
    summary = "Hi summary"
    description = "Hi description"
    comments = {}
    
comment_page_template = namedtemplate.NamedTemplateImplementation(
    ViewPageTemplateFile('commentform.pt'),
    form.interfaces.IPageForm)
