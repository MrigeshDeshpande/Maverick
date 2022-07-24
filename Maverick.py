import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import ha
import mental
import burnrate
import student
import numpy as py
import report
import About_us

import hashlib


# st.sidebar.title('Maverick')


def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def check_hashes(password,hashed_text):
    if make_hashes(password) == hashed_text:
        return hashed_text
    return False

# DB Management
import sqlite3 
conn = sqlite3.connect('database_Maverick.db')
c = conn.cursor()




# DB  Functions
def create_usertable():
    c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
    c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
    conn.commit()

def login_user(username,password):
    c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
    data = c.fetchall()
    return data

def view_all_users():
    c.execute('SELECT * FROM userstable')
    data = c.fetchall()
    return data
### Sunny __ pages that are linked
PAGES = {
        "Mental healthcare FAQ'S": mental ,
        "Mental disease": ha ,
        "Employee Burnrate Calculator":burnrate,
        "Student Burnrate Calculator":student,
        "View you report":report,
        "About Developers":About_us
}

## maverick__ menu

def maverick_menu():
    selection = st.sidebar.radio("Go to", list(PAGES.keys()))
    page = PAGES[selection]
    page.app()

flag=False
check=False
menu = ["Home","Login","SignUp"]
choice = st.sidebar.selectbox("Menu",menu)
    # choice = option_menu(
    #     menu_title=None,
    #     options=["Home","Login","SignUp"],
    #     icons=["house","envelope","book"],
    #     menu_icon="cast",
    #     default_index=0,
    #     orientation="horizontal",
    # )

# appearence change required Status:-done



        ############################
    

########################### Sunny_login_checked   Status:-done####

if choice == "Login":
    st.sidebar.title("Login Section")

    username = st.sidebar.text_input("User Name")
    password = st.sidebar.text_input("Password",type='password')


    if st.sidebar.checkbox("Login"):
            
        create_usertable()
        hashed_pswd = make_hashes(password)

        result = login_user(username,check_hashes(password,hashed_pswd))

        if result:
                              st.success("Welcome To Maverick ,{}".format(username))
                              flag=True
                              maverick_menu()
                              

        else:
            st.sidebar.warning("Incorrect Username/Password")
if choice == "Home":
    st.subheader("Welcome To Maverick\n""WE BELIEVE :: Before the battle of FIST comes the battle of MIND")
    if flag:
        maverick_menu()
        
    

############ Sunny_Sign_up Status:-done############

elif choice == "SignUp":
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password",type='password')
    

    ##### Sunny_check if new_password has at least 8 characters Status:-done #####
     
    if st.button("Signup"):
        

        if len(new_password)<8:
            st.warning("Password too short, Minimum 8 characters required")
        else:
            check = True
        
        if check==True:
            create_usertable()
            add_userdata(new_user,make_hashes(new_password))
            st.success("You have successfully created an Account")
            st.info("Go to Login Menu to login")