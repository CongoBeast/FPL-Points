# pip install sklearn
# import sys

# if 'sklearn' not in sys.modules:
#     print('Installing sklearn...')
#     pip install scikit-learn

import streamlit as st
import pandas as pd
# from sklearn import neighbors
import matplotlib.pyplot as plt 
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import classification_report
from sklearn import metrics


modelscorev2 = joblib.load('FPL-Lin.pkl' , mmap_mode ='r+')

st.header("Welcome to FPL Expert Advisor")

st.write("In this web interface we aim to help use AI to make better FPL decisions")

st.write("Enter the following player information from last season to get the expected points at the end of the season")

def user_input():
        Position_string = st.radio("Select Player Position" , ["FW" , "MID" , "DEF" , "GK"])

        if Position_string == "GK":
            Position = 0
        elif Position_string == "DEF":
            Position = 1
        elif Position_string == "MID":
            Position = 2
        elif Position_string == "FW":
            Position = 3

        Minutes = st.number_input('Type Minutes Played' , key="mins")

        Goals = st.slider("Slide to select number of goals" , 0 , 40)

        Assists = st.slider("Slide to select number of assists" , 0 , 30)
										
        CleanSheets = st.number_input('Type number of ' , key="CS")

        GoalsConceded = st.number_input('Type number of ' , key="GoalsConceded")

        OwnGoals = st.number_input('Type number of ' , key="OwnGoals" )

        PenaltyScored = st.number_input('Type number of ' , key="PenaGoals")

        PenaltyMissed = st.number_input('Type number of ' , key="PenaMiss")

        YellowCards = st.number_input('Type number of Yellow Cards' , key="Yellows")

        RedCards = st.number_input('Type number of Red Cards' , key="RedCards")
        
        Saves = st.number_input('Type number of Saves ' , key="saves")
        
        BonusPoints = st.number_input('Type FPL Bonus Points System Index'  , key="BonusPts")

        BonusPointsSystem = st.number_input('Type FPL Bonus Points System Index' , key="BonusSys")
        
        Influence = st.number_input('Type FPL Threat Index' , key="Influence")
        
        Creativity = st.number_input('Type FPL Creativity Index' , key="Creativity")
        
        Threat = st.number_input('Type FPL Threat Index' , key="Threat")

        ICTIndex = st.number_input('Type FPL ICT Index' , key="ICT")
        
        StartingValue = st.number_input('Type current starting price' , key="StartVal")

        data = {'Position': int(Position),
            'Minutes PLayed': int(Minutes),
            'Goals Scored': int(Goals),
            'Assists': int(Assists),
            'Clean Sheets': int(CleanSheets),
            'Goals Conceded': int(GoalsConceded),
            'Own Goal': int(OwnGoals),
            'Penalty Scored': int(PenaltyScored),
            'Penalties Missed': int(PenaltyMissed),
            'Yellow Cards': int(YellowCards),
            'Red Cards': int(RedCards),
            'Saves': int(Saves),
            'Bonus Points': int(BonusPoints),
            'Bonus Points System': int(BonusPointsSystem),
            'Influence': int(Influence),
            'Creativity': int(Creativity),
            'Threat': int(Threat),
            'ICT Index': int(ICTIndex),
            'Starting Value': int(StartingValue)
            }
        features = pd.DataFrame(data, index=[0])
        return features


df = user_input()

df.fillna(1, inplace=True)

st.subheader('User Input parameters')
st.write(df)

st.subheader("Results")

prediction = modelscorev2.predict(df)

print(prediction)

st.write(prediction)
