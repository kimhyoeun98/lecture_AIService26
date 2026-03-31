import streamlit as st

with st.form('my_form'):
    
    # 텍스트, 숫자, 체크박스 입력 위젯
    name = st.text_input("이름")
    age = st.number_input("나이", min_value=1, value=1, step=1)
    agree = st.checkbox("약관에 동의합니다")
    
    # 제출 버튼
    submit_btn = st.form_submit_button("제출")

# 제출 버튼이 클릭되었을 때의 동작 처리
if submit_btn:
    # 입력받은 이름과 나이 출력
    st.write(f"이름: {name}, 나이: {age}")
    
    # 약관 동의 여부에 따라 초록색 성공 알림창 표시
    if agree:
        st.success("약관에 동의했습니다.")
    else:
        st.error("약관에 동의하지 않았습니다.")