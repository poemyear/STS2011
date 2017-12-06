import os, sys
sys.path.append(os.path.abspath(os.path.join('input')))
sys.path.append(os.path.abspath(os.path.join('output')))
sys.path.append(os.path.abspath(os.path.join('process')))
from input import Input
from output import Output
from process import Process


def main():
    print('start program...')

    fileName = 'daily.csv'    
    api_key = '430156241533f1d058c603178cc3ca0e'

    # generate classes
    input = Input()
    process = Process(api_key)
    output = Output()
    
    # read daily box office file to DataFrame ('2003~2017')
    df = input.readDailyBoxOffice(fileName)
    df = process.updateCurrentDailyBoxOffice(fileName, df)

    while True:
        type = input.getType()

        # Box Office
        if type == 'B': 
            # input: get period & top from user
            period = input.getPeriod()
            top = input.getTop()
            # process: get top N movies from df
            topMovies = process.getTopMovies(df, period, top)
            # output: show 4 types of graphs
            output.showAudiCntGraph(topMovies, df, period, top)
            output.showAudiAccGraph(topMovies, df, period, top)
            output.showSalesAmtGraph(topMovies, df, period, top)
            output.showSalesAccGraph(topMovies, df, period, top)

        # Filmography
        elif type == 'F': 
            # input, process: get & select person
            peopleNm = input.getPeopleNm()
            peopleList = process.getPeopleList(peopleNm)  # from API
            person = input.getPerson(peopleList)
            
            # process: get filmography of input person 
            filmography = process.getFilmography(person, df)
            
            # output: show filmography graph
            output.showFilmographyGraph(peopleNm, filmography)

        # Quit 
        elif type == 'Q':
            break

    print('exit program...')

# main
if __name__ == '__main__':
    main()
