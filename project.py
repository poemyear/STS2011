def getInputSearchText():
	print('1. get user\'s input search text')
	return 'test sample'

def doCrawlingByText(searchText):
	print('2. crawling google searched result with search text' + ': ' + searchText)

def classifySearchResult(searchResult):
	print('3. classify domain links that on current search result page')

def generateFilters():
	print('4. user will select certain domain to show only or remove from result')

def generateNewSearchLink(searchFilter):
	print('5. program will generate new search link applied with search options')

def redirectToPage(urlLink):
	print('6. redirect (or copy url to clipboard, or just return url) to genreated search url link')


def main():
	print('start program...')
	searchText = getInputSearchText()
	searchResult =  doCrawlingByText(searchText)
	searchList = classifySearchResult(searchResult)
	searchFilter = generateFilters()
	urlLink = generateNewSearchLink(searchFilter)
	redirectToPage(urlLink)
	print('exit program...')


# main
main()
