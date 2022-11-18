pip install apyori
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import apriori
st.title("IA Algorithms Web App")
st.subheader("¡¡¡Bienvendidos a mi web interactiva de Machine Learning!!!")
st.header("Bienvenidos")
st.text("Puedes elegir 3 algoritmos de Machine Learning") 
st.markdown("**A priori | Métricas de distancia**")
DatosMovies = pd.read_csv('Datos/movies.csv')
#st.table(DatosMovies)
MoviesLista = DatosMovies.stack().groupby(level=0).apply(list).tolist()
ReglasC1 = apriori(MoviesLista, 
                   min_support=0.01, 
                   min_confidence=0.3, 
                   min_lift=2)
