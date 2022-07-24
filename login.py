###import streamlit as st


#def main():

    #st.title(" Welcome To Maverick ")
    #menu = ["Home","Login","Sign Up"]
    #choice = st.sidebar.selectbox("Menu",menu)

    #if choice == "Home":
    #    st.subheader("Home")
   # elif choice == "Home":
     #   st.subheader("Login Section")
    #    username = st.sidebar.text_input("User Name")
   #     password = st.sidebar.text_input("Password",type='password')
  #      if st.sidebar.button("Login"):
   #         st.success

  #  elif choice == "Sign Up":
 #       st.subheader("Create New Account")
#if __name__ == '__main__':
##    main()
#

import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu
import ha
import mental
import burnrate
import student
import numpy as py


#######################################
# Security LOGIN
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
conn = sqlite3.connect('data.db')
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

######################################





def app():

	"""Simple Login App"""

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



	if choice == "Home":
        
		st.subheader("Login App with SQL Database")
        ############################


        ###########################





	elif choice == "Login":
		st.subheader("Login Section")

		username = st.text_input("User Name")
		password = st.text_input("Password",type='password')


		if st.checkbox("Login"):
			
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))



			if result:
                
          
                
				st.success("Welcome To Maverick {}".format(username))

				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")

				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)


                # PAGES = {
                #        "Mental healthcare chatbot": mental ,
                #        "Mental disease": ha ,
                #        "Employee Burnrate Calculator":burnrate,
                #         "Student Burnrate Calculator":student,
                # }
                # selection = st.sidebar.radio("Go to", list(PAGES.keys()))
                # page = PAGES[selection]
                # page.app()
			else:
				st.warning("Incorrect Username/Password")


	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')
        #check if new_password has at least 8 characters
		if st.button("Signup"):
            

			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created an Account")
			st.info("Go to Login Menu to login")

    

    
