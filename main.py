# Streamlit Documentation: https://docs.streamlit.io/

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from streamlit_card import card # https://github.com/gamcoh/st-card
import base64



# Title/Text
st.title("Employees Churn Prediction")
st.text("Stay or Left? Anticipating Employee Churn using Predictive Analytics")


with open('Image 07-12-2023 at 10.28 AM.jpg', "rb") as f:
    data = f.read()
    encoded = base64.b64encode(data)
data = "data:image/png;base64," + encoded.decode("utf-8")


hasClicked = card(
  title="Churn Prediction",
  text="",
  image= data,
  url="",
  on_click=lambda: print("clicked!")
)



df = pd.read_csv("HR_Dataset.csv")



st.sidebar.write("# Please, fill form")


department = st.sidebar.selectbox('Select departments', options = df['Departments '].unique().tolist())


average_montly_hours = st.sidebar.slider('Select the average montly hours', 85, 320, step=1)


satisfaction = st.sidebar.slider("Select the level of satisfaction", 0.0, 1.0)


last_evaluation = st.sidebar.slider("Select the last evaluation",0.0, 1.0)

    
number_project = st.sidebar.selectbox('Number of projects', options = df.number_project.unique().tolist())


time_spend_company = st.sidebar.selectbox('Time spend in company', options = df.number_project.unique().tolist())


salary = st.sidebar.radio('Salary', options=df.salary.unique().tolist(), key=7)

Work_accident = st.sidebar.radio('Has the employee been in a work accident?', options=['Yes', 'No'], key=5)
Work_accident2 = 0 
if Work_accident == 'Yes':
    Work_accident2 = 1

promotion_last_5years = st.sidebar.radio('Has the employee been promoted in the last 5 years?', options=['Yes', 'No'], key=6)
promotion_last_5years2 = 0
if promotion_last_5years == 'Yes':
    promotion_last_5years2 = 1


# user table 
my_dict2 = {'satisfaction_level' : satisfaction,
 'last_evaluation': last_evaluation,
 'number_project': number_project,
 'average_montly_hours':average_montly_hours ,
 'time_spend_company': time_spend_company,
 'Work_accident': Work_accident,
 'promotion_last_5years': promotion_last_5years,
'departments': department,
 'salary':salary
           }
df2 = pd.DataFrame.from_dict([my_dict2])
st.table(df2.T)


import pickle
filename = "XGBoost_model.sav"
model=pickle.load(open(filename, "rb"))


st.subheader('Your choices:')
my_dict = {'satisfaction_level' : satisfaction,
 'last_evaluation': last_evaluation,
 'number_project': number_project,
 'average_montly_hours':average_montly_hours ,
 'time_spend_company': time_spend_company,
 'Work_accident': Work_accident2,
 'promotion_last_5years': promotion_last_5years2,
'departments': department,
 'salary':salary
           }
df = pd.DataFrame.from_dict([my_dict])


# Prediction with user inputs
predict = st.button("Predict")
result = model.predict(df)
str1 = "The employee will leave the company"
if result == 0:
    str1 = "The employee will stay"
if predict :
    st.text('Prediction is: ')
    st.info(str1)
