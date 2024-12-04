# MAC Address Randomizer

MAC Address Randomizer is a lightweight Python script for Linux users, allowing you to easily change the MAC address of any network interface. Compatible with popular Linux distributions like Kali Linux, Ubuntu, Debian, CentOS, Linux Mint, and more, this tool generates a random MAC address to enhance privacy and security. Ideal for network administrators and privacy-conscious users, it works seamlessly with the iproute2 toolset to modify your device's MAC address in just a few commands.


## Supported OS
- GNU/Linux
- Kali Linux
- Ubuntu
- CentOS
- Linux Mint
- Debian
- Red Hat Enterprise Linux (RHEL): 

## Prerequisites
- [Python3](https://www.python.org/downloads/)



## Installation
**1. Clone this repo:**
```
git clone https://github.com/edatastyle/mac-address-randomizer.git
```

**2. Move into the project directory:**
```
cd mac-address-randomizer
```

**3. Run the installation script with:**
```
sudo ./installer.sh
```

**3. After the installation, you should be able to run the MAC address changer using:**
```
change_mac -i wlan0
```

## Available options:
```
-h, --help              Show this help message and exit
-i, --interface         Interface name
```

## Contributing
Pull requests can be submitted [here](https://github.com/edatastyle/mac-address-randomizer/pulls). Any contribution to the project will be highly appreciated.
