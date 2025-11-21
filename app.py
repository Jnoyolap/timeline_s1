import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Título de la aplicación
st.title("Timeline con Slider")

# Lista de URLs de las imágenes en GitHub
# Reemplaza 'usuario', 'repositorio' y 'branch' con los tuyos
base_url = "https://github.com/Jnoyolap/timeline_s1/tree/main/timeline_images"
images = [
    base_url + "imagen1.jpg",
    base_url + "imagen2.jpg",
    base_url + "imagen3.jpg",
    base_url + "imagen4.jpg",
    base_url + "imagen5.jpg"
]

# Slider con 5 puntos
index = st.slider("Selecciona el punto del timeline", 1, 5, 1)

# Cargar la imagen correspondiente
img_url = images[index - 1]
response = requests.get(img_url)
img = Image.open(BytesIO(response.content))

# Mostrar la imagen
st.image(img, caption=f"Imagen {index}", use_column_width=True)
