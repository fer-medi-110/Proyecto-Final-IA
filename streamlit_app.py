import streamlit as st
import pandas as pd
st.title("IA Algorithms Web App")
st.subheader("¡¡¡Bienvendidos a mi web interactiva de Machine Learning!!!")
st.header("Bienvenidos")
st.text("Puedes elegir 3 algoritmos de Machine Learning") 
st.markdown("**A priori | Métricas de distancia**")
DatosMovies = pd.read_csv('Datos/movies.csv')
st.table(DatosMovies)
