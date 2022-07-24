import streamlit as st
import numpy as np
import pickle

from PIL import Image
image = Image.open('/Users/ashwinv/Documents/GitHub/burnapp/imgs/student.png')

st.image(image)

st.title('Student Burnrate Calculator')



gender = st.selectbox(
    'What is your gender?',
    ('Male', 'Female'))
st.write('You selected:', gender)

cctype = st.selectbox(
    'What type School do you study in?',
    ('Private School', 'Public School'))
st.write('You selected:', cctype)

wfh = st.selectbox(
    'Are you currently studying in offline or online mode?',
    ('Online', 'Offline'))
st.write('You selected:', wfh)

rolee = st.selectbox(
    'Which Standar are you in right now?',
    ('12th', '11th','10th','9th','8th','7th'))
st.write('You selected:', rolee)

hrall = st.select_slider(
    'How many hours do you study per day?',
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
        elif(arr[i] == 'Private School'):
            b.append(0)
        elif(arr[i] == 'Public School'):
            b.append(1)
        elif(arr[i] == 'Online'):
            b.append(0)
        elif(arr[i] == 'Offline'):
            b.append(1)
        elif(arr[i] == '12th'):
            b.append(0) 
        elif(arr[i] == '11th'):
            b.append(1) 
        elif(arr[i] == '10th'):
            b.append(2)    
        elif(arr[i] == '9th'):
            b.append(3) 
        elif(arr[i] == '8th'):
            b.append(4)
        elif(arr[i] == '7th'):
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
        st.warning('You are tired of work, Please take rest and take a break!! 😊')
    else:
        st.error('You are burnt out, please visit a professional for further support')
