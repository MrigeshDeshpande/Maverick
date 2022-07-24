## Maverick-Healthcare Chatbot 

The Project's main motivation is to reduce the pressure on primary care providers and assist people in learning to take responsibility for their health. The goal of this healthcare bot is to give patients with individualized health and useful information. Patients with products and services, as well as diagnostics and treatment recommendations. According to the patient's symptoms This healthcare bot technology will assist hospitals in providing better patient care. Healthcare help is available online 24 hours a day, 7 days a week, and it addresses both specific and general queries. By asking the questions in order, patients are guided as to what they are getting into. This, in turn, aids the doctor in gathering information about the patient prior to any physical engagement. 

**Why is this bot now required?**

Bots are automated services that individuals communicate with via a messaging app. Instead of conversing with another human, the user converses with a bot driven by either simple rules or machine learning. Every bot has a purpose, and health bots are developed to assist with medical difficulties. More exact diagnosis and treatment recommendations based on patients' symptoms. Design to assist with health-related concerns Improved user interface. 

## Motivation  ##

The motivation behind building Maverick is to demonstrate the features and the extent to which bots can reach if they are implemented properly. If they are implemented properly, they can be used to replace more traditional options. A bot should be easy to use by all the generations and have a fairly quick response time and it should be user friendly. Their goal should be making the user experience faster & reliable, making sure that they don't waste users time with useless information. 
The conversation flow between the end user and a bot should be effortless and the end user shouldn't feel like he's/she’s talking to a machine.
There are countless cases where intelligent medical bots could help physicians, nurses, therapists, patients, or their families.
They can step in and minimize the amount of time they spend on tasks like:
- ➢ providing health-related information to users
- ➢ guidance for patient
- ➢ medication management and dosage
- ➢ FAQ-type queries (contact details, directions, opening hours and service/treatment details)

It’s important to note that despite the fact that chatbots can offer valuable facts and symptoms, they aren’t qualified to give an official diagnosis.
The main premise behind these talking or texting smart algorithms is to become the first point of contact before any human involvement is needed.

### Problem Definition ###
No one wants to talk about mental health because it's the elephant in the room. Although India is on the edge of a mental health crisis, there is little public discussion on how to avoid or cure it. There are few efforts being done at the scale necessary to deal with the growing number of persons suffering from mental illnesses. Corona is to blame for the significant increase in instances. 

Isolation as a result of lockdown, dread and uncertainty as a result of employment layoffs, and overall discomfort as a result of not being able to manage various elements of life have all contributed to significant emotional trauma in people across the country. The situation is further compounded by the fact that no one knows when, if ever, things will return to normal.

There is a significant gap between the therapy that should be offered and the aid that is conveniently and affordably available. The ratio of psychiatrists, psychologists, psychiatric social workers, and mental health nurses to patients is 1: 10,000 even in industrialized nations. The system's flaw assures that most
people with mental health problems will never receive the treatment they require.

## Assumptions & Dependencies ##
Assumptions:
------
  + The user has to accept required permission(s).
  + User has to fill the required fields appropriately for getting the desired report.
  + New user has to be created every time after a successful test case.
  + Users cannot share the same account, as it hampers the test result
  + User has to enter only one token at a given time
  
Dependencies:
------
  + The Web application needs to have access to the usage statistics of the user’s data.
  + Streamlit is a library in Python used for the front-end of the project. It should be 
    all we need to extract text from a webpage but may be replaced if necessary. We 
     will develop the project using Python and SQLite databases.
     
### System Requirements ###
- Windows OS & Python 3.8.5 & VScode editor

### Software Requirements (PLATFORM CHOICE) ###
------
-  nltk==3.6.5,
-  numpy==1.20.3
-  pandas==1.3.4
-  scikit_learn==1.0.2
-  streamlit==1.8.1
-  tensorflow==2.8.0
-  tensorflow_hub==0.12.0
-  xgboost

