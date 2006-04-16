
from zope.app.catalog.interfaces import ICatalog
from zope.app import zapi

CATALOG = 'cat1'

class CollectorSearch:

    def searchSimpleText(self):
        catalog = zapi.getUtility(ICatalog, CATALOG)
        searchText = self.request.get('searchText', '')

        result = catalog.searchResults(TextIndex=searchText)
        gen = iter(result)
        print gen.next()

        results = [{'name': 'test',
                    'url': 'turl'}]
        
        return {'results': results,
                'total': len(results)}
    pass
