#pip install apyori
import streamlit as st
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import apriori
st.title("IA Algorithms Web App")
st.subheader("¡¡¡Bienvendidos a mi web interactiva de Machine Learning!!!")
st.header("Bienvenidos")
st.text("Puedes elegir 3 algoritmos de Machine Learning") 
st.markdown("**A priori | Métricas de distancia**")
archivo = st.file_uploader("Ingresa tu archivo .csv")
st.table(archivo)
