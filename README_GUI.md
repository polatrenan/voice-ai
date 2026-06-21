# 🎙️ Voice AI Assistant - GUI Version

Een spraakaangestuurde assistent met een mooie interface!

## ✨ Features

- 🎤 Spraakherkenning (Nederlands)
- 🎨 Mooie GUI interface
- 🌐 Websites openen (GitHub, Roblox, YouTube, Google)
- 📝 Programma's starten (Notepad, Paint, Verkenner)
- 📁 Bestanden beheren
- 🔊 Spraaksynthese (AI spreekt terug)

## 🚀 Installatie

### Optie 1: Rechtstreeks uitvoeren (Python)

```bash
# Zet requirements_new.txt als requirements.txt
pip install -r requirements_new.txt

# Start de app
python voice_assistant_gui.py
```

### Optie 2: .EXE bouwen (voor USB stick)

```bash
# Installeer PyInstaller
pip install PyInstaller

# Build de .EXE
python build_exe.py
```

De .EXE staat in: `dist/Voice_AI_Assistant.exe`

Zet het op je USB stick en je kan het overal uitvoeren!

## 🎤 Hoe te gebruiken

1. Klik op "🎤 Luisteren"
2. Spreken naar je microfoon
3. De app voert je commando uit
4. Luister naar het antwoord

## 💬 Commando's

- "Open GitHub" → GitHub website openen
- "Open Roblox" → Roblox website openen  
- "Open YouTube" → YouTube openen
- "Open Google" → Google openen
- "Open Notepad" → Notepad starten
- "Open Paint" → Paint starten
- "Open Verkenner" → Verkenner openen
- "Maak een bestand" → Nieuw bestand aanmaken
- "Help" → Alle commando's tonen

## 📌 Systeem vereisten

- Windows 10 of hoger
- Microfoon
- Internet (voor websites)
- Python 3.10 of hoger (als je niet de .EXE gebruikt)

## 🐛 Problemen?

### "PyAudio install failed"
```bash
pip install pipwin
pipwin install pyaudio
```

### Microfoon werkt niet
- Zorg dat je microfoon is ingeschakeld
- Test je microfoon in Windows instellingen
- Probeer opnieuw

### Google Speech Recognition werkt niet
- Controleer je internetverbinding
- Probeer opnieuw na een paar seconden

Veel plezier! 🎉
