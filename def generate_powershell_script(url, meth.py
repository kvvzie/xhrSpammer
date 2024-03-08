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
$session = New-Object Microsoft.PowerShell.Commands.WebRequestSession
$session.UserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
$session.Cookies.Add((New-Object System.Net.Cookie("MoodleSession", "8f118307faf1fdf59b58215691de5a59", "/", "enaw.smarthost.pl")))
Invoke-WebRequest -UseBasicParsing -Uri "https://enaw.smarthost.pl/lib/ajax/service.php?sesskey=TKzchtE7jp&info=core_message_send_messages_to_conversation" `
-Method "POST" `
-WebSession $session `
-Headers @{
"Accept"="application/json, text/javascript, */*; q=0.01"
  "Accept-Encoding"="gzip, deflate, br"
  "Accept-Language"="pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7"
  "Origin"="https://enaw.smarthost.pl"
  "Referer"="https://enaw.smarthost.pl/user/profile.php?id=439"
  "Sec-Fetch-Dest"="empty"
  "Sec-Fetch-Mode"="cors"
  "Sec-Fetch-Site"="same-origin"
  "X-Requested-With"="XMLHttpRequest"
  "sec-ch-ua"="`"Not A(Brand`";v=`"99`", `"Opera GX`";v=`"107`", `"Chromium`";v=`"121`""
  "sec-ch-ua-mobile"="?0"
  "sec-ch-ua-platform"="`"Windows`""
} `
-ContentType "application/json" `
-Body "[{`"index`":0,`"methodname`":`"core_message_send_messages_to_conversation`",`"args`":{`"conversationid`":960,`"messages`":[{`"text`":`":steamhappy:`"}]}}]"
    '''

    # Generating an updated PowerShell script
    updated_script = generate_powershell_script(ps_request, url)

    # create a file with updated PowerShell script
    with open("updated_script.ps1", "w") as file:
        file.write(updated_script)

    print("The updated PowerShell script has been saved to a file: updated_script.ps1")

if __name__ == "__main__":
    main()
