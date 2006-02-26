
from zope.formlib import form
from zope.formlib import namedtemplate
from zope.app.pagetemplate import ViewPageTemplateFile

from messageboard.interfaces import IMessageBoard
from messageboard.messageboard import MessageBoard

class AddMessageBoard(form.AddForm):

    form_fields = form.Fields(IMessageBoard)

    template = namedtemplate.NamedTemplate('messageboard')

    def create(self, data):
        messageboard = MessageBoard()
        messageboard.description = data['description']
        return messageboard

messageboard_page_template = namedtemplate.NamedTemplateImplementation(
    ViewPageTemplateFile('messageboardform.pt'),
    form.interfaces.IPageForm)
