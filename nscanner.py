#!/usr/bin/env python3

try:
    import phonenumbers
    import requests
    
except ImportError as err:
    print("Missing dependencies. Please run 'pip install -r requirements.txt' first.")
    sys.exit(1)

try:
    from lib.main import main

except ImportError as err:
    import sys

    print(err, file = sys.stderr)
    sys.exit(1)

if __name__ == '__main__':
    main()
