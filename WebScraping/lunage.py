import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep

def lunage_function():
    '''
    월령 정보를 추가시켜 주는 함수
    input column에 date가 있는 dataframe
    output 컬럼에 date를 기준으로 lunAge라는 항목이 추가됨
    하루에 요청랑 1만개까지 가능
    '''
    ServiceKey = 'Kfe6usVsCnFJYrxL5ibwGW2T2CgwpKKDF2UpYLObF3MWEU%2BUjeKNN1T5jU%2Bd3tJvWO4m7cqYseEms%2Fk507iNGQ%3D%3D'
    url_format = 'http://apis.data.go.kr/B090041/openapi/service/LunPhInfoService/getLunPhInfo?solYear={solYear}&solMonth={solMonth}&solDay={solDay}&ServiceKey={ServiceKey}'

    lunage = [] # 요청한 값을 담을 리스트
    dt_index = pd.date_range(start='20090101', end='20190531')
    for count, i in enumerate(dt_index):
        #extract date
        solYear = str(i)[0:4]
        solMonth = str(i)[4:6]
        solDay = str(i)[6:8]
        
        for i in range(100):
            #url request
            url = url_format.format(solYear=solYear, solMonth=solMonth, solDay=solDay, ServiceKey=ServiceKey)
            print(url)
            req = requests.get(url, timeout=(10, 10))

            #except
            req.raise_for_status()

            #change xml to text
            html = req.text
            soup = BeautifulSoup(html, 'html.parser')
            
            if not (soup.find_all('returnreasoncode')):
                if (soup.find_all('lunage')):
                    break
            #if req.status_code is 200:
            #    break
            sleep(0.01)

        lunage_text = soup.find_all('lunage')[0].text
        lunage.append(lunage_text)
        if count % 500 == 0:
            print("count: ",count)
    print("success!!!!")
    return pd.DataFrame({'lunage':lunage}).astype(float)

c = lunage_function()
    dt_index = pd.date_range(start='20090101', end='20190531')
