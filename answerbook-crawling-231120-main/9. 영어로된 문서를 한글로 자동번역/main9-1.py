import googletrans 
#pip install googletrans==4.0.0-rc1

class Translator :
    def __init__(self):
        self.text = ''
        self.translator = googletrans.Translator()
    def set_text(self, text):
        self.text = text

    def en_to_kr(self):
        result2 = self.translator.translate(self.text, dest='ko', src='en')
        return result2
        print(f"{self.text}=> {result2.text}")

    def ko_to_en(self):
        result1 = self.translator.translate(self.text, dest='en', src='auto')
        return result1
        print(f"{self.text} => {result1.text}")

    def en_doc_to_ko(self):
        read_file_path = r"./영어파일.txt"
        write_file_path = r"./한글파일2.txt"

        with open(read_file_path, 'r') as f:
            readLines = f.readlines()

        for lines in readLines:
            result1 = self.translator.translate(lines, dest='ko')
            print(result1.text)
            with open(write_file_path, 'a', encoding='UTF8') as f:
                f.write(result1.text + '\n')


if __name__ == '__main__':
    t=Translator()
    while 1:
        menu = input('0. 종료 1. 문장입력 2. 영어로 번역 3. 한글로 번역 4. 영어문서>한글')
        if menu == '0':
            print('프로그램을 종료하겠습니다.')
            break
        elif menu == '1':
            text = input('번역할 문장 입력')
            t.set_text(text)
        elif menu == '2':
            a=t.ko_to_en()
            print(f'영어로 번역시 {a}')
        elif menu == '3':
            a= t.en_to_kr()
            print(f'영어로 번역시 {a}')
        elif menu == '4':
            t.en_doc_to_ko()
        else :
            print('제대로 입력해!')
            continue




