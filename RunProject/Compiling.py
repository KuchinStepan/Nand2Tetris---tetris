import subprocess, os
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "nand2tetris", "tools", "VMEmulator.bat")
subprocess.run(["python", "clearVM.py"])
subprocess.run(["python", "clear.py"])
subprocess.run(["cmd", "/c", "RunTetris.bat"], shell=True)
subprocess.run(["cmd", "/c", file_path], shell=True)