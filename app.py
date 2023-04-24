
import streamlit as st
import pickle
import pandas as pd
import json



import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie

st.title('IPL Win predictor')






# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_hello = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_6eeyigak.json")


st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="high",  # medium ; high
    height=200,
    width=None,
    key=None,
)


teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Rajiv Gandhi International Stadium, Uppal',
       'M Chinnaswamy Stadium', 'Wankhede Stadium',
       'Holkar Cricket Stadium', 'Eden Gardens', 'Feroz Shah Kotla',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'Punjab Cricket Association Stadium, Mohali',
       'Sawai Mansingh Stadium', 'MA Chidambaram Stadium, Chepauk',
       'Dr DY Patil Sports Academy', 'Newlands', "St George's Park",
       'Kingsmead', 'SuperSport Park', 'Buffalo Park',
       'New Wanderers Stadium', 'De Beers Diamond Oval',
       'OUTsurance Oval', 'Brabourne Stadium',
       'Sardar Patel Stadium, Motera', 'Barabati Stadium',
       'Vidarbha Cricket Association Stadium, Jamtha',
       'Himachal Pradesh Cricket Association Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Subrata Roy Sahara Stadium',
       'Shaheed Veer Narayan Singh International Stadium',
       'JSCA International Stadium Complex', 'Sheikh Zayed Stadium',
       'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium',
       'Maharashtra Cricket Association Stadium',
       'M. A. Chidambaram Stadium', 'Feroz Shah Kotla Ground',
       'M. Chinnaswamy Stadium', 'Rajiv Gandhi Intl. Cricket Stadium',
       'IS Bindra Stadium', 'ACA-VDCA Stadium']

pipe = pickle.load(open('pipe.pkl', 'rb'))


col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))
with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

selected_city = st.selectbox('Select Host City', sorted(cities))

target = st.number_input('Target')
col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score')
with col4:
    overs = st.number_input('Over Completed')
with col5:
    wickets = st.number_input('Wickets Out')

if overs == 0:
    overs=0.1
if st.button('Predict Probability'):
    if (overs >= 20 and score <target) or (wickets>=10 and score<target) :
        st.write(batting_team+" Loss The Match")
    else:
        runs_left = target-score
        balls_left = (126-(overs*6))
        wickets = 10-wickets
        crr = score/overs
        rrr = (runs_left*6)/balls_left
        # 'batting_team', 'bowling_team', 'city', 'runs_left', 'balls_left', 'wickets', 'total_runs_x', 'crr', 'rrr'
        input_df = pd.DataFrame({'batting_team': [batting_team], 'bowling_team': [bowling_team], 'venue': [selected_city],
                                 'runs_left': [runs_left], 'balls_left': [balls_left], 'wickets': [wickets],
                                 'total_runs_x': [target], 'crr': [crr], 'rrr': [rrr]})
        st.table(input_df)
        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]

        st.header(batting_team + '-' + str(round(win*100))+"%")
        st.header(bowling_team + '-' + str(round(loss*100))+"%")
