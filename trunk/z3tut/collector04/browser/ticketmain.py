
from zope.formlib import form
from zope.formlib import namedtemplate
from zope.app.pagetemplate import ViewPageTemplateFile

from collector.interfaces import ITicket
from collector.interfaces import IComment
from collector.ticket import Ticket

class TicketMain(form.AddForm):

    form_fields = form.Fields(ITicket)

    template = namedtemplate.NamedTemplate('ticketmain')

    def comments(self):
        comments = []
        for name, child in self.context.items():
            if IComment.providedBy(child):
                info = {}
                info['body'] = child.body
                comments.append(info)
        return comments
    
ticket_page_template = namedtemplate.NamedTemplateImplementation(
    ViewPageTemplateFile('ticketmain.pt'),
    form.interfaces.IPageForm)
