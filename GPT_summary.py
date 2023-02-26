import openai
import streamlit as st
from streamlit_chat import message


openai.api_key = st.secrets["api_secret"]

st.title('PwC Korea GPT')
st.header('문장요약 Robot')
st.write('Developed by Assurance DA (jae-dong.kim@pwc.com)')




article_text = st.text_area('요약할 뉴스나 텍스트를 입력해주세요 (참고: 영문은 국문으로 번역되어 제공합니다)', height=300)
lang = st.radio("언어를 선택해주세요",  ('국문', '영문'))
temp = st.slider('요약스타일을 설정하세요 (설정 수치에따라 다양한 결과물을 만나볼 수 있습니다)',0.0,1.0,0.5)

if lang =='국문':
    text = "이어지는 뉴스를 4개의 요약된 문장으로 변환해주세요: " +article_text
else:
    text = "Please convert the following sentences into 4 summarized Korean sentences " +article_text

if len(article_text) >2800:
    st.warning('좀 더 짧은 텍스트를 입력해주세요')

elif len(article_text) >100:
    if st.button('요약문 생성하기'):
        response = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = text,
        max_tokens = 4000, 
        temperature = temp
    )
        res = response['choices'][0]['text']
        st.info(res)

        st.download_button('Download Result',res)
else:
    st.warning('좀 더 긴 문장을 입력해주세요')



    


    

