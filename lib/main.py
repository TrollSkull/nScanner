from lib.core.checkwifi import checkwifi
from lib.core.exceptions import MyExceptions
from lib.core.updater import checkversion

from lib.core.const import (
    TOOL_VERSION,
    DEFLANG,
    APIKEY,
    BANNER,
    Colors
)

import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone

import requests
import argparse
import time
import json
import sys

try:
    if sys.argv[1] == '--update' or sys.argv[1] == '-u':
        checkversion()
except IndexError:
    pass

parser = argparse.ArgumentParser(description='nScanner by TrollSkull',
                                 usage="nscanner.py -n <your number here> [options] or -u for update")

parser.add_argument('--number', '-n', type=str, required=False,
                    help='enter a number to start a scan.')

args = parser.parse_args()

def numverifyscan(number, apikey):
    get = requests.get('https://api.apilayer.com/number_verification/validate',
                       params={'number': number}, headers={'apikey': apikey}).text

    try:
        jsonload = json.loads(get)

    except json.decoder.JSONDecodeError:
        sys.exit(Colors.RED + '\n[nScanner] ' + Colors.WHITE + 'An un expected error ocurred, try again.')

    print(f'{Colors.YELLOW}International Format: {Colors.WHITE}{jsonload["international_format"]}')
    print(f'{Colors.YELLOW}Line Type: {Colors.WHITE}{jsonload["line_type"]}')
    print(f'{Colors.YELLOW}Country Code: {Colors.WHITE}{jsonload["country_code"]}')
    print(f'{Colors.YELLOW}Country Prefix: {Colors.WHITE}{jsonload["country_prefix"]}')
    print(f'{Colors.YELLOW}Local Format: {Colors.WHITE}{jsonload["local_format"]}')

def scannumber(InputNumber):
    if "+" not in InputNumber:
        sys.exit(f'{Colors.RED}\n[nScanner] {Colors.WHITE}The country prefix has not been entered. (ex: +598)')

    try:
        NumberObject = phonenumbers.parse(InputNumber)

        if phonenumbers.is_possible_number(NumberObject):
            print(f'{Colors.GREEN}\n[nScanner] {Colors.WHITE}The number is valid and possible. \n')
            time.sleep(2)
        else:
            print(f'{Colors.RED}\n[nScanner] The number is valid but might not be possible.{Colors.WHITE} \n')

    except Exception as error:
        sys.exit(str(error))

    strip = str(timezone.time_zones_for_number(NumberObject)).replace("('", '')
    time_zone = strip.replace("',)", '')

    location = geocoder.description_for_number(NumberObject, DEFLANG)
    carriers = carrier.name_for_number(NumberObject, DEFLANG)

    print(f'{Colors.YELLOW}Time Zone: {Colors.WHITE}{time_zone}')
    print(f'{Colors.YELLOW}Location: {Colors.WHITE}{location}')
    print(f'{Colors.YELLOW}Carrier: {Colors.WHITE}{carriers}')

def main():
    checkwifi(host = 'google.com', port = 80)
    print(Colors.YELLOW + BANNER + Colors.WHITE + f'{TOOL_VERSION}\n')

    if APIKEY == 'APIKEY':
        print(Colors.RED + '\n[nScanner] ' + Colors.WHITE + 'You need an APIKEY to start using nScanner.\n')
        print(Colors.YELLOW + '[nScanner] ' + Colors.WHITE + "If you don't have a key you can get one for free at ")
        print(Colors.GRAY + '"https://apilayer.com/marketplace/number_verification-api"' + Colors.WHITE)
        sys.exit('and put your key in APIKEY variable in ./lib/core/const.py file.\n')

    try:
        if not args.number:
            number = input(Colors.YELLOW + '[nScanner] ' + Colors.WHITE + 'Enter your number: ')
        else:
            number = str(args.number)

    except KeyboardInterrupt:
        sys.exit(Colors.YELLOW + '\n[nScanner] ' + Colors.WHITE + 'Keyboard interrupt detected, exiting.')

    scannumber(InputNumber = number)

    print(Colors.BLUE + '\n[nScanner] ' + Colors.WHITE +'Using ' + Colors.GRAY + '"numverify.com"' + Colors.WHITE + ' api to fetch more data...\n')

    apinum = number.replace('+', '')
    numverifyscan(number = int(apinum), apikey = APIKEY)

    print(Colors.GREEN + '\n[nScanner] ' + Colors.WHITE + 'Done!')

if __name__ == '__main__':
    main()