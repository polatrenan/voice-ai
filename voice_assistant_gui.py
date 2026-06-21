"""
Voice AI Assistant - GUI Version
Mooie interface met spraakbesturing
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
import threading
import speech_recognition as sr
import pyttsx3
import subprocess
import os
import webbrowser
from pathlib import Path
import json

class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎙️ Voice AI Assistant")
        self.root.geometry("900x700")
        self.root.configure(bg="#2c3e50")
        
        # Voice setup
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)
        
        self.is_listening = False
        self.commands_log = []
        
        self.setup_ui()
        
    def setup_ui(self):
        """Setup de GUI"""
        
        # Header
        header = tk.Frame(self.root, bg="#34495e")
        header.pack(fill=tk.X, pady=10)
        
        title = tk.Label(header, text="🎙️ Voice AI Assistant", 
                        font=("Arial", 24, "bold"), bg="#34495e", fg="white")
        title.pack()
        
        subtitle = tk.Label(header, text="Spreken met je computer", 
                           font=("Arial", 12), bg="#34495e", fg="#ecf0f1")
        subtitle.pack()
        
        # Control buttons
        button_frame = tk.Frame(self.root, bg="#2c3e50")
        button_frame.pack(pady=10)
        
        self.listen_btn = tk.Button(button_frame, text="🎤 Luisteren", 
                                    command=self.start_listening,
                                    font=("Arial", 12, "bold"),
                                    bg="#27ae60", fg="white", 
                                    padx=20, pady=10)
        self.listen_btn.pack(side=tk.LEFT, padx=5)
        
        self.stop_btn = tk.Button(button_frame, text="⏹️ Stoppen", 
                                 command=self.stop_listening,
                                 font=("Arial", 12, "bold"),
                                 bg="#e74c3c", fg="white", 
                                 padx=20, pady=10, state=tk.DISABLED)
        self.stop_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(button_frame, text="🗑️ Wissen", 
                             command=self.clear_log,
                             font=("Arial", 12, "bold"),
                             bg="#3498db", fg="white", 
                             padx=20, pady=10)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # Log text area
        log_label = tk.Label(self.root, text="📝 Log:", 
                            font=("Arial", 12, "bold"), bg="#2c3e50", fg="white")
        log_label.pack(anchor=tk.W, padx=20, pady=(10, 5))
        
        self.log_text = scrolledtext.ScrolledText(self.root, 
                                                  height=15, width=100,
                                                  bg="#34495e", fg="#ecf0f1",
                                                  font=("Courier", 10))
        self.log_text.pack(padx=20, pady=5)
        self.log_text.config(state=tk.DISABLED)
        
        # Status bar
        self.status_var = tk.StringVar(value="⚪ Klaar")
        status_bar = tk.Label(self.root, textvariable=self.status_var,
                             font=("Arial", 10), bg="#34495e", fg="#ecf0f1")
        status_bar.pack(fill=tk.X, padx=20, pady=5)
        
    def add_log(self, message, color="white"):
        """Add message to log"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        
    def start_listening(self):
        """Start listening in a thread"""
        self.is_listening = True
        self.listen_btn.config(state=tk.DISABLED)
        self.stop_btn.config(state=tk.NORMAL)
        self.status_var.set("🔴 Luistert...")
        
        thread = threading.Thread(target=self.listen_loop, daemon=True)
        thread.start()
        
    def stop_listening(self):
        """Stop listening"""
        self.is_listening = False
        self.listen_btn.config(state=tk.NORMAL)
        self.stop_btn.config(state=tk.DISABLED)
        self.status_var.set("⚪ Gestopt")
        
    def listen_loop(self):
        """Listen for commands"""
        try:
            with sr.Microphone() as source:
                self.add_log("\n🎤 Luister naar je stem...")
                audio = self.recognizer.listen(source, timeout=10)
                
            try:
                text = self.recognizer.recognize_google(audio, language="nl-NL")
                self.add_log(f"✅ Je zei: '{text}'")
                self.process_command(text)
            except sr.UnknownValueError:
                self.add_log("❌ Kon niet verstaan, probeer opnieuw")
            except sr.RequestError:
                self.add_log("❌ Geen internet voor spraakherkenning")
                
        except Exception as e:
            self.add_log(f"❌ Fout: {str(e)}")
        finally:
            self.status_var.set("⚪ Klaar")
            
    def process_command(self, text):
        """Process the spoken command"""
        text = text.lower()
        
        # Open programs
        if "open" in text or "start" in text:
            if "github" in text:
                self.add_log("🌐 GitHub openen...")
                webbrowser.open("https://github.com")
                self.speak("GitHub wordt geopend")
            elif "roblox" in text:
                self.add_log("🎮 Roblox openen...")
                webbrowser.open("https://www.roblox.com")
                self.speak("Roblox wordt geopend")
            elif "youtube" in text:
                self.add_log("📺 YouTube openen...")
                webbrowser.open("https://www.youtube.com")
                self.speak("YouTube wordt geopend")
            elif "google" in text:
                self.add_log("🔍 Google openen...")
                webbrowser.open("https://www.google.com")
                self.speak("Google wordt geopend")
            elif "notepad" in text or "kladblok" in text:
                self.add_log("📝 Notepad openen...")
                os.startfile("notepad.exe")
                self.speak("Notepad wordt geopend")
            elif "paint" in text or "schilderen" in text:
                self.add_log("🎨 Paint openen...")
                os.startfile("mspaint.exe")
                self.speak("Paint wordt geopend")
            elif "verkenner" in text or "files" in text:
                self.add_log("📁 Verkenner openen...")
                os.startfile("explorer.exe")
                self.speak("Verkenner wordt geopend")
            else:
                self.add_log("❓ Welk programma wil je openen?")
                self.speak("Ik begrijp niet welk programma je wilt openen")
                
        # File operations
        elif "maak" in text or "create" in text:
            if "bestand" in text or "file" in text:
                self.add_log("📝 Nieuw bestand aanmaken...")
                self.speak("Ik maak een nieuw bestand")
                # Maak een simpel bestand aan
                with open(os.path.expanduser("~/Desktop/new_file.txt"), "w") as f:
                    f.write("Dit is een nieuw bestand gemaakt door Voice AI\n")
                self.add_log("✅ Bestand gemaakt op Desktop")
                
        # Website navigation
        elif "bezoek" in text or "go to" in text or "surf naar" in text:
            self.add_log("🌐 Website openen...")
            self.speak("Website wordt geopend")
            if "google" in text:
                webbrowser.open("https://www.google.com")
            elif "youtube" in text:
                webbrowser.open("https://www.youtube.com")
            elif "github" in text:
                webbrowser.open("https://github.com")
            else:
                webbrowser.open("https://www.google.com")
                
        # Help
        elif "help" in text or "wat kun je" in text or "mogelijkheden" in text:
            help_text = """
ℹ️ Je kan zeggen:
- 'Open GitHub/Roblox/YouTube/Google'
- 'Open Notepad/Paint/Verkenner'
- 'Maak een bestand'
- 'Bezoek [website]'
- 'Wat is de tijd?'
- 'Stop' om af te sluiten
            """
            self.add_log(help_text)
            self.speak("Ik kan veel commando's uitvoeren. Zeg help voor meer info")
            
        else:
            self.add_log(f"❓ Commando niet herkend: '{text}'")
            self.speak("Dit commando begrijp ik niet")
            
    def speak(self, text):
        """Speak text using text-to-speech"""
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except:
            pass
            
    def clear_log(self):
        """Clear the log"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.add_log("📋 Log gewist")

def main():
    root = tk.Tk()
    app = VoiceAssistantGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
