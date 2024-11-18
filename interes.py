# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import streamlit as st

st.set_page_config(
    layout="wide",  # Hace que la aplicación use todo el ancho de la pantalla
    initial_sidebar_state="collapsed",  # Colapsa la barra lateral por defecto
)



# Instala Streamlit con: pip install streamlit

import streamlit as st

# Título de la aplicación
st.title("Calculadora de Capital Final")

# Entrada de datos del usuario
capital_inicial = st.number_input("Capital inicial (Co):", min_value=0.0, step=1000.0)
rentabilidad = st.number_input("Rentabilidad esperada (%) por año:", min_value=0.0, step=0.1) / 100
años = st.number_input("Número de años (n):", min_value=1, step=1)

# Botón de calcular
if st.button("Calcular"):
    capital_final = capital_inicial * (1 + rentabilidad) ** años
    st.write(f"El capital final después de {años} años será: ${capital_final:,.2f}")
