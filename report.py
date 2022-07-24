import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as py
import matplotlib.pyplot as plt




# DB Management
import sqlite3 
conn = sqlite3.connect('database_Maverick.db',check_same_thread=False)
c = conn.cursor()

##################DB-Functions###############

def view_all_users_students(username,user_id):
    c.execute('SELECT username,stid,mental_condition ,login_date FROM students_userstable WHERE username =? AND stid =?',(username,user_id))
    data = c.fetchall()
    return data

def view_all_users_employees(username,user_id):
    c.execute('SELECT username,empid,mental_condition,login_date FROM employees_userstable WHERE username =? AND empid =?',(username,user_id))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data

def get_count_employees(condition,username,user_id):
    data = c.execute('SELECT COUNT(mental_condition) FROM employees_userstable WHERE (mental_condition=? AND username =? AND empid =?)',(condition,username,user_id)).fetchone()[0]
    return data

def get_count_students(condition,username,user_id):
    data = c.execute('SELECT COUNT(mental_condition) FROM students_userstable WHERE (mental_condition=? AND username =? AND empid =?)',(condition,username,user_id)).fetchone()[0]
    return data

###################################### platting pie chart ################################
def plot_pie(flag,user_name,user_id):
    # Pie chart, where the slices will be ordered and plotted counter-clockwise:
    labels = 'Good', 'Tired Out', 'Needs Therapy'
    if flag == True:
        mental_states = [get_count_employees('good',user_name,user_id), get_count_employees('Tired out',user_name,user_id), get_count_employees('Needs Therapy',user_name,user_id)]
    else:
        mental_states = [get_count_students('good',user_name,user_id), get_count_students('Tired out',user_name,user_id), get_count_students('Needs Therapy',user_name,user_id)]

         
    explode = (0.2, 0.1, 0) 
    fig1, ax1 = plt.subplots()
    ax1.pie(mental_states, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # Adding legend
    ax1.legend(labels,
		    title ="Mental condition",
		    loc ="center right",
		    bbox_to_anchor =(1, 0, 0.5, 1))

    
    ax1.set_title(" {}'s Mental Health Report".format(user_name))

    st.pyplot(fig1)


###########################################################

def app():

    task = st.selectbox("Task",["Select","Get Motivated","Analysis","Profiles"])




    if task == "Get Motivated":
        st.subheader("Some Motivation Quotes From Maverick ")
        with open("Motivation.txt", "r", encoding="utf-8") as file:
            for line in file:
                st.write(line.strip())

    elif task == "Analysis":
        st.subheader("Your Performance")
        user_name = st.text_input("Enter your Name")
        user_id = st.text_input("Enter your ID")
        selected = st.selectbox("You are a/an",["Select","Student","Employee"])

        if st.button("Submit"):


            if selected == "Student":
                st.subheader("{}'s Detailed Report".format(user_name))
                plot_pie(False,user_name,user_id)
                st.subheader("\n {}'s Detailed Report In Tabular Form With Dates \n".format(user_name))
                user_result = view_all_users_students(user_name,user_id)
                clean_db = pd.DataFrame(user_result,columns=["Std_Name","Std_id","Mental Condition","date"])
                st.dataframe(clean_db)
                
        
            elif selected == "Employee":
                st.subheader("{}'s Detailed Report".format(user_name))
                plot_pie(True,user_name,user_id)
                st.subheader("\n {}'s Detailed Report In Tabular Form With Dates \n".format(user_name))
                user_result = view_all_users_employees(user_name,user_id)
                clean_db = pd.DataFrame(user_result,columns=["Std_Name","Std_id","Mental Condition","date"])
                st.dataframe(clean_db)
                

    elif task == "Profiles":
        st.subheader("All User Profiles")
        user_result = view_all_users()
        clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
        st.dataframe(clean_db)