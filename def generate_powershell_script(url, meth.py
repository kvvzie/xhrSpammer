def generate_powershell_script(ps_request, url):
    # Skrypt początkowy
    script = """
# Definicja funkcji do wysyłania XHR requestów
function Send-XHRRequest {{
    param (
        [string]$url
    )

    # Tworzenie obiektu żądania
    $xhr = New-Object System.Net.WebClient

    # Wysyłanie żądania i zapisanie odpowiedzi
    $response = $xhr.DownloadString($url)

    # Zwrócenie odpowiedzi
    return $response
}}

# Pobranie URL od użytkownika
$url = "{}"

# Główna pętla programu
while ($true) {{
    # Wywołanie funkcji do wysłania XHR requestu z podanym przez użytkownika URL
    $response = Send-XHRRequest -url $url

    # Wypisanie odpowiedzi na konsolę (można pominąć)
    Write-Output $response

    # Pauza na 3 sekund przed kolejnym wysłaniem żądania
    Start-Sleep -Seconds 3
}}
""".format(url)

    # Dodanie polecenia PowerShell podanego przez użytkownika do funkcji Send-XHRRequest
    script = script.replace("# Tworzenie obiektu żądania", ps_request + "\n    # Tworzenie obiektu żądania")

    return script

def main():
    
    # Retrieving the URL from the user
    url = input("Provide a target URL for requests: ")
    
    ps_request = ''' 

    '''

    # Generating an updated PowerShell script
    updated_script = generate_powershell_script(ps_request, url)

    # create a file with updated PowerShell script
    with open("updated_script.ps1", "w") as file:
        file.write(updated_script)

    print("The updated PowerShell script has been saved to a file: updated_script.ps1")

if __name__ == "__main__":
    main()
