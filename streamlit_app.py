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
st.sidebar.image("ML.jpg")
st.sidebar.header("Algoritmos de IA Disponibles")
boton1 = st.sidebar.button("Apriori")
boton2 = st.sidebar.button("Métricas de distancia")
boton3 = st.sidebar.button("Clustering")
boton4 = st.sidebar.button("Regresión logística")
if (boton1):
  st.text("Bienvenido a la sección Apriori")
  archivo = st.file_uploader("Ingresa tu archivo .csv")
  st.markdown("Este es el contenido del archivo")
  if (archivo != None):
    st.markdown("Este es el contenido del archivo")
    st.dataframe(archivo)
  st.write("Apriori")
