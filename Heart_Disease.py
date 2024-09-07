
import streamlit as st
import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

Model  = joblib.load( "Model.pkl")
Inputs = joblib.load( "Inputs.pkl")
Label  = joblib.load( "Label.pkl")


def Prediction(Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope, Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak):
    df = pd.DataFrame(columns= ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope',
       'Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak'])

    df.at[0,'Sex']= Sex
    df.at[0,"ChestPainType"]= ChestPainType
    df.at[0,"RestingECG"]= RestingECG
    df.at[0,"ExerciseAngina"]= ExerciseAngina
    df.at[0,"ST_Slope"]= ST_Slope
    df.at[0,"Age"]= Age
    df.at[0,"RestingBP"]= RestingBP
    df.at[0,"Cholesterol"]= Cholesterol
    df.at[0,"FastingBS"]= FastingBS
    df.at[0,"MaxHR"]= MaxHR
    df.at[0,"Oldpeak"]= Oldpeak
    
    
    label=LabelEncoder()
    object_col = df.select_dtypes(include='object')
    non_object_col = df.select_dtypes(exclude='object')
    for col in object_col.columns:
        object_col[col]=label.fit_transform(object_col[col])
    df=pd.concat([object_col,non_object_col],axis=1)
    
    # transformed = Label.transform(df[['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']])
    # transformed_df = pd.DataFrame(transformed, columns=Label.get_feature_names_out())
    # df = pd.concat([df[['Age', 'RestingBP', 'Cholesterol', 'FastingBS', 'MaxHR', 'Oldpeak']] , transformed_df] , axis = 1)

    # transformed = Encoder.transform(df[['sex' ,'smoker', 'region']])
    # transformed_df = pd.DataFrame(transformed , columns=Encoder.get_feature_names_out())
    # df = pd.concat([df[['age' , 'bmi', 'children']] , transformed_df] , axis = 1)
    
    #df[['age' , 'bmi']] = scaler.transform(df[['age' , 'bmi']])
    
    #df = pd.DataFrame( poly.fit_transform(df) , columns=poly.get_feature_names_out())
    
    result = Model.predict(df)
    return result[0]


def Main():
    Sex  = st.selectbox("Sex" , ["M" , "F"])
    ChestPainType = st.selectbox("ChestPainType", ["ASY", "NAP", "ATA", "TA"]) 
    RestingECG = st.selectbox("RestingECG", ["Normal", "LVH", "ST"]) 
    ExerciseAngina = st.selectbox("ExerciseAngina", ["Y", "N"])
    ST_Slope = st.selectbox("ST_Slope", ["Flat", "Up", "Down"])
    Age = st.slider( "Age",min_value= 20 , max_value=80 , step= 1 , value=45)
    RestingBP = st.slider( "RestingBP",min_value= 50 , max_value=200 , step= 1 , value=120)
    Cholesterol = st.slider( "Cholesterol",min_value= 80 , max_value=410 , step= 1 , value=200)
    FastingBS = st.number_input("FastingBS", min_value= 0 , max_value=1 , step= 1 , value=1)
    MaxHR = st.slider("MaxHR", min_value= 50 , max_value=210 , step= 1 , value=140)
    Oldpeak = st.number_input("Oldpeak", min_value= 0.0 , max_value=4.0 , step= 0.1 , value=1.0, format="%f")
    
    if st.button("Predict"):
        result = Prediction(Sex, ChestPainType, RestingECG, ExerciseAngina, ST_Slope, Age, RestingBP, Cholesterol, FastingBS, MaxHR, Oldpeak)
        
        if result == 1:
            st.text(f"Has Heart Disease")
        elif result == 0:
            st.text(f"Has No Heart Disease")
    
    

Main()
