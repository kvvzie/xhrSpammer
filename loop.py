import subprocess
import time

# Ścieżka do pliku skryptu PowerShell
script_path = "updated_script.ps1"

# Komenda PowerShell do uruchomienia skryptu w nowym oknie
powershell_command = f"Start-Process powershell.exe -ArgumentList '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', '{script_path}'"

# Liczba iteracji, które chcesz wykonać (25 ms * 400 = 10 s)
iterations = 400

# Pętla uruchamiająca skrypt co 25 ms przez 10 sekund
for _ in range(iterations):
    subprocess.run(["powershell", "-Command", powershell_command], shell=True)
    time.sleep(0.025)  # Czekaj 25 ms

# Możesz dodać kod, który zaczeka na zakończenie działania PowerShell
# i zwróci kontrolę użytkownikowi.