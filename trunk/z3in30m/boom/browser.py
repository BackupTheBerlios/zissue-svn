#Web views module

from boom.interfaces import IMark

class BookMarks:

    def __init__(self, context, request, base_url=''):
        self.context = context
        self.request = request
        self.base_url = base_url

    def listMarks(self):
        marks = []
        for name, child in self.context.items():
            if IMark.providedBy(child):
                info = {}
                info['url'] = child.url
                info['description'] = child.description
                marks.append(info)
        return marks
