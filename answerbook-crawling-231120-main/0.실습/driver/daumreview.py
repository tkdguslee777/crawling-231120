import requests
import requests as req
import json
import pandas as pd
from bs4 import BeautifulSoup as bs
class DaumMovie:
    def __init__(self):
        self.url=''
        self.count = None # 크롤링결과 : {'count': 287, 'sum': 1118, 'id': 149761585}
        self.review_count = 0
        self.review_list = []

    def set_url(self, url):
        self.url = url

    def set_count(self):
        res = req.get(self.url)
        movie_code = '149761585'
        count_url = f"https://comment.daum.net/apis/v1/comments/on/{movie_code}/flags"
        count_res = req.get(count_url)
        self.count = json.loads(count_res.text)
        return self.count #로직상 필요는 없지만 main에서 print하기 위해 리턴함

    def extract_count(self):
        self.review_count = self.count['count']
        return self.review_count

    def set_review_list(self):
        for i in range(0,1): #self.review_count가 맞는데, 시간 관계상 2로 설정
            res = requests.get(self.url)
            ls = json.loads(res.text)
            print(f'i값 : {ls}')
            for i, _ in enumerate(ls):
                review = ls[i]['content']
                user = ls[i]['user']['displayName']
                rating = ls[i]['rating']
                self.review_list.append([user, rating, review])
            df = pd.DataFrame(self.review_list, columns=['user', 'rating', 'review'])
            df.to_excel('./daum_review.xlsx')




if __name__ == '__main__' :
    d = DaumMovie()
    while 1:
        menu = input('0-종료, 1-url등록, 2-리뷰갯수, 3-리뷰목록')
        if menu == '0' :
            print('프로그램 종료')
            break
        elif menu == '1' :
            #url = input ('수집하려는 url 입력')
            url2 = 'https://comment.daum.net/apis/v1/posts/149761585/comments?parentId=0&offset=0&limit=10&sort=LATEST&isInitial=true&hasNext=true'
            d.set_url(url2)

        elif menu == '2' :
            d.set_count()
            c = d.extract_count()
            print(f'리뷰의 총갯수 : {c}')

        elif menu == '3':
            d.set_review_list()

        else :
            print('잘못된 번호')
            continue





