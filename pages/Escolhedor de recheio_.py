import random
import streamlit as st

recheio_1 = ['CARNE MOIDA', 'FRANGO', 'PERNIL DESFIADO']
recheio_2 = ['MUSSARELA', 'CHEDDAR', 'REQUEIJÃO CREMOSO', 'PROVOLONE', 'QUEIJO MINAS', 'CREAM CHEESE']
recheio_3 = ['AZEITONA', 'PALMITO', 'BANANA FRITA', 'BACON', 'CALABRESA', 'CHAMPIGNON', 'PEQUI', 'GUARIROBA', 'MILHO', 'PRESUNTO', 'OVO', 'ATUM', 'LOMBO DEFUMADO', 'UVA PASSAS', 'PATE DE FRANGO']

a = random.choice((recheio_1))



col1, col2, col3 = st.columns(3)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

st.sidebar.title('Selecionador de Sabores')

with col1:
   st.header("Recheio 1")

   if st.button('Escolha 1', on_click=click_button):
       st.markdown(a)

   if st.session_state.clicked:
       st.markdown(random.choice((recheio_1)))

   st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
   st.header("Recheio 2")

   if st.button('Escolha 2', on_click=click_button):
       st.markdown(random.choice((recheio_2)))

   if st.session_state.clicked:
       st.markdown(random.choice((recheio_2)))

   st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("Recheio 3")

    if st.button('Escolha 3', on_click=click_button):
        st.markdown(random.choice((recheio_3)))

    if st.session_state.clicked:
        st.markdown(random.choice((recheio_3)))

    st.image("https://static.streamlit.io/examples/owl.jpg")