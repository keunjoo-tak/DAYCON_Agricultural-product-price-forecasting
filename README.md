# DAYCON_Agricultural-product-price-forecasting


# 개요
## 1. 주제
농산물 가격 예측 모형 개발

## 2. 배경
  * 농산물 가격 예측 서비스:
  농산물의 원활한 수급과 적정한 가격 유지를 위해 한국농수산식품유통공사(aT)는 농산물유통 종합정보시스템(이하 농넷)을 구축하여 운영하고 있습니다.
  농넷에서는 농산물 수급 관련 정보를 수집하여 다양한 빅데이터 분석 정보를 제공하고 있으며, 
  AI를 활용한 농산물가격예측 시스템을 구축하여 활용하고 있습니다. (향후 대민서비스 예정)
  * 목적 : 
  본 대회에서는 기존 농넷의 농산물 가격 예측 모형을 개선할 수 있는 새로운 아이디어와 알고리즘을 얻고자 합니다.

## 3. 결과 활용
    수상자 알고리즘은 농넷 가격예측 서비스에 활용

## 4. 주최 / 주관
  * 주최 : 한국농수산식품유통공사
  * 주관 : 데이콘

## 5. 참고문헌 
  * Helin Yin, Dong Jin, Yeong Hyeon Gu, Chang Jin Park, Sang Keun Han, Seong Joon Yoo, "STL-ATTLSTM: Vegetable Price Forecasting Using STL and Attention Mechanism-Based LSTM", Agriculture 2020

# 규칙
## 1. 평가
  * 1차 평가에서 6팀을 선발하여 이들을 대상으로 2차 평가 진행
  * 1차 계량 평가(90%)와 2차 비계량 평가(10%) 점수를 합산하여 최종 순위 결정 

< 1차 평가 > 
* ⅰ) 평가 산식: NMAE (Normalized Mean Absolute Error)
* ⅱ) 예측 대상: 21개 품목 및 품종의 1주 후, 2주 후, 4주 후 가격

    * 대상품목(16) : 배추, 무, 양파, 건고추, 마늘, 대파, 얼갈이배추, 양배추, 깻잎, 시금치, 미나리, 당근, 파프리카, 새송이, 팽이버섯, 토마토
    * 대상품종(5) : 청상추, 백다다기, 애호박, 캠벨얼리, 샤인마스캇

* ⅲ) 가격 산출 기준 : 전국 도매시장 (총 거래금액)/(총 거래량) (원/kg)

* ⅳ) Public Score: Private Score 평가 전에 자신의 모델 성능을 확인해볼 수 있는 점수

예측 대상: 2020년 10월 6일(화) ~ 2020년 11월 12일(목) 기간 내 품목별 1주, 2주, 4주 후 가격 
리더보드 업데이트 : 제출 후 실시간 업데이트

* ⅴ) Private Score: 최종 점수에 반영되는 Score

  예측 대상: 2021년 10월 5일(화) ~ 2021년 11월 11일(목) 기간 내 품목별 1주, 2주, 4주 후 가격
  답안 제출 기간: 2021년 9월 28일(화) ~ 2021년 11월 4일(목)
  리더보드 업데이트: 2021년 10월 6일(수) ~ 2021년 11월 12일(금) 내 1일 1회 업데이트
  ※ Private 리더보드 업데이트 시기는 시장 상황에 따라 변동 가능. (일반적으로 가격 자료 수집까지 하루 소요)

  ※ 답안 제출 기간 동안 매일 자정까지 답안을 제출해야함. API 사용하여 자동화 가능.

* ⅵ) 2차 평가 대상 선발: 수상 제외 및 실격 사유에 해당하지 않는 팀 중에서 Private Score가 높은 상위 6팀

< 2차 평가 >
* ⅰ) 일시: 2021년 12월 1일(수)

* ⅱ) 평가 방식: 온라인 발표 평가

* ⅲ) 평가 대상: 1차 평가에서 선발된 6팀

* ⅳ) 평가 기준: 과제 이해도, 기술 우수성, 적용 가능성, 부정제출 여부

## 2. 코드 제출
※ 홈페이지 참조

