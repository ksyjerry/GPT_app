import openai
import streamlit as st
from streamlit_chat import message


openai.api_key = st.secrets["api_secret"]





# curie:ft-personal-2023-03-01-14-34-54
# "text-davinci-003
# gpt-3.5-turbo
# curie:ft-personal-2023-03-02-00-46-42

# def generate_response(prompt):
#     completions = openai.Completion.create(
#         engine = "curie:ft-personal-2023-03-02-00-46-42",
#         prompt = prompt,
#         max_tokens = 50, 
#         n = 1,
#         stop = None, 
#         temperature = 0
#     )

#     message = completions.choices[0].text
#     return message

def generate_response(prompt):
    completions = openai.ChatCompletion.create(
        engine = "gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "당신은 IFRS 회계전문가입니다."},
        {"role": "user", "content": prompt}
    ]
    )

    message = completions.choices[0]['message']['content']
    return message


# prompt1 = """ 
# President Yoon Suk Yeol will hold a summit with Japanese Prime Minister Fumio Kishida next week, as he is set to visit the neighboring country with first lady Kim Keon Hee, the presidential office said Thursday.

# This is the first visit by a Korean president to Japan in about four years since former President Moon Jae-in visited Osaka in June 2019 to attend the Group of 20 summit. It is also the first time in 11 years and 3 months that a Korean president participates in a bilateral summit in Japan since the meeting between former President Lee Myung-bak and former Prime Minister Yoshihiko Noda in December 2011.

# The two-day visit is scheduled from March 16-17 at the invitation of the Japanese government. Seoul and Tokyo are currently coordinating the details of the presidential trip, South Korean officials said in a written statement.

# The two first ladies will have separate fellowship events, they added.

# Expectations are high for the two leaders to discuss bolstering bilateral ties in various fields including security, economy, society and culture, the presidential office said, noting that it is aimed at putting historic disputes behind them and bringing the focus to future ties.

# The summit announcement comes after Seoul and Tokyo agreed on a deal in which South Korea would compensate Korean laborers forced to work in Japanese factories during World War II, despite mounting opposition from the victims and opposition parties. The proposal was aimed at resolving a colonial-era grievance that has long strained the relationship between the key US allies in Asia.

# Japan’s Chief Cabinet Secretary Hirokazu Matsuno told the press that the South Korean leader will be making a working trip to the country.

# Korea is an important neighbor to cooperate with in responding to various challenges faced by the international community, he said, expressing hopes for bilateral ties to advance further.

# During Yoon's trip to Tokyo, the two countries are expected to discuss regional security related to North Korea's nuclear threats and resuming military information sharing.
# """

# prompt2 = """

# ▶기업들에게 회계법인은 신뢰 가는 비즈니스 솔루션을 제공하는 역할을 한다. PwC가 전 세계 CEO들을 대상으로 한 설문 중에서, 지속가능성이 높은 기업일 수록 소비자의 ‘신뢰’가 높다는 결과가 나온 것이 있다. 회계법인의 역할은 결국 경제의 다양한 이해관계자들이 상호 신뢰를 바탕으로 더욱 원활하게 소통하면서 발전해나갈 수 있도록 회계 및 재무부문에 있어서 ‘신뢰’의 영역을 더 확대하고 공고히 하는 것이다.

# -신외감법이 시행된 지 만 3년이 지났다. 감사인의 독립성과 회계투명성이 높아졌다고 보는가?

# ▶신외감법의 도입이 외부감사법인의 독립성을 높여 궁극적으로 한국기업의 회계투명성을 높이는데 기여했다는 점은 이론의 여지가 없어 보인다. 다만 그 과정에서 기업들의 부담이 늘어난 것 또한 부인하기 어려운 것 같다. 따라서 기업이나 회계법인의 시각으로만 볼 것이 아니라, 재무정보를 이용하는 투자자들의 관점에서 효용이 있느냐에 초점을 맞춰야 한다고 생각한다.

# -현장에서 느껴지는 긍정적인 변화가 있는가?

# ▶최근 현장에서 직접 기업과 접촉하며 일하는 주니어 회계사들이 직업에 대한 자긍심이 생겨서 좋다고 얘기한다. 회계사는 ‘자본주의의 파수꾼’이라고 하는데 신외감법 이후 파수꾼 역할을 제대로 할 수 있게 됐다는 것이다. 신외감법이 10년 정도 꾸준히 지속되면 기업과 회계법인 모두 새로운 체계에 적응해서 회계 투명성도 우리나라의 경제 위상에 맞게 개선되리라 확신한다.

# -기업계에서는 비용부담 등의 이유로 반발이 여전히 크다. 대한상의는 주기적 지정감사제 폐지를 건의하기도 했다.

