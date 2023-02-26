import openai
import streamlit as st
from streamlit_chat import message


openai.api_key = st.secrets["api_secret"]

st.title('PwC Korea GPT')
st.header('문장요약 엔진')
st.write('Developed by Assurance DA (jae-dong.kim@pwc.com)')




article_text = st.text_area('요약할 뉴스나 텍스트를 입력해주세요')
temp = st.slider('요약스타일을 설정하세요 (설정 수치에따라 다양한 결과물을 만나볼 수 있습니다)',0.0,1.0,0.5)
if len(article_text) >1200:
    st.warning('좀 더 짧은 텍스트를 입력해주세요')

elif len(article_text) >100:
    if st.button('요약문 생성하기'):
        response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = f"이어지는 뉴스를 8개의 문장으로 요약해주세요: " +article_text,
        max_tokens = 1024, 
        temperature = temp
    )
        res = response['choices'][0]['text']
        st.info(res)

        st.download_button('Download Result',res)
else:
    st.warning('좀 더 긴 문장을 입력해주세요')



    


    

