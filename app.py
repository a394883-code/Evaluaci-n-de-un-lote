import streamlit as st
st.title("Evaluación de un lote")
st.sidebar.write("Ximena Garfio Bustillos")
st.sidebar.write("Grupo 3L")
st.sidebar.write("Facultad de Ciencias Quimicas")
pH = st.number_input("pH", value = 6.5)

temperatura = st.number_input("Temperatura (°C)", value = 23.0)

if st.button("Evaluar"):

  if pH < 6.00 or pH > 7.00:
      resultado = "Revisar pH"
  elif temperatura < 20.00 or temperatura >25.00:
      resultado = "Revisar temperatura"
  else:
      resultado = "Lote aceptable"

  st.write(f"Resultado: {resultado}")
