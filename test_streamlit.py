import streamlit as st

st.title('Hello, Streamlit world')

name = 'hyoeun'
st.write(f'Hello, {name}. welcome')

import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
})

import time

text = st.title('텍스트 변화')
time.sleep(2)
text.info('2초가 지났음')
