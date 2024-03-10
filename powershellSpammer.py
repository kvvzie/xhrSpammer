# made by kvvzie
def generate_powershell_script(ps_request, url):
    # main script
    script = """
# made by kvvzie
# some function
function Send-XHRRequest {{
    param (
        [string]$url
    )

    # creating some shit
    $xhr = New-Object System.Net.WebClient

    # sending some sht
    $response = $xhr.DownloadString($url)

    # returnin response
    return $response
}}

# gettin url
$url = "{}"

# main loop
while ($true) {{
    # sendin xhr request
    $response = Send-XHRRequest -url $url

    # printinm response
    Write-Output $response

    # pause for 250 milisec
    Start-Sleep -Milliseconds 250
}}
""".format(url)

    # some random shit
    script = script.replace("# creating some shit", ps_request + "\n    # creating some shit")

    return script

def main():
    
    # reading powershell request from input.ps1 file
    with open("input.ps1", "r") as file:
        ps_request = file.read()
    
    
    # retrieving the URL from the user
    url = input("Provide a target URL for requests: ")
    

    # generating an updated PowerShell script
    updated_script = generate_powershell_script(ps_request, url)

    # create a file with updated PowerShell script
    with open("updated_script.ps1", "w") as file:
        file.write(updated_script)

    print("The updated PowerShell script has been saved to a file: updated_script.ps1")

if __name__ == "__main__":
    main()
