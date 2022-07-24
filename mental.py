import pandas as pd
import numpy as np
import string
import re
import nltk
import streamlit as st
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords 
stopwords=stopwords.words('english')
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
le= LabelEncoder()
from sklearn.svm import LinearSVC
lsvc = LinearSVC(random_state = 2021)


def data_prep(text):
  text=text.lower()
  text = re.sub(r'[^\w\s]', '', text)
  text=" ".join(t for t in text.split() if t not in stopwords)
  return text

df = pd.read_csv('mental.csv')
df=df.drop(["Question_ID"],axis="columns")
df["Questions"]=df["Questions"].apply(data_prep)
tf=TfidfVectorizer()
tf_train=tf.fit_transform(df["Questions"])
df_check=pd.DataFrame(tf_train.toarray(),columns=tf.get_feature_names())
df["Answers_Code"]=le.fit_transform(df["Answers"])
lsvc.fit(df_check,df["Answers_Code"])
Ans=df["Answers"].unique()
Ans=Ans.tolist()
Ans_Code=df["Answers_Code"].unique()
Ans_Code=Ans_Code.tolist()

def app():
    st.title("Mental healthcare FAQ's")
    st.image("https://image.shutterstock.com/image-vector/cute-chatbot-robot-assistant-different-600w-1984034186.jpg")
    text = st.selectbox("Example questions related to mental healthcare",(st.text_input("Ask any question related to mental healthcare "),"What does it mean to have a mental illness?","What causes mental illness?","What are some of the warning signs of mental illness?",
    "How can I use distraction to manage difficult thoughts or feelings?"))
    if text!=None:
        tx =[]
        tx.append(text)
        testing=tf.transform(tx)
        result = lsvc.predict(testing)[0]
        r  = Ans_Code.index(result)
        if st.button('Submit'):
          st.write(Ans[r])



