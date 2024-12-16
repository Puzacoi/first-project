import requests
from bs4 import BeautifulSoup
from datetime import *

# 네이버 환율 페이지 URL
url = "https://finance.naver.com/marketindex/exchangeList.nhn"

response = requests.get(url)

# 응답이 정상인지 확인
if response.status_code == 200:
    # HTML 파싱한다(사이의 데이터를 추출하기 위함)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 달러의 현재 환율 정보를 가져온다
    usd_rate = soup.find("td", {"class": "sale"}).get_text().strip()

    # ,를 제거하여 1,300을 1300으로 하고 실수형으로 변환시킨다
    usd_rate_float = float(usd_rate.replace(',', '').split()[0])

# 업비트 주소이다
url = "https://api.upbit.com/v1/ticker"

# 요청 파라미터
params = {
    'markets': 'KRW-BTC'  # 비트코인의 한국 원화(KRW) 가격
}

# API 요청
response = requests.get(url, params=params)

# 응답이 정상적인지 확인
if response.status_code == 200:
    # 응답 데이터 가져오기
    data = response.json()

    # 비트코인 가격 추출
    btc_price = data[0]['trade_price']


clock = datetime.now() #오늘의 날짜,시간 등에 대한 정보가 담겨있다
ymd ="%s년 %s월 %s일"%(clock.year, clock.month, clock.day)
def Conversion(v, c): #달러,코인의 값을 받아오고 수량을 받아와서 계산
    return float(v * c) # 환율

print("== 원화 보유량 계산기 ==")
print("== %s 기준 =="%ymd)
while True:
	d_value = float(input("달러 보유수량 :"))
	b_value = float(input("비트코인 보유수량:"))

	d_won = Conversion(d_value,usd_rate_float)
	b_won = Conversion(b_value,btc_price)

	print(f"달러{usd_rate_float} x 보유량%f = %.2f원 "%(d_value, d_won))
	print(f"비트{btc_price} x 보유량 %f = %.2f원 "%(b_value, b_won))	
	result = (d_won + b_won)

	print("원화 보유량: %.2f원 입니다."%(result))
	e_value = float(input("종료는 0입니다 :"))
	if e_value ==0:
		print("종료")
		break
	else:
		print("=============================")