## System Design ##
**System Architecture**
------
![image](https://user-images.githubusercontent.com/67750918/180645787-68b00837-f431-41e2-a036-988e03c80263.png)

## Modular architecture ##
------
 The chatbot structure consists of sub-modules: Natural Language Understanding 
(NLU) toolkit, chat management system, FAQ retrieval system, and document search 
module. Before we dive into each module, let's take a look at the workflow.
 When a chatbot detects a question, it transmits the text and removes the relevant 
information from it. This is achieved using an NLU toolkit that includes a target separator 
and a business chip.

Next, it responds to the user. The box management module enables 
the chatbot to chat with the user and support the user with a specific task.
 The BERT-based FAQ return system is a powerful FAQ page query tool and comes 
up with the right answer. The module can help a bot to answer questions even when 
written differently than expected FAQ.

 Even after all this, the chatbot may not have the answer to all users' questions. 
Document search module makes it easy for a bot to search for documents or web pages 
and come up with the right answer. Each part has its own strength. When combined, they 
create a very capable chatbot

### ALGORITHM ###
------
The Nave Bayes method is a supervised learning technique for addressing classification 
issues that is based on the Bayes theorem.
It is mostly utilized in text classification tasks that require a large training dataset.
The Nave Bayes Classifier is a simple and effective classification method that aids in the 
development of fast machine learning models capable of making quick predictions.

It's a probabilistic classifier, which means it makes predictions based on an object's 
probability.
Spam filtration, sentiment analysis, and article classification are all frequent uses of the 
Nave Bayes Algorithm.
The whole process can be brought down to five steps:

**Step 1: Handling Data**
- Data is loaded from the data file and spread into training and tested assets.

**Step 2: Summarizing the Data**
- Summarise the properties in the training data set to calculate the probabilities and make 
predictions.

**Step 3: Making a Prediction**
- A particular prediction is made using a summarise of the data set to make a single 
prediction.

**Step 4: Making all the Predictions**
- Generate prediction given a test data set and a summarise data set.

**Step 5: Evaluate Accuracy**
- Accuracy of the prediction model for the test data set as a percentage correct out of 
them all the predictions made.

**Step 6: Tying all Together**
- Finally, we tie to all steps together and form our own model of Naive Bayes Classifier
------
### DFD Level-0 ### 
![image](https://user-images.githubusercontent.com/67750918/180646178-e0e599fb-f091-4be3-8b5d-d5d2315c6333.png)
------
### Class Diagram(Structural Model) ###
![image](https://user-images.githubusercontent.com/67750918/180646222-1072c0fa-a21c-48c2-8a70-c2a7a7b8d55f.png)
------
### Activity Diagram ###
![image](https://user-images.githubusercontent.com/67750918/180646282-7c876988-8091-46b6-b771-8c2ae4c1d582.png)
------
### Conclusion & Future Work ###
------
 **CONCLUSION**
------
 Medical developments have advanced to the point that we can treat a broader range of 
diseases, new diagnostic and therapeutic methods are emerging, and pharmacology is 
producing an expanding variety of medications for various diseases, ages, body kinds, 
and so on.

 This generates a massive quantity of reference material that doctors must either know 
or remember, which necessitates several years of practice and ongoing learning. They at 
the very least require quick access to such knowledge. Here's what Alan's AI-powered 
chatbots hope to do. Chatbots assist patients in deciding if they should see a specialist 
and, if so, which one, offer answers to simple queries, and remind them to take their 
medicine.

 **FUTURE WORK**
------
*Connecting databases to the internet to improve the diagnosis of mental health*

- ➢ Because of the vast dataset available after connecting to the internet the accuracy 
of the test will also increase providing more accurate results. 

- ➢ In this situation, any synonyms of the entered words which are not in the database 
will be searched for, on the internet and returned with an appropriate result.

- ➢ Connecting the database to the internet also helps in identifying the mental health 
disorders which weren't previously available in the database.

- ➢ The person ought to take the test and the result will be in one of the mainframe 
colors: green, yellow, or red. The green color represents the person having a good 
work-life balance, in short in a good mental state.

- ➢ The Yellow color shows the person has started developing signs/traits of mental 
illness. After taking the test, the report shall be forwarded to the concerned family 
members and the HR department, so that appropriate treatment can be 
channelized.

- ➢ When a person is evaluated to a red color code the evaluation would be shared 
with his / her emergency contact. After contacting the emergency contact of the 
person who has evaluated a red color code a guided 10 min meditation video will 
play to help calm the person down. 

- ➢ This 10 min guided video will act as a distraction in the meantime the emergency 
contact person (Human Resource, Family, Friends, or a Colleague) can get in 
touch with the person.

*Calling the API of Music applications and mind relaxing games*
------
- ➢ Our prediction earlier was limited by our database. By connecting it to the 
internet, we can improve the performance by adding more varied questions and 
answers about the particular ailment from multiple database sources. 
- ➢ After the 10 min guided meditation you’ll be guided to a stress-relieving game. 
While the user is playing the game, motivational songs will be played in the 
background distracting user from suicidal thoughts which can be achieved by 
calling the APIs of music applications available on iOS and android.

*We can use Artificial Intelligence (AI) which may assist with mental health 
detection which will improve the accuracy exponentially*
------

 AI-based protocols may be employed at any moment, providing real-time treatment 
information while maintaining total anonymity. In the areas of illness detection and 
preliminary diagnosis, AI functions as a helper. However, it may only be used as a 
supplement to a doctor and not as a complete replacement. 

AI choices can be incorrect in  non-standard settings. Because mental issues and their complexity vary so widely, a 
"clinical perspective" that AI has yet to acquire is sometimes required.
 Over time, AI mental health treatment procedures will efficiently bridge the gap 
between the patient and treatment availability.

The model might be integrated into mobile apps that track a user's text and speech for 
mental diseases in the future. This is particularly crucial for those who are unable to visit 
a mental health facility for a good diagnosis due to distance, expense, or even fear of 
being vulnerable to a therapist.

-  ➢ Personal perception entails gathering background and behavioral data utilizing
sensors and data from mobile devices. Machine learning is then utilized to 
forecast mental health issues using this data. Mouse and keyboard click habits, 
for example, can provide information about sadness and anxiety.

- ➢ Text and social media content natural language processing Voice and intonation 
can also provide vital details about a person's mental condition. Language 
processing and sound analysis can be used by AI-based systems to detect 
indicators of mental illness. Poor vocabulary, semantic incoherence, and syntactic 
complexity have all been linked to major mental illnesses including schizophrenia 
and other kinds of psychosis, according to research.

- ➢ Conversational interfaces: - Technically, a bot uses answers to messages to 
simulate a real conversation, and it may also integrate advanced sound analysis 
methods. Simple chatbots aid in the navigation and discovery of therapy and 
medical advice. However, AI research is increasingly focusing on using advanced 
language processing algorithms to enable therapeutic dialogue

**APPLICATION**
------
- A chatbot can help you from anywhere with an internet connection, whether you're out 
and about or at home.

- As a result, chatbots enable people to get mental health help from the comfort and safety 
of their own home. (Rather than confronting the possibly intimidating chore of visiting 
an unknown office.)

- Furthermore, chatbots communicate through a well-known route. Texting and instant 
messaging are popular ways for people to communicate in real time. Engaging with a 
chatbot then seems effortless rather than burdensome.

- Chatbots are also available 24 hours a day, seven days a week. So, whether it's late at 
night, early in the morning, or anywhere in between, the bot is available to listen and 
assist.

- Mental health chatbots are also non-committal. If a user changes their mind and isn't 
ready to communicate, they aren't under any obligation to do so. They may just uninstall 
the app or go away from the page.

- There's also the issue that chatbots aren't people. They are unable to pass judgement on 
you. This implies that service users may reach out without being criticised or 
misunderstood
