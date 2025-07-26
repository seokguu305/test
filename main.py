import requests
import datetime

# 오늘 날짜 및 시간 (발표 시각: 0600 or 1800)
now = datetime.datetime.now()
base_date = now.strftime("%Y%m%d")
tmFc = base_date + "0600"  # 오전 예보 기준, 오후면 "1800"

# 기상청 해양기상정보 API
service_key = "uVlewaNuxkPT1MejspqtD9zkInFxx+dAgTcFJvdGTVNfVHbrr3mK23k0MU6teAOf0uZ37+LEjuqWtei34I1vVg=="
endpoint = "http://apis.data.go.kr/1360000/MarineWeatherInfoService/getSeaFcst"

params = {
    'serviceKey': service_key,
    'pageNo': '1',
    'numOfRows': '100',
    'dataType': 'JSON',
    'regId': '11B00000',  # 동해 앞바다 예시
    'tmFc': tmFc
}

response = requests.get(endpoint, params=params)
data = response.json()

# 결과 출력
if 'response' in data:
    try:
        items = data['response']['body']['items']['item']
        print("=== 동해 앞바다 예보 ===")
        for item in items:
            print(item)
    except KeyError:
        print("데이터 파싱 중 오류가 발생했습니다.")
else:
    print("API 호출 실패:", data)