# ▶주기적 지정감사제는 비교적 객관적 위치일 수 있는 해외 투자은행(IB) 측도 긍정적으로 평가하고 있다. 지난해 말 금융감독원이 주최한 업계 간담회에서 해외 IB들은 주기적 지정감사제가 해외에 없는 제도지만 한국 기업의 취약한 지배구조 문제를 보완하고 회계 투명성을 높이는 데 긍정적인 측면이 있다고 평가했다. 외국인 투자자들에게 코리아 디스카운트를 해소하는 데 기여했다고 볼 수 있다. 단기간에 상장사의 회계 투명성을 크게 높이는 데 기여한 제도를 불과 4년 만에 바꾸는 것은 득보다 실이 클 수 있다.

# """

# prompt3 = """
# -지난해 빅4회계법인들이 사상 최대 매출을 기록했다. 삼일PwC도 컨설팅 매출을 합하면 2022회계연도에는 총매출 1조2323억원을 달성했다. 비결은 무엇인가?

# ▶컨설팅 부문의 성장률이 가장 높았고, 딜 부문, 세무 부문, 회계·감사 순으로 성장세가 컸다. 컨설팅·딜 부문의 성장은 한국 기업들의 디지털 트랜스포메이션과 에너지 트랜지션 이행 노력 등에 힙입은 바가 크다. 그러나 기업의 업무가 오직 한 부분에 국한돼지는 않을 터. 통합 서비스를 통해 시너지를 발휘하면 더 많은 가치를 기업에게 제공할 수 있다. 그래서 CEO로 취임한 이후 특히 강조한 것이 ‘부문간의 협업(collaboration)’이다.

# 예를 들어 M&A(인수합병)와 관련해 딜 부문에 재무 자문을 요청하면, 감사, 세무부분 그리고 PwC 관련사들까지 같이 참여해 제안서를 만들고 프리젠테이션에 참여한다. 기업 입장에선 본인들이 미처 생각하지 못한 부분까지 솔루션과 새 아이디어를 제공받게 된다. 이런 선순환을 통해 삼일PwC는 더 많은 업무를 수임하고 있다. 이를 전문적으로 하기 위해 딜 플랫폼, ESG 플랫폼, 유니콘 플랫폼 등 상시 협업 ‘플랫폼’을 만들었다.

# -회계업계의 성장과 더불어 공인회계사의 인기도 치솟고 있다. 특히 기업에서 회계인력 수요가 급증했다. 회계법인으로서 인력 확보의 해법은?

# ▶기업활동을 하는 데엔 법률, 회계, 세무, 노무 등 다양한 전문지식이 필요하다. 최근 들어 회계 전문가들에 대한 수요가 높아지고 있다. 경쟁이 높아지다보니 전문가들을 채용하고 또 유지하는 데 어려움이 없지 않다. 내부인원으로 회계인력을 충족하는 것보다는 회계법인의 전문 서비스를 활용하는 게 더 좋지 않을까 한다. 핵심분야 집중에 더욱 유효하다. 실제로 많은 기업들이 결산, 재무보고, 내부회계제도 관리 목적으로 회계법인의 전문 회계 서비스를 활용 중이고, 이같은 움직임은 점점 확대되는 추세다.

# 회계·재무분야 업무자동화를 통해 기업에선 관련 분야의 인력 수요를 줄일 수 있다. RPA(Robotic Process Automation)같은 디지털 기술을 사용해서다. 그러나 모든 기업들이 제각각 자동화에 투자하는 것은 기업뿐만 아니라 사회 전체적으로도 비효율적인 중복투자다. 업계 1등 법인으로서 남다른 관심을 가지고 최근 자동화 분야에 대한 솔루션을 만들었다. 현재 몇몇 기업에 시험테스트 중이다. 테스트가 완료되면 서비스를 본격 시작할 것이다.

# -삼일회계법인의 CEO로 첫 3년 임기를 보내셨는데 전문가들 4000여 명이 모인 거대조직을 이끌면서 사상 최대 실적을 연거푸 경신하는 게 쉬운일은 아니셨을 것 같다. 조직운영에 있어서 가장 중요시하는 철학이 있다면?
# """

st.title('Samil PwC Accounting GPT')
st.header('IFRS 챗봇')
st.write('Developed by Assurance DA (jae-dong.kim@pwc.com)')

question = st.text_input('질문을 입력하세요(English Questions Preferred) ')
completions = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": question},
#       {"role": "system", "content": prompt2},
#       {"role": "system", "content": prompt3},
      {"role": "user", "content": question}
  
    ]
)

st.write(completions.choices[0]['message']['content'])


# if 'generated' not in st.session_state:
#     st.session_state['generated']=[]

# if 'past' not in st.session_state:
#     st.session_state['past']=[]

# def get_text():
#     input_text = st.text_input('안녕하세요! 무엇을 도와드릴까요?' , key ='input')
#     return input_text

# user_input = get_text()



# if user_input:
#     output = generate_response(user_input)
#     st.session_state.past.append(user_input)
#     st.session_state.generated.append(output)

# if st.session_state['generated']:
#     for i in range(len(st.session_state['generated'])-1,-1,-1):
#         message(st.session_state['generated'][i],key = str(i))
#         message(st.session_state['past'][i], is_user=True, key = str(i)+'_user')

    





