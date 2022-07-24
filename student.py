import streamlit as st
import numpy as np
import pickle

###### sunny_libraries ####
import pandas as pd
import datetime

# DB Management
import sqlite3 
conn = sqlite3.connect('database_Maverick.db',check_same_thread=False)
c = conn.cursor()
 
# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS students_userstable(username TEXT,stid TEXT,mental_condition TEXT,login_date DATE,score REAL)')

def add_userdata(username,stdid,mental_condition,login_date,score):
    c.execute('INSERT INTO students_userstable(username,stid,mental_condition ,login_date,score) VALUES (?,?,?,?,?)',(username,stdid,mental_condition,login_date,score))
    conn.commit()


def view_all_users():
    c.execute('SELECT username,stid,mental_condition ,login_date FROM students_userstable')
    data = c.fetchall()
    return data
############## db ends here ####################

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

def app():
    st.title('Student Burnrate Calculator')
    st.image("https://raw.githubusercontent.com/KiranKhanna721/Mental-Harmony/main/burnapp/imgs/student.png")
    
    ######## sunny__edits #######
    name = st.text_input("Please Enter Your Name")
    std_id = st.text_input("Please Enter Your Student Id")
    user_date = datetime.date.today()
    
    ########   doms  ###############
    create_usertable()

    gender = st.selectbox('What is your gender?',('Male', 'Female'))
    st.write('You selected:', gender)
    cctype = st.selectbox('What type School do you study in?',('Private School', 'Public School'))
    st.write('You selected:', cctype)
    wfh = st.selectbox('Are you currently studying in offline or online mode?',('Online', 'Offline'))
    st.write('You selected:', wfh)
    rolee = st.selectbox('Which Standar are you in right now?',('12th', '11th','10th','9th','8th','7th'))
    st.write('You selected:', rolee)
    hrall = st.select_slider('How many hours do you study per day?',options=[1,2,3,4,5,6,7,8,9,10])
    st.write('You selected:', hrall)
    fat = st.select_slider('On a scale of 1 to 10 how mentally fatigues are you',options=[1,2,3,4,5,6,7,8,9,10])
    st.write('You selected:', fat)
    if st.button('Start Calculation'):
        av = [gender,cctype,wfh,rolee,hrall,fat]
        ave = encode(av)
        ave = ave.astype(np.int)
        print(ave)
        pickle_model = pickle.load(open('xg.pkl','rb'))
        Ypredict = pickle_model.predict(ave)
        if(Ypredict <= 0.4):
            st.success('You are not burnt out, you can keep working!! 😄')

            add_userdata(name,std_id,"Good",user_date,Ypredict)
            st.success('Mr/Ms {} your data is successfully recorded for mental health evaluation.\n Thank you for using MAVERICK'.format(name))## for green colour


        elif(Ypredict>0.4 and Ypredict<=0.7):
            st.warning('You are tired of work, Please take rest and take a break!! 😊')

            add_userdata(name,std_id,"Tired out",user_date,Ypredict)
            st.success('Mr/Ms {} your data is successfully recorded for mental health evaluation.\n Thank you for using MAVERICK'.format(name))## for green colour


        else:
            st.error('You are burnt out, please visit a professional for further support')

            add_userdata(name,std_id,"Needs Therapy",user_date,Ypredict)
            st.success('Mr/Ms {} your data is successfully recorded for mental health evaluation.\n Thank you for using MAVERICK'.format(name))## for green colour
        

        #### display the database ######
        st.subheader("User Profiles")
        user_result = view_all_users()
        clean_db = pd.DataFrame(user_result,columns=["Std_Name","Std_id","Mental Condition","date"])
        st.dataframe(clean_db)

