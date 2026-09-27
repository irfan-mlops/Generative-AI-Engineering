"""
02_pip_installation.py

Topic:
Installing Python packages using pip.

NOTE:
The pip commands are executed in the terminal.
"""

# ------------------------------------------------------------
# INSTALL A PACKAGE
# ------------------------------------------------------------

# Run this command in the terminal:
#
# pip install requests


# ------------------------------------------------------------
# IMPORT THE INSTALLED PACKAGE
# ------------------------------------------------------------

import requests


# ------------------------------------------------------------
# USE THE PACKAGE
# ------------------------------------------------------------

response = requests.get("https://httpbin.org/get")

print("Status code:", response.status_code)


# ------------------------------------------------------------
# USEFUL PIP COMMANDS
# ------------------------------------------------------------

"""
Install a package:
    pip install requests

Upgrade a package:
    pip install --upgrade requests

Show installed packages:
    pip list

Save dependencies:
    pip freeze > requirements.txt

Install dependencies:
    pip install -r requirements.txt

Uninstall a package:
    pip uninstall requests
"""