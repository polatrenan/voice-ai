"""
Voice Recognition & Text-to-Speech Module
"""

import speech_recognition as sr
import pyttsx3
from config import LANGUAGE, SPEECH_RATE, RECOGNITION_TIMEOUT

class VoiceAssistant:
    def __init__(self):
        """Initialize voice engine"""
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', SPEECH_RATE)
        
        # Nederlands instellingen
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'Dutch' in voice.name or 'Nederlands' in voice.name:
                self.engine.setProperty('voice', voice.id)
                break
    
    def speak(self, text):
        """Spreek tekst uit"""
        print(f"🤖 AI: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Luister naar spraakopdracht"""
        try:
            with sr.Microphone() as source:
                print("👂 Luisteren...")
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = self.recognizer.listen(source, timeout=RECOGNITION_TIMEOUT)
            
            # Probeer Nederlands eerst, dan Engels
            try:
                command = self.recognizer.recognize_google(audio, language=LANGUAGE)
            except:
                command = self.recognizer.recognize_google(audio, language='en-US')
            
            print(f"👤 Je: {command}")
            return command.lower()
        
        except sr.UnknownValueError:
            self.speak("Sorry, ik heb je niet verstaan. Probeer opnieuw.")
            return None
        except sr.RequestError as e:
            self.speak(f"Fout met spraakherkenning: {e}")
            return None
        except Exception as e:
            print(f"Fout: {e}")
            return None
    
    def is_wake_word(self, text):
        """Check of wake word gezegd is"""
        if text is None:
            return False
        return 'hey assistant' in text or 'hallo assistent' in text or 'assistent' in text
