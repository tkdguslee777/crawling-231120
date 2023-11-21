from currency_converter import CurrencyConverter
# pip install CurrencyConverter

class Exchange:
    def __init__(self):
        pass

    def get_all_currencies(self):
        cc = CurrencyConverter()
        return cc.currencies

    def change_usd_to_krw(self):
        cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
        return cc.convert(1, 'USD', 'KRW')

if __name__ == '__main__':
    e = Exchange()
    while 1:
        menu = input('0. 종료 1. 전체화폐단위 2. 원달러')
        if menu == '0' :
            print('프로그램을 종료하겠습니다.')
            break
        elif menu == '1':
            c= e.get_all_currencies()
            print(f'{c}')
        elif menu == '2':
            x = e.change_usd_to_krw()
            print(f'변환된 결과 : {x}')
        else :
            print('다시 선택해주세요')
            continue


print()

