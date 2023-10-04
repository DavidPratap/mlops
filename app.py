import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pickle
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Web Deployment of Medical Diagnostic App ⚕️')
st.subheader("Is the person diabetic ?")
df=pd.read_csv('diabetes.csv')
if st.sidebar.checkbox('View Data', False):
    st.write(df.head())
if st.sidebar.checkbox('View Distributions', False):
    df.hist()
    plt.tight_layout()
    st.pyplot()
    
#Step1: Load the pickled model
model=open('rfc.pickle', 'rb')
clf=pickle.load(model)
model.close()

# Step2: Get the fron-end user input 
pregs=st.number_input('Pregnancies', 0, 17, 0)
glucose=st.number_input('Glucose', 44, 200,44)
bp=st.number_input('BloodPressure', 20, 140, 20)
skin=st.number_input('SkinThickness', 7,99,7)
insulin=st.number_input('Insulin',14,850, 14)
bmi=st.number_input('BMI', 18, 67, 18)
dpf=st.number_input('DiabetesPedigreeFunction', 0.05, 2.50, 0.05)
age=st.number_input('Age', 21, 85, 21)

# step 3 : convert user input to model input
data={
    'Pregnancies':pregs,
    'Glucose':glucose,
    'BloodPressure':bp, 
    'SkinThickness':skin, 
    'Insulin':insulin,
    'BMI':bmi, 
    'DiabetesPedigreeFunction':dpf, 
    'Age':age
}
input_data=pd.DataFrame([data])

# Step4: Get the predictions and print the result
prediction=clf.predict(input_data)[0]
if st.button("Predict"):
    if prediction==1:
        st.subheader('Diabetic')
    else:
        st.subheader('Healthy')
