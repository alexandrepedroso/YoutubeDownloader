import os
import json
import requests
import streamlit as st
from pytube import YouTube

st.set_page_config(page_title='Python YT Downloader', page_icon='LogotipoSite.png', menu_items=None)
with open("styles.css") as f:
    st.markdown(fr"<head><meta charset='UTF-8'><meta http-equiv='X-UA-Compatible' content='IE=edge'><meta name='viewport' content='width=device-width, initial-scale=1.0'<link rel='stylesheet' href='https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'><title>Baixador</title></head><body><header><i class='fa-brands fa-github'></i></header><img class='imagem' src=https://i.ibb.co/jMgLQwg/Logotipo-circular-monograma-elegante-feminino-amarelo-e-preto-2-removebg-preview.png><footer><span class='carregando'></span></footer></body><style>{f.read()}</style>", unsafe_allow_html= True)


st.title(' Baixador de vídeos - Youtube')



def baixar ():
    caminho = st.text_input('Insira o link do vídeo:')
    opcao = st.selectbox('Selecione o formato que deseja baixar:',('Áudio','Alta Resolução', 'Baixa Resolução'))
    video = YouTube(caminho)

    matches= ['Áudio','Alta Resolução', 'Baixa Resolução']
    if st.button ('Baixar'):
        video = YouTube(caminho)
        st.error(' ⬇️ Download sendo realizado ⬇️',)        
        st.write("Título do Video: " + str(video.title) + "  |  Views: " + str(video.views))
        st.video(caminho)
        if opcao =='Áudio':
            video = video.streams.filter(only_audio=True).first()
            out_file = video.download()
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
        elif opcao =='Alta Resolução':
            video.streams.filter(progressive=True).get_highest_resolution().download()
            st.write('Download feito!')
        elif opcao =='Baixa Resolução':
            video.streams.filter(progressive=True).get_lowest_resolution().download()
            st.write('Download feito!')

if __name__ == '__main__':
	baixar()