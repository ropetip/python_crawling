import requests
import openpyxl
from bs4 import BeautifulSoup

codes = [
    '005930',
    '000660',
    '035720'
]

fpath = r'D:\python_crawling\02_파이썬엑셀다루기\주식_data.xlsx'

# 1) 엑셀 불러오기
wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트 선택

cnt = 2;
for code in codes:
    url = f"https://finance.naver.com/item/sise.naver?code={code}"
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('#_nowVal').text
    ws[f'B{cnt}'] = price
    cnt = cnt + 1

# 4) 엑셀 저장하기
wb.save(fpath)
