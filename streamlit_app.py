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
st.sidebar.button("Apriori")
st.sidebar.button("Métricas de distancia")
st.sidebar.button("Clustering")
st.sidebar.button("Regresión logística")
bottonApriori = st.button("A priori")
if bottonApriori:
  st.text("Es un algoritmo para crear sistemas de recomendaciones")
  archivo = st.file_uploader("Ingresa tu archivo .csv")
  st.markdown("Este es el contenido del archivo")
  st.dataframe(archivo)
  st.write("Apriori")
bottonMetricas = st.button("Métricas de distancia")
if bottonMetricas:
  archivo = st.file_uploader("Ingresa tu archivo .csv")
  st.markdown("Este es el contenido del archivo para métricas")
  st.dataframe(archivo)
  st.write("Métricas")
