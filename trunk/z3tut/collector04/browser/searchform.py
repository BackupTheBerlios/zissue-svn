
class CollectorSearch:
    
    def searchSimpleText(self):
        searchText = self.request.get('searchText', '')
        results = [{'name': 'test',
                    'url': 'turl'}]
        
        return {'results': results,
                'total': len(results)}
    pass
