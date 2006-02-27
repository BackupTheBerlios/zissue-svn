
from zope.formlib import form
from zope.formlib import namedtemplate
from zope.app.pagetemplate import ViewPageTemplateFile

from collector.interfaces import ICollector
from collector.interfaces import ITicket
from collector.ticketcollector import Collector

class CollectorMain(form.AddForm):

    form_fields = form.Fields(ICollector)

    template = namedtemplate.NamedTemplate('collectormain')

    def create(self, data):
        collector = Collector()
        collector.description = data['description']
        return collector
    
    #tickets = [{"summary": "hi"}, {"summary": "ok"}]
    def tickets(self):
        tickets = []
        for name, child in self.context.items():
            if ITicket.providedBy(child):
                info = {}
                info['summary'] = child.summary
                info['description'] = child.description
                tickets.append(info)
        return tickets
    
collector_page_template = namedtemplate.NamedTemplateImplementation(
    ViewPageTemplateFile('collectormain.pt'),
    form.interfaces.IPageForm)
