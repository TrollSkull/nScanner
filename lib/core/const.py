############### CONFIGURATION SECTION ###############

DEFLANG = 'en'

# APIKEY (your numverify.com api key) you can get a key for free on:
# https://apilayer.com/marketplace/number_verification-api
APIKEY = '6ccdce3a0f46148e6c093b06fd41ad7a'

############# DON'T TOUCH ANYTHING BELOW ############

TOOL_VERSION = open("./lib/core/version", "r").read()
BANNER = (r'''
        ____                          
  ___  / __/______ ____  ___  ___ ____
 / _ \_\ \/ __/ _ `/ _ \/ _ \/ -_) __/
/_//_/___/\__/\_,_/_//_/_//_/\__/_/   ''')

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    WHITE = '\033[0m'
    BLUE = '\033[34m'
    GRAY = '\033[1;30m'
