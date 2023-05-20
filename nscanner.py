#!/usr/bin/env python3

__author__ = 'TrollSkull'
__version__= 'v1.0'

try:
    import phonenumbers
    import requests

except ImportError:
    import os
    requirements = ['phonenumbers', 'requests']

    for requirement in requirements:
        os.system(f'pip3 install {requirement}')

try:
    from lib.main import main
    from lib.core.exceptions import MyExceptions

except ImportError as err:
    import sys

    print(err, file=sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    main()