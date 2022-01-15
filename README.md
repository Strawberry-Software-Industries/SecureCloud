
# SecureCloud
<b> Your new Cloud. Free and Open Source.

## What is SecureCloud?
SecureCloud is a free and open source cloud that makes storing files on your (home) server more than easy!

## How does SecureCloud work? 
SecureCloud is currently in the early beta phase, so many features are not yet available. 
SecureCloud will be available in English & German.

## How can I install SecureCloud?
Via the Install Script, which can be found in [this](https://github.com/Strawberry-Software-Industries/Install-SecureCloud) Repository. 

## Important notes when you start SecureCloud for the first time
If you start SecureCloud for the first time, please note that you have to change the Local IP address to the IP address the device uses. 

    if __name__ == '__main__':
    application.run(host="localhost", port=80, threaded=True)    

<b>Change localhost to your IP address.
Under Windows you can find it with `ipconfig`, or under Linux with `ip a` or `ifconfig`. </b>
######
For example:

    if __name__ == '__main__':
    application.run(host="192.168.2.101", port=80, threaded=True)    

Now you can reach SecureCloud via your given IP address (for me `192.168.2.101`). In the beta phase you have to note that you have to put "/home" behind the IP address, otherwise you will get on a 404 page. (for example `192.168.2.101/home`

## Supported Platforms
For SecureCloud to run well, you always need the latest version of python3.
Therefore only the LTS distributions and the latest distribution of Ubuntu are supported, and only Debian Stable (Debian 11) & Oldstable (Debian 10) are supported. 
If you manage to get SecureCloud running on Debian 9, and Ubuntu 16.04, 20.10, 21.04 without much effort, feel free to send a pull request. 

| Platform | Version  |  Supported|
|--|--|--|
| Debian | 9 and below| No|
| Debian | 10| Yes |
| Debian | 11| Yes |
| Ubuntu| 16.04 LTS| No |
| Ubuntu| 18.04 LTS | Yes |
| Ubuntu| 20.04 LTS | Yes |
| Ubuntu| 21.10 | Yes |
 
