
from zope.formlib import form
from zope.formlib import namedtemplate
from zope.app.pagetemplate import ViewPageTemplateFile

from collector.interfaces import ITicket
from collector.ticket import Ticket

class AddTicket(form.AddForm):

    form_fields = form.Fields(ITicket)

    template = namedtemplate.NamedTemplate('ticket')

    def create(self, data):
        ticket = Ticket()
        ticket.summary = data['summary']
        ticket.description = data['description']
        return ticket
    
    def nextURL(self):
        return "../@@CollectorMain.html"
    
ticket_page_template = namedtemplate.NamedTemplateImplementation(
    ViewPageTemplateFile('ticketform.pt'),
    form.interfaces.IPageForm)
