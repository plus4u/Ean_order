import streamlit as st
import pandas as pd

st.set_page_config(page_title="이안글로벌 윤활유 간편주문", layout="centered")

st.title("🛢️ 이안글로벌 모바일 주문")
st.caption("단가를 확인하시고 주문 수량을 입력해 주세요.")

# 1. 고객 정보 입력
st.subheader("1. 주문자 정보")
company = st.text_input("고객사 / 상호명 *")
name = st.text_input("담당자명 *")
phone = st.text_input("연락처 *")
address = st.text_input("배송지 주소 *")

# 2. 제품 및 수량 선택
st.subheader("2. 제품 선택 및 수량")
product = st.selectbox(
    "제품을 선택하세요",
    ["Kixx GX5 SQ 5W-30 (79,000원/박스)", 
     "Kixx DX9 CK-4/E11 10W-40 (92,000원/페일)",
     "Kixx RD HD 46 (65,000원/페일)",
     "Kixx Grease 2 (58,000원/캔)"]
)

# 단가 추출 및 수량 계산
price_map = {
    "Kixx GX5 SQ 5W-30 (79,000원/박스)": 79000,
    "Kixx DX9 CK-4/E11 10W-40 (92,000원/페일)": 92000,
    "Kixx RD HD 46 (65,000원/페일)": 65000,
    "Kixx Grease 2 (58,000원/캔)": 58000
}

qty = st.number_input("주문 수량", min_value=1, value=1, step=1)
unit_price = price_map[product]
total_price = unit_price * qty

# 총 금액 계산 표시
st.info(f"💰 **총 주문금액: {total_price:,} 원**")

requests = st.text_area("희망 납기일 및 요청사항")

# 3. 주문 제출 버튼
if st.button("주문 제출하기", type="primary"):
    if not company or not phone:
        st.error("상호명과 연락처는 필수 입력 항목입니다.")
    else:
        # 구글 시트에 주문 데이터 추가 저장 로직 (백엔드 처리)
        st.success("주문이 성공적으로 접수되었습니다! 담당자 확인 후 연락드리겠습니다.")