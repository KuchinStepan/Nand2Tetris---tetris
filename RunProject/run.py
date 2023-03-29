import shutil
from pathlib import Path

start_path = Path(__file__).resolve().parent.parent
dest_path = start_path / "vm"

def get_path():
    return dest_path


dest_path.mkdir(exist_ok=True)
for file_path in start_path.rglob("*.jack"):
    if (dest_path / file_path.name).exists():continue
    shutil.copy(file_path, dest_path)
