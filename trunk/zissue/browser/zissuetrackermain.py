#ZissueTracker main page supporting classes

class ZissueTrackerMain:

    def __init__(self, context, request, base_url=''):
        self.context = context
        self.request = request
        self.base_url = base_url

    def getName(self):
        
        return self.context.name

    name = property(getName)

    def description(self):
        return self.context.description
    pass
