# nScanner
<p align="left">
<img src="/.assets/logo.png" width="400" height="200"/>

[![Version](https://img.shields.io/badge/Version-1.0-green)]()
[![Bash](https://img.shields.io/badge/Made%20with-Python-blue)]()
[![License](https://img.shields.io/badge/License-GPL%203.0-yellow)]()

nScanner is a tool to find data about a phone number using OSINT sources, libraries and APIs like **[Numverify](https://numverify.com/)**, coded by **[TrollSkull](https://github.com/TrollSkull)** (**[@ImTrollSkull](https://twitter.com/ImTrollSkull)**)
  
You need a numverify API KEY to get more data, you can get a key for free on: [apilayer.com/marketplace](https://apilayer.com/marketplace/number_verification-api)

Numverify provides 100 request per month for free, so don't worry about the usage of this API :^)
  
Once you get a key you need to put it in the APIKEY variable in `./lib/core/const.py` file and then run nscanner.py
  
Also you can change the language of the requested information in `./lib/core/const.py` modifying the DEFLANG variable, see the supported languages [here](https://pypi.org/project/phonenumbers/).

## INSTALLATION
### One line installation.
Just copy this line and paste in the terminal.
```bash
apt install -y git python; git clone https://github.com/TrollSkull/nScanner; cd nScanner; python nscanner.py
```

You can download nScanner on any platform by cloning the official Git repository:

```bash
$ pkg install -y git python

$ git clone https://github.com/TrollSkull/nScanner

$ cd nScanner
    
$ python nscanner.py
```

## USAGE

To get a list of all options and switches use the `--help` command.
```
Usage: nscanner.py -n <your number here> [options] or -u for update

     -h, --help         show this help message and exit
     --number NUMBER, -n NUMBER
                        enter a number to start a scan
     --update UPDATE, -u
                        update the script
  
Report bugs to (t.me/TrollSkull)
```
  
### LICENCE

**[GPL-3.0 License © nScanner](https://github.com/TrollSkull/nScanner/blob/main/LICENSE)**
