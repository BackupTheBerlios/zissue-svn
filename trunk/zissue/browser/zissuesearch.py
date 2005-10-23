from zissue.interfaces import IMainProduct
from zissue.interfaces import IComponent
from zissue.interfaces import IZissue

class ZissueSearch:

    def searchSimpleText(self):
        searchText = self.request.get('searchText', '')
        results = []
        for name, child in self.context.items():
            if IMainProduct.providedBy(child):
                for name1, child1 in child.items():
                    if IComponent.providedBy(child1):
                        for name2, child2 in child1.items():
                            if IZissue.providedBy(child2):
                                if child2.summary.find(searchText) >= 0:
                                    results.append(name2)

                    elif ISubProduct.providedBy(child1):
                        for name3, child3 in child.items():
                            if IComponent.providedBy(child3):
                                for name4, child4 in child3.items():
                                    if IZissue.providedBy(child4):
                                        if child4.summary.find(searchText) >= 0:
                                            results.append(name4)

        return {'results': results,
                'total': len(results)}
