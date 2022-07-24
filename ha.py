
import pandas as pd
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import streamlit as st


def preprocess(file):
    path = file+'.txt'
    data = pd.read_csv(path, sep = ';')
    hos = []
    for i in range(len(data.emotion)):
        if data['emotion'][i] in ['joy', 'love', 'surprise']:
            hos.append(1) # happy is 1
        else:
            hos.append(0) # sad is 0
    data['hos'] = hos
    return data

train_data = preprocess('train')
train = train_data.copy()


model = "https://tfhub.dev/google/tf2-preview/gnews-swivel-20dim/1"
hub_layer = hub.KerasLayer(model, output_shape=[20], input_shape=[], 
                           dtype=tf.string, trainable=True)
#hub_layer(train['text'][:3])

model = tf.keras.Sequential()
model.add(hub_layer)
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dense(1))

#model.summary()

model.compile(optimizer='adam',
              loss=tf.losses.BinaryCrossentropy(from_logits=True),
              metrics=[tf.metrics.BinaryAccuracy(threshold=0.0, name='accuracy')])

val = preprocess('val')
#val.head()

history = model.fit(train.text,
                    train.hos,
                    epochs=40,
                    batch_size=512,
                    validation_data=(val.text, val.hos),
                    verbose = 0)

predstr = model.predict(train.text)


def postprocessor(preds):
  range = predstr.max()-predstr.min()
  norm_preds = []
  probab = []
  for i in preds:
    norm_preds.append((i - predstr.min()) / range)
    probab.append((i - predstr.min()) * 100 / range)
  return np.mean(probab)#, probab


def app():
    st.title("Mental Health Disease detection")
    st.image("https://as2.ftcdn.net/v2/jpg/04/91/64/17/1000_F_491641779_GL9KuQtgf6hDAEUEEOQzAXUyIYabxTag.jpg")
    answers = []
    answers.append(st.text_input('How would you describe your experience at your workplace/college/school in the past few days?'))
    answers.append(st.text_input('How do you like to spend your leisure time? How do you feel after it?'))
    answers.append(st.text_input('Life has its ups and downs. Although handling successes can be difficult, setbacks can affect mental health strongly. How do you manage your emotions after failures?'))
    answers.append(st.text_input('Are there any improvements/decline in your salary/grades?'))
    answers.append(st.text_input('In a broad sense, how would you describe the way your life is going on?'))
    if st.button('Submit'):
        results = model.predict(answers)
        score = postprocessor(results)
        #st.write('Your mental health score is:', str(score))

        if score < 35:
            st.warning("You are going through a bad phase in life. But don't worry, bad times are not permanent. Try to seek help from a trained professional to improve your mental health.")
        else:
            st.success("Your mental health looks great! Continue enjoying life and try to help others who are struggling with their mental health.")
