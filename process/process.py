from datetime import datetime, timedelta
import requests
import pandas as pd

class Process:

    # Base Url for API
    base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/'
    
    # Using API Key 
    def __init__(self, api_key):
        self.key = api_key

    # API Call to /people/searchPeopleList.json
    def getPeopleList (self, peopleNm):
        result = requests.get(url = Process.base_url + 'people/searchPeopleList.json', params = {'key': self.key, 'peopleNm': peopleNm})
        return result.json()['peopleListResult']['peopleList']

    # Parsing filmography as DataFrame
    def getFilmography (self, person, df):
        filmography = []
        for movieNm in person['filmoNames'].split('|') :
            if movieNm in df['movieNm'].unique():
                # dfMovie is each movieNm's DataFrame
                dfMovie = df.where(df['movieNm'] == movieNm).dropna()
                audiAcc = int(dfMovie['audiAcc'].max())
                salesAcc = int(dfMovie['salesAcc'].max())
                openDt = dfMovie['targetDt'].min()
                filmography.append({'movieNm':movieNm, 'openDt':openDt, 'audiAcc': audiAcc, 'salesAcc':salesAcc, 'movieNmDt': '{} ({})'.format(movieNm, openDt.strftime('%Y'))})
        return pd.DataFrame(filmography).sort_values('openDt')

    # Subtract top N movies from given DataFrame
    def getTopMovies (self, df, period, top):
        df_period = df.where(df['targetDt'] > datetime.today() - timedelta(period)).dropna()
        return df_period.groupby('movieNm')['audiAcc'].max().nlargest(top).index

    # Update DataFrame with recent data & append new data to file
    def updateCurrentDailyBoxOffice(self, fileName, df_old):
        lastDt = df_old['targetDt'].max()
        daysGap = (datetime.today() - lastDt).days
        if daysGap <= 1:
            return df_old
        for targetDt in (datetime.strptime(lastDt, '%Y%m%d') + timedelta(days=n) for n in range(1, daysGap)):
            # API Call 
            result = requests.get(url = base_url + 'boxoffice/searchDailyBoxOfficeList.json', params = {'key': key, 'targetDt': targetDt.strftime('%Y%m%d')})
            df_new = pd.DataFrame(result.json()['boxOfficeResult']['dailyBoxOfficeList'])
            # Type Casting
            df_new[['audiCnt', 'audiAcc', 'salesAmt', 'salesAcc']] = df_new[['audiCnt', 'audiAcc', 'salesAmt', 'salesAcc']].apply(pd.to_numeric)
            df_new['targetDt'] = targetDt.strftime('%Y%m%d')
            # Minimalize DataFrame
            df_new = df_new [['targetDt', 'movieCd', 'audiCnt', 'audiAcc', 'salesAmt', 'salesAcc', 'movieNm']]
            # Save to csv file (append)
            df_new.to_csv(fileName, sep='\t', encoding = 'utf-8', mode='a', header=False, index=False)
        # Append new data to old data
        return df_old.append(df_new, ignore_index=True)