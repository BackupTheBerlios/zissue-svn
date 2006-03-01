from collector.interfaces import ITicket

class CollectorMain:

    def tickets(self):
        tickets = []
        for name, child in self.context.items():
            if ITicket.providedBy(child):
                info = {}
                info['summary'] = child.summary
                info['description'] = child.description
                info['name'] = child.__name__ + "/@@+/AddComment.html"
                tickets.append(info)
        return tickets