## 3. 참여 규칙
※ 홈페이지 참조

## 4. 외부 데이터 및 사전학습 모델
* ⅰ) 예측일 전날 자정까지 확인이 가능한 데이터만 학습 및 추론 과정에서 사용 가능(Data Leakage 관련 토크 게시글 참고)

* ⅱ) 공공데이터와 같이 누구나 얻을 수 있고 법적 제약이 없는 외부 데이터 허용(코드 제출시 출처 명시)

* ⅲ) 사전학습 모델 사용 가능(코드 제출시 사전학습에 사용된 데이터 명시)

* ⅳ) 추천 외부 데이터

  농산물 유통 정보: https://www.kamis.or.kr/customer/reference/openapi_list.do

  aT도매유통 정보시스템: https://at.agromarket.kr/openApi/apiInfoDtl.do?apiSeq=1

  농촌진흥청 국립농업과학원 농업기상 데이터: https://www.data.go.kr/data/15078057/openapi.do

  관세청_품목별 수출입 실적: https://www.data.go.kr/data/3046122/openapi.do

  농식품수출정보: https://www.kati.net/statistics/monthlyPerformanceByProduct.do

## 5. 유의 사항
※ 홈페이지 참조

# 일정
## 세부 일정


- 데이터 공개 : 2021년 8월 30일 10:00
- 대회 기간 : 2021년 8월 30일 10:00 ~ 2021년 11월 12일
- 팀 병합 마감 : 2021년 9월 21일
- Private 제출 : 2021년 09월 28일 ~ 2021년 11월 4일
- Private 평가 : 2021년 10월 6일 ~ 2021년 11월 12일
- 코드 제출 기간 : 2021년 11월 15일 ~ 2021년 11월 19일
- 코드 평가 기간 : 2021년 11월 22일 ~ 2021년 11월 26일
- 2차 평가 : 2021년 12월 1일
- 최종 순위 발표 : 2021년 12월 3일
- 시상식 : 2021년 12월 10일

# 데이터
## 1. public_data : public leaderboard용 데이터

	1-1. train.csv : 베이스라인 코드용으로 가공된 학습 데이터
      *  date: 일자
      *  요일: 요일
      *  품목_거래량(kg): 해당 품목의 거래량
      *  품목_가격(원/kg): 해당 품목의 kg당 가격
      *  품목_가격 산출 방식 : 품목 또는 품종의 총 거래금액/총 거래량 (※취소된 거래내역 제외)

	1-2. test_files : 베이스라인 코드용으로 가공된 테스트 데이터(추론일자별 분리, ex.test_2020-08-29.csv => 2020년 8월 29일 추론에 사용 가능 데이터)

	1-3. train_AT_TSALET_ALL : 학습용 전국 도매시장 거래정보 데이터(train.csv 생성에 사용)

      *  SALEDATE: 경락 일자
      *  WHSAL_NM: 도매시장
      *  CMP_NM: 법인
      *  PUM_NM: 품목
      *  KIND_NM: 품종
      *  DAN_NM: 단위
      *  POJ_NM: 포장
      *  SIZE_NM: 크기
      *  LV_NM: 등급
      *  SAN_NM: 산지
      *  DANQ: 단위중량
      *  QTY: 물량
      *  COST: 단가
      *  TOT_QTY: 총물량 (음수로 집계된 값은 거래 취소 내역)
      *  TOT_AMT: 총금액

	1-4. test_AT_TSALET_ALL : 추론용 전국 도매시장 거래정보 데이터(test_files 생성에 사용)



## 2. private_data : private leaderboard용 데이터, public leaderboard 학습 및 추론 사용 불가

	2-1. private.csv : 베이스라인 코드용으로 가공된 데이터

	2-2. AT_TSALET_ALL : 2021년 8월까지의 전국 도매시장 거래정보 데이터(private.csv 생성에 사용)



## 3. sample_submission.csv : 제출 양식

* 예측대상일자: 예측대상일(기준일로부터 1,2,4주 뒤 일자)
* 품목_가격(원/kg): 해당 품목의 kg당 가격