import streamlit as st
import pickle
pickle_in=open('Play_Tennis.pkl','rb')
model=pickle.load(pickle_in)
Outlook=st.selectbox('Enter Outlook : ',('Sunny','Overcast','Rain'))
Temperature=st.selectbox('Enter Temperature : ',('Hot','Mild','Cool'))
Humidity=st.selectbox('Enter Humidity : ',('High','Normal'))
Wind=st.selectbox('Enter Wind : ',('Weak','Strong'))
Value=""
if st.button("PREDICT"):
  result=model.predict([[Outlook,Temperature,Humidity,Wind]])
  if result==1:
    st.success("You Can Play Tennis")
  else:
    st.success("You Can't Play Tennis")
