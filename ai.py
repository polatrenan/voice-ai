"""
AI/LLM Module - Ollama integration
"""

import requests
from config import OLLAMA_MODEL, OLLAMA_HOST

class AIEngine:
    def __init__(self):
        """Initialize Ollama connection"""
        self.host = OLLAMA_HOST
        self.model = OLLAMA_MODEL
        self.system_prompt = """Je bent een Nederlandse AI-assistent die op een computer draait.
Je helpt met:
- GitHub operaties (repositories, branches, pull requests, issues)
- Computertaken (bestanden, mappen, programma's)
- Programmeren en scripts
- Algemene vragen

Antwoord in het Nederlands. Wees kort en duidelijk."""
    
    def generate_response(self, user_message):
        """Generate AI response using Ollama"""
        try:
            response = requests.post(
                f'{self.host}/api/generate',
                json={
                    'model': self.model,
                    'prompt': user_message,
                    'system': self.system_prompt,
                    'stream': False
                },
                timeout=30
            )
            
            if response.status_code == 200:
                result = response.json()
                return result.get('response', 'Ik weet het antwoord niet.')
            else:
                return f"Fout: {response.status_code}"
        
        except requests.exceptions.ConnectionError:
            return "Ollama is niet beschikbaar. Start Ollama en probeer opnieuw. (ollama serve)"
        except Exception as e:
            return f"Fout met AI: {e}"
    
    def check_connection(self):
        """Check of Ollama beschikbaar is"""
        try:
            response = requests.get(f'{self.host}/api/tags', timeout=5)
            return response.status_code == 200
        except:
            return False
