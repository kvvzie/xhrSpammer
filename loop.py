import subprocess
import time

# script path
script_path = "updated_script.ps1"

# new powershell comand
powershell_command = f"Start-Process powershell.exe -ArgumentList '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', '{script_path}'"

num_windows = int(input("Enter the number of PowerShell windows to open: "))

powershell_processes = []

# # of processes
for _ in range(num_windows):
    powershell_process = subprocess.Popen(["powershell", "-Command", powershell_command], shell=True)
    powershell_processes.append(powershell_process)
    
response = input("any input will force the program to close")
    
for process in powershell_processes:
    process.wait()
