import openai
import streamlit as st
from streamlit_chat import message


openai.api_key = st.secrets["api_secret"]

st.title('PwC Korea GPT')
st.header('문장요약 Robot')
st.write('Developed by Assurance DA (jae-dong.kim@pwc.com)')




article_text = st.text_area('요약할 뉴스나 텍스트를 입력해주세요', height=300, placeholder ='100문자 이상 1500문자 이내로 입력')
lang = st.radio("요약문으로 반환될 언어를 선택해주세요",  ('국문', '영문'))
temp = st.slider('요약스타일을 설정하세요 (설정 수치에따라 다른 스타일의 문장이 생성됩니다)',0.0,1.0,0.5)

if lang =='국문':
    text = "Please convert the following sentences into 4 summarized Korean sentences" +article_text
else:
    text = "Please convert the following sentences into 4 summarized English sentences " +article_text

if len(article_text) >1600:
    st.warning('좀 더 짧은 텍스트를 입력해주세요')

elif len(article_text) >100:
    if st.button('요약문 생성하기'):
        response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        max_tokens = 2400, 
        temperature = temp
    )
        res = response['choices'][0]['text']
        st.info(res)

        st.download_button('Download Result',res)
else:
    st.warning('좀 더 긴 문장을 입력해주세요')



    


    

