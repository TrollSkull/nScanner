import requests, urllib.request, sys
from lib.core.const import Colors, TOOL_VERSION
from lib.core.checkwifi import checkwifi
from lib.core.exceptions import MyExceptions

url = "https://raw.githubusercontent.com/TrollSkull/nScanner/master/"

def update():
    files = ['nscanner.py', 'lib/core/checkwifi.py', 'lib/core/updater.py', 'lib/core/version',
             'lib/core/const.py', 'lib/main.py', 'lib/core/exceptions.py']
    
    for file in files:
        data = urllib.request.urlopen(url + file).read()
        
        with open(file, "wb") as f:
            f.write(data)
    
    sys.exit(Colors.OK + "\n[nScanner]" + Colors.WHITE + " Updated successfull, exiting script.")

def checkversion():
    try:
        checkwifi(host = 'google.com', port = 80)
        git_version = requests.get("https://raw.githubusercontent.com/TrollSkull/nScanner/main/lib/core/version").text  
    
    except Exception as err:
        raise MyExceptions
    
    print(Colors.BLUE + "\n[nScanner]" + Colors.WHITE +" Verifying Git version...")

    if (TOOL_VERSION == git_version):
        print(Colors.YELLOW + "\n[nScanner]" + Colors.WHITE + " Version match with GitHub repository.")
        
    else:
        print(Colors.BLUE + "\n[nScanner]" + Colors.WHITE + " Update available, downloading " + Colors.BLUE + "(" + Colors.OK + git_version + Colors.BLUE + ")...")
        update()