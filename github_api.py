"""
GitHub API Module
"""

from github import Github
from config import GITHUB_TOKEN, GITHUB_USERNAME

class GitHubManager:
    def __init__(self):
        """Initialize GitHub connection"""
        if not GITHUB_TOKEN:
            print("⚠️  GITHUB_TOKEN niet ingesteld in .env")
            self.github = None
            return
        
        try:
            self.github = Github(GITHUB_TOKEN)
            self.user = self.github.get_user()
            print(f"✅ GitHub verbonden: {self.user.login}")
        except Exception as e:
            print(f"❌ GitHub verbindingsfout: {e}")
            self.github = None
    
    def create_repository(self, name, description="", private=False):
        """Maak een nieuwe repository"""
        try:
            repo = self.user.create_repo(
                name=name,
                description=description,
                private=private,
                auto_init=True
            )
            return f"Repository '{name}' aangemaakt: {repo.html_url}"
        except Exception as e:
            return f"Fout bij aanmaken repository: {e}"
    
    def create_issue(self, repo_name, title, body=""):
        """Maak een issue aan"""
        try:
            repo = self.user.get_repo(repo_name)
            issue = repo.create_issue(title=title, body=body)
            return f"Issue aangemaakt: {issue.html_url}"
        except Exception as e:
            return f"Fout bij aanmaken issue: {e}"
    
    def create_branch(self, repo_name, branch_name, base_branch="main"):
        """Maak een branch aan"""
        try:
            repo = self.user.get_repo(repo_name)
            ref = repo.get_git_ref(f'heads/{base_branch}')
            repo.create_git_ref(f'refs/heads/{branch_name}', ref.object.sha)
            return f"Branch '{branch_name}' aangemaakt"
        except Exception as e:
            return f"Fout bij aanmaken branch: {e}"
    
    def list_repositories(self):
        """Lijst alle repositories op"""
        try:
            repos = self.user.get_repos()
            repo_list = [repo.name for repo in repos]
            return f"Je repositories: {', '.join(repo_list)}"
        except Exception as e:
            return f"Fout bij ophalen repositories: {e}"
    
    def check_connection(self):
        """Check of GitHub beschikbaar is"""
        return self.github is not None
