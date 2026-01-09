import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# 페이지 설정
st.set_page_config(
    page_title="판매 데이터 대시보드",
    page_icon="📊",
    layout="wide"
)

# 데이터 로드
@st.cache_data
def load_data():
    df = pd.read_csv('sales_data.csv')
    df['날짜'] = pd.to_datetime(df['날짜'])
    return df

# 데이터 로드
try:
    df = load_data()
except FileNotFoundError:
    st.error("sales_data.csv 파일을 찾을 수 없습니다. generate_data.py를 먼저 실행해주세요.")
    st.stop()

# 제목
st.title("📊 판매 데이터 분석 대시보드")
st.markdown("---")

# 사이드바 필터
st.sidebar.header("필터")
selected_categories = st.sidebar.multiselect(
    "카테고리 선택",
    options=df['카테고리'].unique(),
    default=df['카테고리'].unique()
)

date_range = st.sidebar.date_input(
    "날짜 범위",
    value=(df['날짜'].min(), df['날짜'].max()),
    min_value=df['날짜'].min(),
    max_value=df['날짜'].max()
)

# 데이터 필터링
filtered_df = df[
    (df['카테고리'].isin(selected_categories)) &
    (df['날짜'] >= pd.Timestamp(date_range[0])) &
    (df['날짜'] <= pd.Timestamp(date_range[1]))
]

# KPI 지표
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sales = filtered_df['판매액'].sum()
    st.metric("총 판매액", f"₩{total_sales:,.0f}")

with col2:
    total_quantity = filtered_df['판매수량'].sum()
    st.metric("총 판매수량", f"{total_quantity:,}개")

with col3:
    avg_sales = filtered_df['판매액'].mean()
    st.metric("평균 판매액", f"₩{avg_sales:,.0f}")

with col4:
    num_transactions = len(filtered_df)
    st.metric("거래 건수", f"{num_transactions:,}건")

st.markdown("---")

# 차트
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 카테고리별 판매액")
    category_sales = filtered_df.groupby('카테고리')['판매액'].sum().reset_index()
    fig1 = px.bar(
        category_sales,
        x='카테고리',
        y='판매액',
        color='카테고리',
        text='판매액'
    )
    fig1.update_traces(texttemplate='₩%{text:,.0f}', textposition='outside')
    fig1.update_layout(showlegend=False)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("🥧 카테고리별 판매 비중")
    fig2 = px.pie(
        category_sales,
        values='판매액',
        names='카테고리',
        hole=0.4
    )
    st.plotly_chart(fig2, use_container_width=True)

# 시계열 그래프
st.subheader("📅 일별 판매 추이")
daily_sales = filtered_df.groupby('날짜')['판매액'].sum().reset_index()
fig3 = px.line(
    daily_sales,
    x='날짜',
    y='판매액',
    markers=True
)
fig3.update_layout(hovermode='x unified')
st.plotly_chart(fig3, use_container_width=True)

# 데이터 테이블
st.subheader("📋 상세 데이터")
col1, col2 = st.columns(2)

with col1:
    st.subheader("카테고리별 통계")
    category_stats = filtered_df.groupby('카테고리').agg({
        '판매액': ['sum', 'mean', 'count'],
        '판매수량': 'sum'
    }).round(0)
    category_stats.columns = ['총 판매액', '평균 판매액', '거래 건수', '총 판매수량']
    st.dataframe(category_stats, use_container_width=True)

with col2:
    st.subheader("최근 거래 내역")
    recent_data = filtered_df.sort_values('날짜', ascending=False).head(10)
    st.dataframe(recent_data, use_container_width=True)

# 푸터
st.markdown("---")
st.markdown("*데이터는 가상으로 생성되었습니다.*")
