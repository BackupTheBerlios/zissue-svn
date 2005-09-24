from zope.app.pagetemplate.viewpagetemplatefile import ViewPageTemplateFile
from zissue.interfaces import IComment

class ZissueDetails:

    def __init__(self, context, request, base_url=''):
        self.context = context
        self.request = request
        self.base_url = base_url

    def listContentInfo(self):
        children = []
        for name, child in self.context.items():
            if IComment.providedBy(child):
                info = {}
                info['note'] = child.note
                url = "%s%s%s" % (self.base_url, name, '/')
                info['url'] = url + '@@comments.html'
                thread = ZissueDetails(child, self.request, url)
                info['thread'] = thread.additional()
                children.append(info)
        return children

    additional = ViewPageTemplateFile('additional.pt')
