"""
Voice AI Assistant - Main Application
"""

from voice import VoiceAssistant
from ai import AIEngine
from github_api import GitHubManager
from commands import CommandProcessor

def print_banner():
    """Print welcome banner"""
    print("""
    ╔═══════════════════════════════════════╗
    ║     🎙️  Voice AI Assistant 🎙️        ║
    ║                                       ║
    ║  Zeg "Hey Assistant" om te starten   ║
    ║  Zeg "Stop" om af te sluiten         ║
    ╚═══════════════════════════════════════╝
    """)

def check_systems():
    """Check of alle systemen beschikbaar zijn"""
    print("\n🔍 Systemen controleren...\n")
    
    voice = VoiceAssistant()
    print("✅ Voice systeem gereed")
    
    ai = AIEngine()
    if ai.check_connection():
        print("✅ Ollama/AI beschikbaar")
    else:
        print("⚠️  Ollama niet beschikbaar (optioneel, maar aanbevolen)")
        print("   → Download van: https://ollama.ai")
        print("   → Start: ollama serve")
        print("   → Download model: ollama pull llama2\n")
    
    github = GitHubManager()
    if github.check_connection():
        print("✅ GitHub verbonden")
    else:
        print("⚠️  GitHub niet verbonden (optioneel)")
        print("   → Zet GITHUB_TOKEN in .env bestand\n")

def main():
    """Main application loop"""
    print_banner()
    check_systems()
    
    voice = VoiceAssistant()
    processor = CommandProcessor()
    
    print("\n📢 Zeg 'Hey Assistant' om me wakker te maken...\n")
    
    try:
        while True:
            # Wacht op wake word
            text = voice.listen()
            
            if text is None:
                continue
            
            if 'stop' in text or 'exit' in text or 'quit' in text:
                voice.speak("Tot ziens!")
                print("\n👋 Af!")
                break
            
            if voice.is_wake_word(text):
                voice.speak("Hallo! Wat kan ik voor je doen?")
                
                # Luister naar opdracht
                command = voice.listen()
                
                if command:
                    response = processor.process_command(command)
                    voice.speak(response)
    
    except KeyboardInterrupt:
        print("\n\n👋 Onderbroken. Tot ziens!")

if __name__ == "__main__":
    main()
