import pandas as pd


class Naverstock:
    def __init__(self):
        self.code = None

    def krx_crawl(self):
        c = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header = 0)[0]
        c['종목코드']=c['종목코드'].map('{:06d}'.format) # 005930이 5930으로 출력되는 것을 막는다.
        k = c[['회사명','종목코드']]
        print(k)


    def get_url(self):
        pass

    def naver_crawl(self):
        pass



if __name__ == '__main__':
    n = Naverstock()

    while 1:
        menu = input('0-종료, 1-종목코드, 2-url, 3-시세와 종가 엑셀로 저장')
        if menu =='0':
            print('프로그램 종료')
            break
        elif menu =='1':
            n.krx_crawl()

        elif menu == '2':
            pass
        elif menu == '3':
            pass
        else:
            print('잘못된 값')
            continue