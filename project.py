import os, sys
sys.path.append(os.path.abspath(os.path.join('input')))
sys.path.append(os.path.abspath(os.path.join('output')))
sys.path.append(os.path.abspath(os.path.join('process')))
from input import *
from output import *
from process import *

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
