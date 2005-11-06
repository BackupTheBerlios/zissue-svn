from zissue.interfaces import IMainProduct
from zissue.interfaces import ISubProduct
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
                                    info = {}
                                    info['name'] = name2
                                    info['url'] = name+"/"+name1+"/"+name2
                                    results.append(info)

                    elif ISubProduct.providedBy(child1):
                        for name3, child3 in child1.items():
                            if IComponent.providedBy(child3):
                                for name4, child4 in child3.items():
                                    if IZissue.providedBy(child4):
                                        if child4.summary.find(searchText) >= 0:
                                            info = {}
                                            info['name'] = name4
                                            info['url'] = name+"/"+name1+"/"+name3+"/"+name4
                                            results.append(info)

        return {'results': results,
                'total': len(results)}
