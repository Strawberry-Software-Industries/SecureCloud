# SecureCloud
[![SecureCloud - v1.9](https://img.shields.io/badge/SecureCloud-v1.9-2ea44f)](https://github.com/Strawberry-Software-Industries/SecureCloud/blob/main/current_version.txt) [![SecureCloud - v1.5.2 LTS](https://img.shields.io/badge/SecureCloud-v1.5.2_LTS-2ea44f)](https://github.com/Strawberry-Software-Industries/SecureCloud/blob/main/current_version_lts.txt)
[![CodeQL](https://github.com/Strawberry-Software-Industries/SecureCloud/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/Strawberry-Software-Industries/SecureCloud/actions/workflows/codeql-analysis.yml) [![Stale](https://github.com/Strawberry-Software-Industries/SecureCloud/actions/workflows/stale.yml/badge.svg)](https://github.com/Strawberry-Software-Industries/SecureCloud/actions/workflows/stale.yml) [![Python application](https://github.com/Strawberry-Software-Industries/SecureCloud/actions/workflows/python-app.yml/badge.svg)](https://github.com/Strawberry-Software-Industries/SecureCloud/actions/workflows/python-app.yml) <br> <br>
<b> Your new Cloud. Free and Open Source. 
By Strawberry Software </b>

## What is SecureCloud?
SecureCloud is a free and open source cloud that makes storing files on your (home) server more than easy!

| ℹ️ Information
| -------------
| We are looking for developers! To appy, simply join our Discord server and DM a staff member!

Try out free Demo at [demo-securecloud.loca.lt](https://demo-securecloud.loca.lt/) <br>
**Username:** `admin` <br>
**Password:** `python`


## How does SecureCloud work? 
SecureCloud is currently a stable product, and includes some features. Some features will be added soon!
SecureCloud is available in English & German

## How can I install SecureCloud?
Via the Install Script, which can be found in [this](https://github.com/Strawberry-Software-Industries/Install-SecureCloud) Repository. 
Otherwise clone this repository (unstable), or download the latest release (stable).

## Version history

You can look at the history in [VERSION.md](https://github.com/Strawberry-Software-Industries/SecureCloud/blob/main/VERSION.md)	

## Supported Platforms
SecureCloud works on Python 3.9 or higher. However, the Strawberry Software team recommends using the latest Python 3.10 version. All versions below Python 3.9 are untested and may not work.
Since some distributions use a version below Python 3.9, we have removed support for this distro. 
If you manage to get SecureCloud running on Debian 9, and Ubuntu 16.04 without much effort, feel free to send a pull request. 

| Version | Supported  |  Status|
|--|--|--| 
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

| ⚠️ Warning
| -------------
| The BSD support hasn't been tested yet!

| Platform | Version | Supported |
| -------- | ------- | --------- |
| FreeBSD  | v13+    | ❓        |

## Long-Term Support
We offer Long-Term Support (LTS) for consumers. The Current Version is v1.5.*
LTS support is free for all SecureCloud users. 

## The support of any SecureCloud version

| ⚠️ Warning
| -------------
| The current LTS concept will change with version 2.0 (Vanilla Cake)

The current non-LTS version of SecureCloud has support until a new version of SecureCloud is released (Any, even LTS). From then on the version has only 7 days of support. 
**Example:**
Current LTS version: v1.5.*
Current Non-LTS version: v1.6 (GIT-Build)
When version 1.7 is released, version 1.6 has only 7 days of support. After the 7 days the version is in EoL status (End of Life) and does not get any security updates. In addition, we do not provide further support for the version. (Via Discord or GitHub).
**For LTS versions:**
Each LTS version has support until a new LTS version comes out. From then on the version has only 7 days of support. 

	
## Does this also work on a Raspberry Pi?
Yes of course! SecureCloud is optimized for the Raspberry Pi, and has been tested on a Raspberry Pi by the Strawberry developers. (5 of our 8 developers have a Raspberry Pi). Now you know why we have optimized SecureCloud so well 😉
<b>If the hostname of your RPi is `raspberrypi`, you can reach the Pi via the web address `raspberrypi.local`. If you have a Fritz Box, it could be that the URL is `raspberry.fritz.box`. Just try it!</b>

## System requirements

#### **Minimal requirements**
 - **RAM:** 256 MB or more
 - **CPU:** Any x86 or armv7l CPU with 1 Core and 800MHz clock speed
 - **Storage:** 3,5 GB (Including Python SDK, etc..)
 - **Internet connection via wifi** 
 - **OS:** Debian 10 or higher | Ubuntu 18.04 or higher 
 
#### **Recommended requirements**
- **RAM:** 512 MB or more
- **CPU:** Any x64 or aarch64 CPU with 2 Cores and 1,0GHz clock speed
- **Storage:** 8 GB (Including Python SDK, etc..)
- **Internet connection via LAN** 
- **OS:** Debian 11 or higher | Ubuntu 20.04 LTS or higher 

## Performance on a Raspberry Pi
**Raspberry Pi 4 Model B:** Very good performance. Recommended for Home Server with SecureCloud or other Cloud Software. <br>
**Raspberry Pi 3 Model A+:** Good performance, but a bit slower than the RPi 4 because of the RAM. I recommend it only if you want something very cheap. <br>
**Raspberry Pi 3 Model B+:** Good performance, but I recommend the RPi 4 with 2 GB RAM  <br>
**Raspberry Pi Zero W:** Performance is a bit poor, there can be internet lags or CPU lags from time to time.  <br>
**Raspberry Pi Zero 2 W:** Good performance for a mini Home Server! <br>

## GitHub
| ℹ️ Information
| -------------
| CodeQL and pytest are running every 12h on 00:00 (12AM) UTC and on 12:00 (12PM) UTC.

## Information about the program code
SecureCloud was programmed in the Python programming language. We're using Flask for the Web Server. Material Design Lite ([getmdl.io](https://getmdl.io)) was used for the web design. 
