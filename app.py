import streamlit as st
st.title("Evaluación de un lote")
pH = st.number_input("pH", value = 6.5)

temperatura = st.number_input("Temperatura (°C)", value = 23.0)

if st.button("Evaluar"):

    # Completa aquí la lógica
  if pH < 6.00 or pH > 7.00:
      resultado = "Revisar pH"
  elif temperatura < 20.00 or temperatura >25.00:
      resultado = "Revisar temperatura"
  else:
      resultado = "Lote aceptable"

 st.write(f"Resultado: {resultado}")
