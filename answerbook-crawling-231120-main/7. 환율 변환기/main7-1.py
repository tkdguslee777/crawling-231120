from currency_converter import CurrencyConverter
# pip install CurrencyConverter
import requests
from bs4 import BeautifulSoup

class Exchange:
    def __init__(self):
        pass

    def get_all_currencies(self):
        cc = CurrencyConverter()
        return cc.currencies

    def change_usd_to_krw(self):
        cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
        return cc.convert(1, 'USD', 'KRW')

    def realtime_usd_to_krw(self, target1, target2):
        headers = {
            'User-Agent': 'Mozilla/5.0',
            'Content-Type': 'text/html; charset=utf-8'
        }
        # https://kr.investing.com/currencies/usd-krw

        response = requests.get(f"https://kr.investing.com/currencies/{target1}-{target2}", headers=headers)
        content = BeautifulSoup(response.content, 'html.parser')
        containers = content.find('span', {'data-test': 'instrument-price-last'})
        return containers.text

if __name__ == '__main__':
    e = Exchange()
    while 1:
        menu = input('0. 종료 1. 전체화폐단위 2. 원달러 3.실시간 환율변화')
        if menu == '0' :
            print('프로그램을 종료하겠습니다.')
            break
        elif menu == '1':
            c= e.get_all_currencies()
            print(f'{c}')
        elif menu == '2':
            c = e.change_usd_to_krw()
            print(f'변환된 결과 : {c}')
        elif menu == '3' :
            target1 = input('환전하려는 화폐단위 : ')
            target2 = input('환전된 화폐단위 : ')
            c = e.realtime_usd_to_krw(target1,target2)
            print(f'변환된 결과 : {c}')
        else :
            print('다시 선택해주세요')
            continue


print()

