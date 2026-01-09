# 📊 판매 데이터 분석 대시보드

Streamlit을 사용한 인터랙티브 판매 데이터 분석 대시보드입니다.

## 기능

- 실시간 KPI 지표 (총 판매액, 판매수량, 평균 판매액, 거래 건수)
- 카테고리별 판매액 시각화
- 카테고리별 판매 비중 파이 차트
- 일별 판매 추이 그래프
- 카테고리 및 날짜 범위 필터링
- 상세 데이터 테이블

## 로컬 실행 방법

### 1. 저장소 클론

```bash
git clone <your-repo-url>
cd cursor_tutotial
```

### 2. 가상환경 생성 및 활성화

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 또는 Windows: venv\Scripts\activate
```

### 3. 필요한 라이브러리 설치

```bash
pip install -r requirements.txt
```

### 4. 가상 데이터 생성

```bash
python generate_data.py
```

### 5. 대시보드 실행

```bash
streamlit run dashboard.py
```

브라우저에서 자동으로 `http://localhost:8501`로 열립니다.

## 기술 스택

- Python 3.x
- Streamlit
- Pandas
- Plotly
- NumPy

## 라이선스

MIT
