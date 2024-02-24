import sys
from pathlib import Path

ROOT_DIR = Path.cwd().parent
APP_DIR = ROOT_DIR / 'app'
sys.path.append(str(APP_DIR))