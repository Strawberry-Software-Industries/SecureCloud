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
If you manage to get SecureCloud running on Debian 9, and Ubuntu 16.04, 20.10 without much effort, feel free to send a pull request. 

## Linux Support
| Platform | Version  |  Supported|  Branch |
|--|--|--| -- |
| Debian | 9 and below | No | OldOldstable |
| Debian | 10 | Yes | Oldstable | 
| Debian | 11 | Yes | Stable | 
| Debian | 12 | Yes | Testing | 
| Debian | Sid | Yes | Unstable | 
| Ubuntu | 16.04 | No | ESM | 
| Ubuntu| 18.04 | Yes | Stable | 
| Ubuntu| 20.04 | Yes | Stable | 
| Ubuntu| 20.10 | No | End of Life | 
| Ubuntu| 21.04 | No | End of Life | 
| Ubuntu| 21.10 | Yes | Current | 
| Ubuntu| 22.04 | Yes | Future |  

## Windows Support
| Platform | Version  |  Supported| 
|--|--|--| 
| Windows | 10 Build 2004 and above | Yes| 
| Windows 11| Any | Yes | 
| Windows 7 | Any | No |

## BSD Support
| Platform | Version  |  Supported| 
|--|--|--|
| Windows | 10 Build 2004 and above | Yes| 
| Windows 11| Any | Yes | 
| Windows 7 | Any | No |




## Does this also work on a Raspberry Pi?
Yes of course! SecureCloud is optimized for the Raspberry Pi, and has been tested on a Raspberry Pi by the Strawberry developers. 
<b>If the hostname of your RPi is `raspberrypi`, you can reach the Pi via the web address `raspberrypi.local/home` </b>

## System requirements

#### **Minimal requirements**
 - **RAM:** 256 MB or more
 - **CPU:** Any x86, or armv7l CPU with 1 Core and 900MHz clock speed
 - **Storage:** 1 GB
 - **Internet connection via wifi** 
 - **OS:** Debian 10 or higher | Ubuntu 16.04 or higher 
 
#### **Recommended requirements**
- **RAM:** 1 GB or more
- **CPU:** Any x86, x64, armv7l or aarch64 CPU with 2 Cores and 1,3GHz clock speed
- **Storage:** 5 GB
- **Internet connection via LAN** 
- **OS:** Debian 11 or higher | Ubuntu 20.04 or higher 

## Performance on a Raspberry Pi
**Raspberry Pi 4 Modell B [2, 4, 8 GB]:** Very good performance. Recommended for Home Server with SecureCloud or other Cloud Software. <br>
**Raspberry Pi 3 Modell A+:** Good performance, but a bit slower than the RPi 4 because of the RAM. I recommend it only if you want something very cheap. <br>
**Raspberry Pi 3 Modell B+:** Good performance, but I recommend the RPi 4 with 2 GB RAM  <br>
**Raspberry Pi Zero W:** Performance is a bit poor, there can be internet lags or CPU lags from time to time.  <br>
**Raspberry Pi Zero 2 W:** Good performance for a mini Home Server! <br>

## Information about the program code
SecureCloud was programmed in the Python programming language and the Flask framework was used. Material Design Lite ([getmdl.io](https://getmdl.io)) was used for the web design. All rights for the icons & some images belong to Google. 
