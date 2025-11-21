import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Título de la aplicación
st.title("Timeline con Slider")

# Lista de URLs de las imágenes en GitHub
# Reemplaza 'usuario', 'repositorio' y 'branch' con los tuyos
base_url = "https://github.com/Jnoyolap/timeline_s1/main/timeline_images"
images = [
    base_url + "timeline1.png",
    base_url + "timeline2.png",
    base_url + "timeline3.png",
    base_url + "timeline4.png",
    base_url + "timeline5.png"
]

# Slider con 5 puntos
index = st.slider("Selecciona el punto del timeline", 1, 5, 1)

# Cargar la imagen correspondiente
img_url = images[index - 1]
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

# Mostrar la imagen
st.image(img, caption=f"Imagen {index}", use_column_width=True)
