import pandas as pd
import urllib.request
import json
import datetime

# 어제 기준 농넷 데이터 불러오기
today = datetime.datetime.today()
yesterday = (today - datetime.timedelta(1)).strftime('%Y%m%d')
url = 'https://www.nongnet.or.kr/api/whlslDstrQr.do?sdate=' # sdata = 날짜

response = urllib.request.urlopen(url+yesterday).read()
response = json.loads(response)

data = pd.DataFrame(response['data'])

print(data)