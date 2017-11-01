from urllib.parse import urlparse
from collections import Counter
class Process:
    def classifySearchResult(self, searchResult):
        domains = []
        for key, value in searchResult.items():
            parsed_uri = urlparse(value.split('/url?q=')[1])
            domains.append('{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri))
        # print('3. classify domain links that on current search result page')
        return Counter(domains)

    def generateFilters(self, searchList, n):
        filters = ["-site:" + tup[0] for tup in searchList.most_common(n)]
        # print('4. user will select certain domain to show only or remove from result')
        return filters

    def generateNewSearchLink(self, searchText, searchFilter):
        # print('5. program will generate new search link applied with search options')
        newText = searchText + ' ' + ' '.join(searchFilter)
        url = 'https://www.google.co.kr/search?q='+newText+'sourceid=chrome&ie=UTF-8/'
        return url


