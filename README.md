<div align="center">
	<img src="/.github/assets/logo.png" width="400" height="200"/>

  [![Version](https://img.shields.io/badge/Version-1.1-green)]()
  [![Bash](https://img.shields.io/badge/Made%20with-Python-blue)]()
  [![License](https://img.shields.io/badge/License-GPL%203.0-yellow)]()
</div>

# 📱 nScanner: OSINT-based phone number information tool.
**nScanner** is a command-line OSINT tool designed to retrieve public information about a phone number using open-source libraries and third-party APIs such as **[Numverify](https://numverify.com/)**.

It allows you to quickly validate numbers and gather metadata like country, carrier, and line type in a simple and lightweight way.

## ⚙️ Installation
You can download nScanner on any platform by cloning the official Git repository:

```bash
$ git clone https://github.com/TrollSkull/nScanner

$ cd nScanner

$ pip install -r requirements.txt
    
$ python nscanner.py
```

> [!IMPORTANT]
> You need a numverify API KEY to get more data, you can get a key for free on: [apilayer.com/marketplace](https://apilayer.com/marketplace/number_verification-api)
>
> Once you get a key you need to put it in the APIKEY variable in `./lib/core/const.py` file and then run nscanner.py
>
> Also you can change the language of the requested information in `./lib/core/const.py` modifying the DEFLANG variable, see the supported languages [here](https://pypi.org/project/phonenumbers/).

## 🔍 Usage

To get a list of all options and switches use the `--help` command.
```
Usage: nscanner.py -n <your number here> [options] or -u for update

     -h, --help         show this help message and exit
     --number NUMBER, -n NUMBER
                        enter a number to start a scan
     --update UPDATE, -u
                        update the script
  
Report bugs to (trollskull.contact@gmail.com)
```
  
## 📃 License and Disclaimer
> [!WARNING]
> This project is intended for educational and legitimate OSINT purposes only. Always ensure compliance with local laws and regulations when performing data lookups.

This project is licensed under the GNU General Public License v3.0 © SwiftTube. For more details, please refer to the full license **[here](https://github.com/TrollSkull/nScanner/blob/main/LICENSE)**.
