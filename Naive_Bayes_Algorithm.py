import streamlit as st
import pickle
pickle_in=open('Play_Tennis.pkl','rb')
model=pickle.load(pickle_in)
Outlook=st.number_input('Enter Outlook : ')
Temperature=st.number_input('Enter Temperature : ')
Humidity=st.number_input('Enter Humidity : ')
Wind=st.number_input('Enter Wind : ')
Value=""
if st.button("PREDICT"):
  result=model.predict([Outlook,Temperature,Humidity,Wind])
  if result==1:
    st.success("You Can Play Tennis")
  else:
    st.success("You Can't Play Tennis")
