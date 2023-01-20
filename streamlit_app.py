
import streamlit as st
import pandas as pd

st.header("Hello")
df=pd.DataFrame({
  'No':[1,2,3,4,5],
  'Nama':['Kucing','Tikus','Ayam','Burung','Bebek']
})

st.write(df)
