import requests
import pandas as pd

class Input:

    # Input from User 
    def getType(self):
        return input('B: 박스오피스 랭킹\nF: 영화인 필모그래피 관객수 그래프\nQ: 종료\n: ')
    def getPeriod(self):
        return int (input('기준 기간 입력 from today (단위: day)\n: '))
    def getTop(self):
        return int (input('상위 N개 영화 랭킹 조회\n: '))
    def getPeopleNm(self):
        return input('영화인 입력\n:')
    def getPerson(self, peopleList):
        if (len(peopleList) != 1):
            for index, person in enumerate (peopleList):
                print('[{}] {} {} [{}]'.format(index, person['peopleNm'], person['repRoleNm'], person['filmoNames']))
            people = peopleList[int(input('영화인 선택\n:'))]
        else:
            people = peopleList[0]     
        return people

    # Read written DataFrame from CSV file and return as DataFrame
    def readDailyBoxOffice(self, fileName):
        df = pd.read_csv(fileName, sep='\t', encoding = 'utf-8')
        df['targetDt'] = pd.to_datetime(df['targetDt'], format='%Y%m%d')
        return df.sort_values('targetDt')
