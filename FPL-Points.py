# pip install sklearn
# import sys

# if 'sklearn' not in sys.modules:
#     print('Installing sklearn...')
#     pip install scikit-learn

import streamlit as st
import pandas as pd
from sklearn import neighbors
import matplotlib.pyplot as plt 
import joblib


modelscorev2 = joblib.load('FPL-KNN.pkl' , mmap_mode ='r+')

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

        data = {'Position': Position,
            'Minutes PLayed': Minutes,
            'Goals Scored': Goals,
            'Assists': Assists,
            'Clean Sheets': CleanSheets,
            'Goals Conceded': GoalsConceded,
            'Own Goal': OwnGoals,
            'Penalty Scored': PenaltyScored,
            'Penalties Missed': PenaltyMissed,
            'Yellow Cards': YellowCards,
            'Red Cards': RedCards,
            'Saves': Saves,
            'Bonus Points': BonusPoints,
            'Bonus Points System': BonusPointsSystem,
            'Influence': Influence,
            'Creativity': Creativity,
            'Threat': Threat,
            'ICT Index': ICTIndex,
            'Starting Value': StartingValue
            }
        features = pd.DataFrame(data, index=[0])
        return features


df = user_input()

st.subheader('User Input parameters')
st.write(df)

st.subheader("Results")

prediction = modelscorev2.predict(df)

print(prediction)

st.write(prediction)
