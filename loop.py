import subprocess
import time

# script path
script_path = "updated_script.ps1"

# new powershell comand
powershell_command = f"Start-Process powershell.exe -ArgumentList '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', '{script_path}'"

# iterations (25 ms * 400 = 10 s)
iterations = 400

# loop
for _ in range(iterations):
    subprocess.run(["powershell", "-Command", powershell_command], shell=True)
    time.sleep(0.025)  # Czekaj 25 ms
