import streamlit as st

def app():
    st.title("MAVERICK DEVELOPERS")
    st.write("Check Out Our Research Paper On Maverick At: [Maverick-bot](abc.com) and also Check Out Our Survey Paper On Bots At: [A Survey On ChatBots](https://tinyurl.com/4j7jtba5)")

    select = st.selectbox("Research Members",["Group","Mr.Mrigesh Deshpande","Mr.SunnyAnand Jha","Mr.Rohil Wattal","Mr.Rohit Vig"])
    if select == "Mr.SunnyAnand Jha":
        st.subheader("About SunnyAnand Jha")
        st.text("Final Year Student at Dy Patil institute of technology\nEmail:- jhasunny19@gmail.com\nContact Number:-9987805195")
    elif select == "Mr.Mrigesh Deshpande":
        st.subheader("About Mrigesh Deshpande")
        st.text("Final Year Student at Dy Patil institute of technology\nEmail:- mrigeshdeshpande246@gmail.com\nContact Number:-9993307810")
    elif select == "Mr.Rohil Wattal":
        st.subheader("About Rohil Wattal")
        st.text("Final Year Student at Dy Patil institute of technology\nEmail:- rohiljan@gmail.com\nContact Number:-8585988103")
    elif select == "Mr.Rohit Vig":
        st.subheader("About Rohit Vig")
        st.text("Final Year Student at Dy Patil institute of technology\nEmail:- rohitvig365@gmail.com\nContact Number:-8855051068")

    