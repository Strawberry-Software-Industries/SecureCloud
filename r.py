import requests

def get_installed_version():
    with open("current_version.txt", "r") as version:
        return version.read()


def get_online_version():
    api = requests.get("https://api.strawberrysoftware.ga/api/v1/securecloud/version/?edition=home")
    return api.text

installed_ver = get_installed_version()
online_ver = get_online_version()

if installed_ver == online_ver:
    print("You are running the latest version!")
else:
    print("You are not running the latest version!")