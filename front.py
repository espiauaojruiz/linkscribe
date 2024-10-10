import streamlit as st
import requests

st.title("Web-Screaping")
st.spinner('Cargando...')
user_input = st.text_input("Introduce url:")

#metodo q valida el inicio de la url y lo ajusta
def validar_url(url):
    if not url.startswith(('http://', 'https://')):
        # Si no comienza con ninguno, agregar "https://"
        url = 'https://' + url
    return url

# Función para mostrar el JSON de forma organizada
def mostrar_datos_json(json_data):

    # Mostrar el título de los datos
    st.header(json_data['data']['title'])

    # Mostrar la imagen de vista previa
    st.image(json_data['data']['previewLink'], width=400, caption="Logo de USAGov")

    # Descripción
    st.subheader("Descripción")
    st.markdown(f"**{json_data['data']['description']}**")

    # Categoría
    st.subheader("Categoría")
    st.write(f" {json_data['data']['category']} (Índice: {json_data['data']['categoryIndex']})")

    # Status y mensaje
    st.subheader("Estado de la Respuesta")
    st.write(f"Status: {json_data['status']}")
    st.write(f"Mensaje: {json_data['message']}")



if st.button("Enviar"):



    url_validada = validar_url(user_input)

    api_url = "http://linkscribe.australiaeast.cloudapp.azure.com:8000/classificate"

  
    payload = {
        "url": url_validada
    }
     # Hacer la solicitud POST a la API
    response = requests.post(api_url, json=payload)
    response.status_code = 200 

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
         # Obtener los datos en formato JSON
        api_data = response.json()
        try:
            mostrar_datos_json(api_data)
        except (ValueError, ZeroDivisionError,Exception) as e:    
            st.write(api_data)

    else:
        # Mostrar un mensaje de error si la llamada a la API falla
        st.error(f"Error al llamar a la API. Código de estado: {response.status_code}")




