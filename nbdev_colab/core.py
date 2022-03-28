# AUTOGENERATED! DO NOT EDIT! File to edit: nbs/00_core.ipynb (unless otherwise specified).

__all__ = ['setup_drive', 'setup_git', 'git_push']

# Cell
import os
from google.colab import drive

# Cell
def setup_drive():
  "Connect Google Drive to use GitHub"
  drive.mount('/content/drive', force_remount=True)
  os._exit(00)

# Cell
from pathlib import Path
import os, subprocess

# Cell
def setup_git(path:Path, project_name:str, username:str, password:str, email:str):
  "Link your mounted drive to GitHub. Remove sensitive information before pushing"
  start = os.getcwd()
  os.chdir(path)
  commands = []
  commands.append(f"git config --global user.email {email}")
  commands.append(f"git config --global user.name {username}")
  commands.append("git init")
  commands.append("git remote rm origin")
  commands.append(f"git remote add origin https://{username}:{password}@github.com/{username}/{project_name}.git")
  commands.append("git pull origin master --allow-unrelated-histories")
  for cmd in commands:
    process = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
    output, err = process.communicate()
  os.chdir(start)

# Cell
from nbdev.export import *

# Cell
def git_push(path:Path, message:str):
  "Convert the notebooks to scripts and then push to the library"
  start = os.getcwd()
  os.chdir(path)
  commands = []
  commands.append('nbdev_install_git_hooks')
  commands.append('nbdev_build_lib')
  commands.append('git add *')
  commands.append(f'git commit -m "{message}"')
  commands.append('git push origin master')
  for cmd in commands:
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output, err = process.communicate()
  os.chdir(start)