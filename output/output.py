from datetime import datetime, timedelta
import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
font_location = 'KoPubDotumBold.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
plt.rc('font', family=font_name)

class Output:

    # Show BoxOffice Graph by matplotlib, called by 4 functions below
    def showGraph(self, field, fieldName, movies, dataFrame, period, top):
        ax = plt.subplot(111)
        for movieNm in movies:
            dfByMovie = dataFrame.where(dataFrame['movieNm'] == movieNm).dropna()
            ax.plot(dfByMovie['targetDt'], dfByMovie[field], label = movieNm)
        
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 2, box.height * 2])
        ax.set_ylabel(fieldName)
        ax.set_title('최근 {}일 박스오피스 {} Top {} 변동추이'.format(period, fieldName, top))
        ax.legend(loc = 'center left', bbox_to_anchor=(1, 0.5))
        plt.show()

    # These 4 functions will call 'showGraph' in above.
    def showAudiCntGraph(self, movies, dataFrame, period, top):
        self.showGraph('audiCnt', '일 관객수', movies, dataFrame, period, top)
    def showAudiAccGraph(self, movies, dataFrame, period, top):
        self.showGraph('audiAcc', '누적 관객수', movies, dataFrame, period, top)
    def showSalesAmtGraph(self, movies, dataFrame, period, top):
        self.showGraph('salesAmt', '일 매출액', movies, dataFrame, period, top)
    def showSalesAccGraph(self, movies, dataFrame, period, top):
        self.showGraph('salesAcc', '누적 매출액', movies, dataFrame, period, top)

    # Show FilmoGraphy Graph by matplotlib
    def showFilmographyGraph(self, peopleNm, dataFrame):
        ax = dataFrame[['movieNmDt', 'audiAcc']].plot.bar()
        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 2, box.height * 2])
        ax.set_xticklabels(dataFrame['movieNmDt'])
        ax.set_ylabel('누적 관객수')
        ax.set_title('{} 작품 누적 관객수 (개봉년도 순)'.format(peopleNm))
        plt.show()    
