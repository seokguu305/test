import requests
from urllib.parse import urlencode, quote_plus
import datetime

# 오늘 날짜 및 시간
now = datetime.datetime.now()
base_date = now.strftime("%Y%m%d")
base_time = now.strftime("%H00")

# 기상청 해양 API 정보
endpoint = "http://apis.data.go.kr/1360000/MarineWeatherInfoService/getSeaFcst"
service_key = "발급받은_디코딩된_서비스키"

# 예보 지역 코드 (예: 동해 바다: 11B00000) — 지역코드는 실제 지역에 따라 다름
# 아래 예시는 강원 동해 앞바다
params = {
    'serviceKey': service_key,
    'pageNo': '1',
    'numOfRows': '100',
    'dataType': 'JSON',
    'regId': '11B00000',  # 지역 ID: 동해 앞바다 예시
    'tmFc': base_date + "0600"  # 발표 시각: 0600, 1800 기준
}

response = requests.get(endpoint, params=params)
data = response.json()

# 결과 출력
items = data['response']['body']['items']['item']
for item in items:
    print(f"예보일: {item['wfSv']}")
