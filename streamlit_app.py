import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import openai
import os

# Configurar la API de OpenAI




# Crear una instancia del ChatBot
bot = ChatBot('VendedorBot')

# Entrenar el bot con datos de entrenamiento
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.spanish')

# Función para generar respuestas utilizando GPT-3
def generate_response(input_text):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=input_text,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

# Configurar la interfaz de Streamlit
st.title('Asistente de Vendedores de Inmuebles')

# Función para obtener la respuesta del bot
def get_bot_response(user_input):
    bot_response = bot.get_response(user_input).text
    if bot_response == 'No se que responder':
        bot_response = generate_response(user_input)
    return bot_response

# Interacción con el usuario
user_input = st.text_input('Tú:')

if user_input:
    bot_response = get_bot_response(user_input)
    st.text(f'Bot: {bot_response}')
