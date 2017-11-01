import os, sys
sys.path.append(os.path.abspath(os.path.join('input')))
sys.path.append(os.path.abspath(os.path.join('output')))
sys.path.append(os.path.abspath(os.path.join('process')))
from input import Input
from output import Output
from process import Process


def main():
    print('start program...')
    input = Input()
    output = Output()
    process = Process()

    searchText = input.getInputSearchText()
    # print(searchText)
    searchResult =  input.doCrawlingByText(searchText)
    # print(searchResult)
    searchList = process.classifySearchResult(searchResult)
    # print(searchList)
    searchFilter = process.generateFilters(searchList, 3)
    # print(searchFilter)
    urlLink = process.generateNewSearchLink(searchText, searchFilter)
    # print(urlLink)
    out = output.redirectToPage(urlLink)
    # print(out)
    
    print('exit program...')


# main
main()
