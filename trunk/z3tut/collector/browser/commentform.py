
from zope.formlib import form
from zope.formlib import namedtemplate
from zope.app.pagetemplate import ViewPageTemplateFile

from collector.interfaces import IComment
from collector.comment import Comment

class AddComment(form.AddForm):

    form_fields = form.Fields(IComment)

    template = namedtemplate.NamedTemplate('comment')

    def create(self, data):
        comment = Comment()
        comment.body = data['body']
        return comment
    
    def nextURL(self):
        return "../../@@CollectorMain.html"
    
    def comments(self):
        ticket = self.context.__parent__
        comments = []
        for name, child in ticket.items():
            if IComment.providedBy(child):
                info = {}
                info['body'] = child.body
                comments.append(info)
        return comments
    
    def summary(self):
        ticket = self.context.__parent__
        return ticket.summary
    
    def description(self):
        ticket = self.context.__parent__
        return ticket.description
    pass

comment_page_template = namedtemplate.NamedTemplateImplementation(
    ViewPageTemplateFile('commentform.pt'),
    form.interfaces.IPageForm)
