
from zope.formlib import form
from zope.formlib import namedtemplate
from zope.app.pagetemplate import ViewPageTemplateFile

from messageboard.interfaces import IMessage
from messageboard.message import Message

class AddMessage(form.AddForm):

    form_fields = form.Fields(IMessage)

    template = namedtemplate.NamedTemplate('message')

    def create(self, data):
        message = Message()
        message.title = data['title']
        message.body = data['body']
        return message

message_page_template = namedtemplate.NamedTemplateImplementation(
    ViewPageTemplateFile('messageform.pt'),
    form.interfaces.IPageForm)
