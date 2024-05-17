import streamlit as st
from pathlib import Path
import base64

st.set_page_config(
     page_title='Cozitas',
     layout="wide",
     initial_sidebar_state="expanded",
)

def main():
    cs_sidebar()
    cs_body()

    return None

def cs_sidebar():
    def img_to_bytes(img_path):
        img_bytes = Path(img_path).read_bytes()
        encoded = base64.b64encode(img_bytes).decode()
        return encoded

    st.sidebar.markdown('''[<img src='data:image/png;base64,{}' class='img-fluid' width=32 height=32>](http://localhost:8501/)'''.format(img_to_bytes("download.png")), unsafe_allow_html=True)

def cs_body():
    st.title("Welcome")
    st.text('Site feito para testes')
    st.info('Informação somente', icon="ℹ️")


if __name__ == '__main__':
    main()