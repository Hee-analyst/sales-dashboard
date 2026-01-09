import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 가상 데이터 생성
np.random.seed(42)

# 날짜 범위 (최근 3개월)
start_date = datetime.now() - timedelta(days=90)
dates = [start_date + timedelta(days=i) for i in range(90)]

# 제품 카테고리
categories = ['전자제품', '의류', '식품', '가구', '도서']

# 데이터 생성
data = []
for date in dates:
    for category in categories:
        sales = np.random.randint(50, 500)
        quantity = np.random.randint(5, 50)
        data.append({
            '날짜': date.strftime('%Y-%m-%d'),
            '카테고리': category,
            '판매액': sales,
            '판매수량': quantity
        })

# DataFrame 생성 및 저장
df = pd.DataFrame(data)
df.to_csv('sales_data.csv', index=False, encoding='utf-8-sig')

print(f"가상 데이터 생성 완료: {len(df)}개 레코드")
print(df.head())
