import streamlit as st
import numpy as np
import pickle
## changes######
import pandas as pd
import datetime

# DB Management
import sqlite3 
conn = sqlite3.connect('database_Maverick.db',check_same_thread=False)
c = conn.cursor()

# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS employees_userstable(username TEXT,empid TEXT,mental_condition TEXT,login_date DATE,score REAL)')

def add_userdata(username,empid,mental_condition,login_date,score):
    c.execute('INSERT INTO employees_userstable(username,empid,mental_condition,login_date,score) VALUES (?,?,?,?,?)',(username,empid,mental_condition,login_date,score))
    conn.commit()


def view_all_users():
    c.execute('SELECT username,empid,mental_condition,login_date FROM employees_userstable')
    data = c.fetchall()
    return data
########### querys in definitions #######




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

def app():
    st.title('Employee Burnrate Calculator')
    st.image("https://raw.githubusercontent.com/KiranKhanna721/Mental-Harmony/main/burnapp/imgs/banner.webp")


    #### Sunny_additions
    name = st.text_input("Please Enter Your Name")
    emp_id = st.text_input("Please Enter Your Employee Id")
    user_date = datetime.date.today()
    ###### creating user table if it does not exists
    create_usertable()

    ####### do not touch #####
    gender = st.selectbox('What is your gender?',('Male', 'Female'))
    st.write('You selected:', gender)
    cctype = st.selectbox(
        'What type of company do you work in?',
        ('Service based', 'Product based'))
    st.write('You selected:', cctype)
    wfh = st.selectbox('Does your company have work-from-home options?',('Yes they do', 'No they do not'))
    st.write('You selected:', wfh)
    rolee = st.selectbox('How do you best descibe your role in your company?',('Management', 'Technical','Human Resources','sales','Marketing','Finance'))
    st.write('You selected:', rolee)
    hrall = st.select_slider(
        'How many hours do you work per day?',options=[1,2,3,4,5,6,7,8,9,10])
    st.write('You selected:', hrall)
    fat = st.select_slider(
        'On a scale of 1 to 10 how mentally fatigues are you',options=[1,2,3,4,5,6,7,8,9,10])
    st.write('You selected:', fat)
#####################################
    if st.button('Start Calculation'):
        av = [gender,cctype,wfh,rolee,hrall,fat]
        ave = encode(av)
        ave = ave.astype(np.int)
        print(ave)
        pickle_model = pickle.load(open('xg.pkl','rb'))
        Ypredict = pickle_model.predict(ave)
        
        if(Ypredict <= 0.4):
            st.success('You are not burnt out, you can keep working!! 😄')## for green colour
            
            ## store in DB
            add_userdata(name,emp_id,"good",user_date,Ypredict)
            st.success('Mr/Ms {} your data is successfully recorded for mental health evaluation.\n Thank you for using MAVERICK'.format(name))## for green colour

        elif(Ypredict>0.4 and Ypredict<=0.7):
            st.warning('You are tired of work, Please take rest and take a break!! 😊🍸') # for yellow colour
            ## store in DB
            add_userdata(name,emp_id,"Tired out",user_date,Ypredict)

            st.success('Mr/Ms {} your data is successfully recorded for mental health evaluation.\n Thank you for using MAVERICK'.format(name))
        
        else:
            st.error('You are burnt out, please visit a professional for further support') # for red colour
            ## store in DB
            add_userdata(name,emp_id,"Needs Therapy",user_date,Ypredict)

            st.success('Mr/Ms {} your data is successfully recorded for mental health evaluation.\n Thank you for using MAVERICK'.format(name))
        
        st.subheader("User Profiles")
        user_result = view_all_users()
        clean_db = pd.DataFrame(user_result,columns=["Emp_Name","Emp_id","Mental Condition","date"])
        st.dataframe(clean_db)