
from zope.formlib import form
from zope.formlib import namedtemplate
from zope.app.pagetemplate import ViewPageTemplateFile

from collector.interfaces import ICollector
from collector.ticketcollector import Collector

class AddCollector(form.AddForm):

    form_fields = form.Fields(ICollector)

    template = namedtemplate.NamedTemplate('collector')

    def create(self, data):
        collector = Collector()
        collector.description = data['description']
        return collector

collector_page_template = namedtemplate.NamedTemplateImplementation(
    ViewPageTemplateFile('collectorform.pt'),
    form.interfaces.IPageForm)
