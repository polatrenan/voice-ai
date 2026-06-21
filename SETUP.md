# Voice AI Assistant - Setup Handleiding

## 🚀 Stap 1: Installeer Python

Zorg dat Python 3.9+ geïnstalleerd is:
```bash
python --version
```

## 🔧 Stap 2: Installeer Dependencies

```bash
# Clone de repository
git clone https://github.com/polatrenan/voice-ai.git
cd voice-ai

# Installeer Python packages
pip install -r requirements.txt
```

## 🤖 Stap 3: Installeer Ollama (voor AI)

Dit is OPTIONEEL maar sterk aanbevolen voor het AI-gedeelte.

1. Download Ollama van: https://ollama.ai
2. Installeer het
3. Open terminal/PowerShell en voer uit:
```bash
ollama serve
```

4. In een ander terminal-venster:
```bash
ollama pull llama2
```

Dit downloadt het AI-model (~4GB).

## 🔑 Stap 4: GitHub Token (optioneel)

Voor GitHub-functies:

1. Ga naar: https://github.com/settings/tokens
2. Klik "Generate new token" → "Generate new token (classic)"
3. Zet vinkje bij `repo` en `gist`
4. Klik "Generate token" en kopieer het

5. Maak `.env` bestand in je project-map:
```
GITHUB_TOKEN=jouw_token_hier
GITHUB_USERNAME=jouw_username_hier
```

**BELANGRIJK**: Voeg `.env` NOOIT toe aan GitHub! Het staat al in `.gitignore`.

## 🎙️ Stap 5: Start de AI

```bash
python main.py
```

Je ziet:
```
╔═══════════════════════════════════════╗
║     🎙️  Voice AI Assistant 🎙️        ║
║                                       ║
║  Zeg "Hey Assistant" om te starten   ║
║  Zeg "Stop" om af te sluiten         ║
╚═══════════════════════════════════════╝

🔍 Systemen controleren...
✅ Voice systeem gereed
✅ Ollama/AI beschikbaar
✅ GitHub verbonden

📢 Zeg 'Hey Assistant' om me wakker te maken...
```

## 🗣️ Voorbeelden van Commando's

Zeg "Hey Assistant" eerst, daarna:

### GitHub
- "Maak een repository genaamd mijn-project"
- "Toon mijn repositories"
- "Maak een branch genaamd feature-x"

### Bestanden
- "Open notepad"
- "Open bestandsverkenner"
- "Open browser"

### AI Vragen
- "Wat is Python?"
- "Leg uit hoe git werkt"
- "Maak een hello world script"

## ⚠️ Troubleshooting

### "Spraakherkenning werkt niet"
- Zorg dat je mic goed is ingesteld
- Zet volume hoger
- Probeer dichterbij de mic te spreken

### "Ollama niet beschikbaar"
- Start `ollama serve` in terminal
- Wacht tot het klaar is
- Probeer opnieuw

### "GitHub fout"
- Check je `.env` file
- Controleer je token is geldig
- Zorg dat je online bent

## 📚 Volgende Stappen

- Voeg meer commando's toe in `commands.py`
- Verbeter spraakherkenning met `Whisper`
- Maak een GUI met `tkinter` of `PyQt`
- Voeg database toe voor command history

Veel plezier! 🎉
