# Configuratie voor Voice AI Assistant

import os
from dotenv import load_dotenv

load_dotenv()

# GitHub configuratie
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME', 'polatrenan')

# Ollama configuratie
OLLAMA_MODEL = 'llama2'
OLLAMA_HOST = 'http://localhost:11434'

# Voice configuratie
LANGUAGE = 'nl-NL'  # Nederlands
SPEECH_RATE = 150
RECOGNITION_TIMEOUT = 5  # seconden

# Wake word
WAKE_WORD = 'hey assistant'
