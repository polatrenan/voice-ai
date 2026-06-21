"""
Script om voice_assistant_gui.py om te zetten naar .EXE
Run: python build_exe.py
"""

import subprocess
import sys
import os

print("🔨 Voice AI Assistant naar .EXE converteren...")
print("=" * 50)

# Check if PyInstaller is installed
try:
    import PyInstaller
except ImportError:
    print("📦 PyInstaller installeren...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyInstaller"])

print("\n⚙️ .EXE aan het builden...")
subprocess.check_call([
    sys.executable, "-m", "PyInstaller",
    "--onefile",
    "--windowed",
    "--icon=NONE",
    "--name=Voice_AI_Assistant",
    "--add-data=.",
    "voice_assistant_gui.py"
])

print("\n✅ Klaar!")
print("📁 Je .EXE staat in: dist/Voice_AI_Assistant.exe")
print("💾 Zet het op je USB stick!")
