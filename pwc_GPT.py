import openai
import streamlit as st
from streamlit_chat import message


openai.api_key = st.secrets["api_secret"]

# curie:ft-personal-2023-03-01-14-34-54
# "text-davinci-003
# gpt-3.5-turbo
# curie:ft-personal-2023-03-02-00-46-42

def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "curie:ft-personal-2023-03-02-00-46-42",
        prompt = prompt,
        max_tokens = 50, 
        n = 1,
        stop = None, 
        temperature = 0
    )

    message = completions.choices[0].text
    return message

# def generate_response(prompt):
#     completions = openai.ChatCompletion.create(
#         engine = "gpt-3.5-turbo",
#         messages=[
#         {"role": "system", "content": "당신은 IFRS 회계전문가입니다."},
#         {"role": "user", "content": prompt}
#     ]
#     )

#     message = completions.choices[0]['message']['content']
#     return message



st.title('Samil PwC Accounting GPT')
st.header('계정과목 분류 챗봇')
st.write('Developed by Assurance DA (jae-dong.kim@pwc.com)')

# user_input = st.text_input('말해보세요', key = 'input')
# st.write(generate_response(user_input))


if 'generated' not in st.session_state:
    st.session_state['generated']=[]

if 'past' not in st.session_state:
    st.session_state['past']=[]

def get_text():
    input_text = st.text_input('안녕하세요! 무엇을 도와드릴까요?' , key ='input')
    return input_text

user_input = get_text()

if user_input:
    output = generate_response(user_input)
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1,-1,-1):
        message(st.session_state['generated'][i],key = str(i))
        message(st.session_state['past'][i], is_user=True, key = str(i)+'_user')

    





