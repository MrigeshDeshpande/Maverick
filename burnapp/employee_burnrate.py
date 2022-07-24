import streamlit as st
import numpy as np
import pickle

from PIL import Image
image = Image.open('/Users/ashwinv/Documents/GitHub/burnapp/imgs/banner.webp')

st.image(image)

st.title('Employee Burnrate Calculator')



gender = st.selectbox(
    'What is your gender?',
    ('Male', 'Female'))
st.write('You selected:', gender)

cctype = st.selectbox(
    'What type of company do you work in?',
    ('Service based', 'Product based'))
st.write('You selected:', cctype)

wfh = st.selectbox(
    'Does your company have work-from-home options?',
    ('Yes they do', 'No they do not'))
st.write('You selected:', wfh)

rolee = st.selectbox(
    'How do you best descibe your role in your company?',
    ('Management', 'Technical','Human Resources','sales','Marketing','Finance'))
st.write('You selected:', rolee)

hrall = st.select_slider(
    'How many hours do you work per day?',
    options=[1,2,3,4,5,6,7,8,9,10])
st.write('You selected:', hrall)

fat = st.select_slider(
    'On a scale of 1 to 10 how mentally fatigues are you',
    options=[1,2,3,4,5,6,7,8,9,10])
st.write('You selected:', fat)

def encode(arr):
    b = []
    for i in range(len(arr)):
        if(arr[i] == 'Male'):
            b.append(1)
        elif(arr[i] == 'Female'):
            b.append(0)
        elif(arr[i] == 'Product based'):
            b.append(0)
        elif(arr[i] == 'Service based'):
            b.append(1)
        elif(arr[i] == 'No they do not'):
            b.append(0)
        elif(arr[i] == 'Yes they do'):
            b.append(1)
        elif(arr[i] == 'Management'):
            b.append(0) 
        elif(arr[i] == 'Technical'):
            b.append(1) 
        elif(arr[i] == 'Human Resources'):
            b.append(2)    
        elif(arr[i] == 'sales'):
            b.append(3) 
        elif(arr[i] == 'Marketing'):
            b.append(4)
        elif(arr[i] == 'Finance'):
            b.append(5)      
        else:
            b.append(arr[i])
    b = np.array([b])
    return b



# st.write(av)
# st.write(ave)


if st.button('Start Calculation'):

    av = [gender,cctype,wfh,rolee,hrall,fat]
    ave = encode(av)
    # st.write(ave)
    # st.write(type(ave))
    ave = ave.astype(np.int)
    print(ave)
    with open("/Users/ashwinv/Documents/GitHub/burnapp/Models/XGBoost.pkl", 'rb') as file:
        pickle_model = pickle.load(file)
    Ypredict = pickle_model.predict(ave)
    # st.write('prediction is:', Ypredict)
    if(Ypredict <= 0.4):
        st.success('You are not burnt out, you can keep working!! 😄')
    elif(Ypredict>0.4 and Ypredict<=0.7):
        st.warning('You are tired of work, Please take rest and take a break!! 😊🍸')
    else:
        st.error('You are burnt out, please visit a professional for further support')













