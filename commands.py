"""
Command Processing Module
"""

import subprocess
import os
from github_api import GitHubManager
from ai import AIEngine

class CommandProcessor:
    def __init__(self):
        """Initialize command processor"""
        self.github = GitHubManager()
        self.ai = AIEngine()
    
    def process_command(self, command):
        """Process user command"""
        command = command.lower().strip()
        
        # GitHub commands
        if 'github' in command or 'repository' in command or 'repo' in command:
            return self.handle_github_command(command)
        
        # System commands
        elif 'open' in command or 'start' in command:
            return self.handle_open_command(command)
        
        elif 'maak' in command or 'create' in command or 'schrijf' in command:
            return self.handle_create_command(command)
        
        # Default: ask AI
        else:
            return self.ai.generate_response(command)
    
    def handle_github_command(self, command):
        """Handle GitHub commands"""
        if not self.github.check_connection():
            return "GitHub is niet verbonden. Voeg GITHUB_TOKEN toe aan .env"
        
        if 'repository' in command and 'maak' in command:
            # Extract repository name
            words = command.split()
            if 'genaamd' in words:
                idx = words.index('genaamd')
                repo_name = words[idx + 1] if idx + 1 < len(words) else 'new-repo'
                return self.github.create_repository(repo_name)
        
        elif 'issue' in command and 'maak' in command:
            return "Issue aanmaken: zeg 'maak issue in [repo] met titel [titel]'"
        
        elif 'branch' in command and 'maak' in command:
            words = command.split()
            if 'genaamd' in words:
                idx = words.index('genaamd')
                branch_name = words[idx + 1] if idx + 1 < len(words) else 'new-branch'
                return self.github.create_branch('voice-ai', branch_name)
        
        elif 'mijn repositories' in command or 'repositories' in command:
            return self.github.list_repositories()
        
        else:
            return self.ai.generate_response(f"GitHub: {command}")
    
    def handle_open_command(self, command):
        """Handle open/start commands"""
        try:
            if 'notepad' in command or 'editor' in command:
                os.startfile('notepad.exe') if os.name == 'nt' else subprocess.Popen(['gedit'])
                return "Notepad geopend"
            elif 'verkenner' in command or 'explorer' in command or 'bestanden' in command:
                os.startfile('.') if os.name == 'nt' else subprocess.Popen(['nautilus', '.'])
                return "Bestandsverkenner geopend"
            elif 'chrome' in command or 'browser' in command:
                os.startfile('chrome.exe') if os.name == 'nt' else subprocess.Popen(['google-chrome'])
                return "Browser geopend"
            else:
                return "Kan dit programma niet openen"
        except Exception as e:
            return f"Fout: {e}"
    
    def handle_create_command(self, command):
        """Handle create/write commands"""
        if 'python' in command or '.py' in command:
            return "Ik kan een Python script aanmaken. Zeg: 'maak python script genaamd [naam]'"
        elif 'file' in command or 'bestand' in command:
            return "Ik kan een bestand aanmaken. Zeg: 'maak bestand genaamd [naam]'"
        else:
            return self.ai.generate_response(command)
