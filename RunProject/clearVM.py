import run
from pathlib import Path

directory = run.get_path()

files = Path(directory).glob('*.vm')

for file in files:
    file.unlink()