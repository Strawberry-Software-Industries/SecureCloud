# SecureCloud
<b> Your new Cloud. Free and Open Source. 
By Strawberry Software </b>

## What is SecureCloud?
SecureCloud is a free and open source cloud that makes storing files on your (home) server more than easy!

## How does SecureCloud work? 
SecureCloud is currently a stable product, and includes some features. Some features will be added soon!
SecureCloud is available in English & German

## How can I install SecureCloud?
Via the Install Script, which can be found in [this](https://github.com/Strawberry-Software-Industries/Install-SecureCloud) Repository. 

## Important notes when you start SecureCloud for the first time
**<u>NOTE: This notes are deprecated. Starting with SecureCloud v1.0 you don't have to change anything in the source code.<u>**<br>
If you start SecureCloud for the first time, please note that you have to change the Local IP address to the IP address the device uses. 

```py
if __name__ == '__main__':
	application.run(host="localhost", port=80, threaded=True)    
```
<b>Change localhost to your IP address.
Under Windows you can find it with `ipconfig`, or under Linux with `ip a` or `ifconfig`. </b>
######
For example:
```py
if __name__ == '__main__':
	application.run(host="192.168.2.101", port=80, threaded=True)    
```
Now you can reach SecureCloud via your given IP address (for me `192.168.2.101`). In the beta phase you have to note that you have to put "/home" behind the IP address, otherwise you will get on a 404 page. (for example `192.168.2.101/home`) <br>
**<u>NOTE: This notes are deprecated. Starting with SecureCloud v1.0 you don't have to change anything in the source code.<u>**<br>

## Supported Platforms
SecureCloud works on Python 3.9 or higher. However, the Strawberry Software team recommends using the latest Python 3.10 version. All versions below Python 3.9 are untested and may not work.
Since some distributions use a version below Python 3.9, we have removed support for this distro. 
If you manage to get SecureCloud running on Debian 9, and Ubuntu 16.04 without much effort, feel free to send a pull request. 

| Version | Supported  |  Status|
|--|--|--| -- |
| Python 3.8 | - | Untested |
| Python 3.9 | Yes | Tested, working |
| Python 3.10 | Yes | Tested, working |
| Python 3.11 | - | Untested |

## Linux Support
| Platform | Version  |  Supported|  Branch |
|--|--|--| -- |
| Debian | 9 and below | No | OldOldstable |
| Debian | 10 | Yes | Oldstable | 
| Debian | 11 | Yes | Stable    | 
| Debian | 12 | Yes | Testing   | 
| Debian | Sid | Yes | Unstable | 
| Ubuntu | 16.04 | No | ESM     | 
| Ubuntu | 18.04 | Yes | Stable | 
| Ubuntu | 20.04 | Yes | LTS | 
| Ubuntu | 20.10 | Yes | End of Life | 
| Ubuntu | 21.04 | Yes | End of Life | 
| Ubuntu | 21.10 | Yes | Current | 
| Ubuntu | 22.04 | Yes | Future, LTS  |  
| Gentoo | - | Yes | Rolling Release |  
| Arch | - | Yes | Rolling Release   |  
| Manjaro | - | Yes | Rolling Release   |  


## Windows Support
| Platform | Version  |  Supported| 
|--|--|--| 
| Windows 7 | - | No |
| Windows 8 | - | No |
| Windows 8.1 | - | Yes |
| Windows 10 | Build 1909 and above | Yes| 
| Windows 11 | Build 22000.51 and above | Yes | 


## BSD Support
***BSD Support wasn't tested yet.***
| Platform | Version  |  Supported| 
|--|--|--|
| FreeBSD | Any | Yes| 
| OpenBSD | Any | Yes |

## Long-Term Support
We offer Long-Term Support (LTS) for consumers. The Current Version is v1.3.*
LTS support is free for all SecureCloud users. 

## The support of any SecureCloud version
The current non-LTS version of SecureCloud has support until a new non-LTS version of SecureCloud is released. From then on the version has only 7 days of support. 
**Example:**
Current LTS version: v1.3.*
Current Non-LTS version: v1.4
When version 1.5 is released, version 1.4 has only 7 days of support. After the 7 days the version is in EoL status (End of Life) and does not get any security updates. In addition, we do not provide further support for the version. (Via Discord or GitHub).
**For LTS versions:**
Each LTS version has support until a new LTS version comes out. From then on the version has only 7 days of support. 


## Version history
| Version | Status |  Release | End of Life| Notes
| --     | --      | --        | --        | -- 
| 0.2.2-Beta | EoL  	| 16.01.2022 | Yes      |First Beta Release
| 0.1-rc2 	 | EoL    	| 16.01.2022   | Yes    |        
| 0.6-rc3 	 | EoL    	| 16.01.2022   | Yes    |        
| 0.7-rc4 	 | EoL    	| 16.01.2022   | Yes    |        
| 0.8-r5 	 | EoL     	| 17.01.2022   | Yes    | Last RC & Beta
| 1.0 	 	 | EoL 		| 27.01.2022   | Yes 	| First Stable Release 
| 1.1 		 | LTS      | 29.01.2022   | Yes 	| First LTS 
| 1.1.1 	 | LTS      | 30.01.2022   | Yes     | 
| 1.2   	 | EoL 	| 31.01.2022   | Yes    | 
| 1.3   	 | LTS 		| 08.02.2022   | No     | LTS with more Features 
| 1.4   	 | Stable 	| 24.02.2022   | No     | Beta Login System
| 1.5   	 | Future  | 11.03.2022   | No     | 


## Does this also work on a Raspberry Pi?
Yes of course! SecureCloud is optimized for the Raspberry Pi, and has been tested on a Raspberry Pi by the Strawberry developers. (3 of our 7 developers have a Raspberry Pi. (4B 8GB, 4B 4GB, 2B)). Now you know why we have optimized SecureCloud so well 😉
<b>If the hostname of your RPi is `raspberrypi`, you can reach the Pi via the web address `raspberrypi.local/home` </b>

## System requirements

#### **Minimal requirements**
 - **RAM:** 128 MB or more
 - **CPU:** Any x86, or armv7l CPU with 1 Core and 800MHz clock speed
 - **Storage:** 1 GB
 - **Internet connection via wifi** 
 - **OS:** Debian 10 or higher | Ubuntu 18.04 or higher 
 
#### **Recommended requirements**
- **RAM:** 512 MB or more
- **CPU:** Any x86, x64, armv7l or aarch64 CPU with 2 Cores and 1,0GHz clock speed
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
SecureCloud was programmed in the Python programming language and the Flask framework was used. Material Design Lite ([getmdl.io](https://getmdl.io)) was used for the web design. All rights for the Material Design Icons belong to Google. 
