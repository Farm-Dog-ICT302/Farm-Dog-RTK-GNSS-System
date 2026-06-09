# Farm-Dog-RTK-GNSS
The system consists of two components:

• A Base Station that receives GNSS satellite data and generates RTK correction data.

• A Rover that receives these RTK corrections and combines them with its own GNSS measurements to achieve centimetre-level positioning accuracy.

## Features

- RTK GNSS positioning using the u-blox ZED-F9P
- Web-based interface built with Flask
- Live coordinate display
- Find Mode navigation to target coordinates
- CSV coordinate logging
- NTRIP correction support
- Sub-2.5 cm positioning accuracy (under ideal conditions)

## Hardware Required

### Base Station
    - Raspberry Pi 4B 4GB
    - u-blox ZED-F9P GNSS module
    - GNSS antenna
    - Tripod Height - 2 metres (used for field testing)
    - ABS IP66 enclosure
    - Power bank or fixed power supply

<img src="https://raw.githubusercontent.com/Farm-Dog-ICT302/Farm-Dog-RTK-GNSS-System/main/images/hardware_images/BaseStation.jpeg" width="60%" alt="BaseStation Image">


### Rover
    - Raspberry Pi 4B 4GB
    - u-blox ZED-F9P GNSS module
    - GNSS antenna (mounted on 2m pole)
    - Tripod Height - 2 metres
    - ABS IP66 enclosure
    - Power bank
    
<img src="https://raw.githubusercontent.com/Farm-Dog-ICT302/Farm-Dog-RTK-GNSS-System/main/images/hardware_images/Rover2.jpeg" width="60%" alt="Rover Image">


### Network
    - GL-MT3000 portable Wi-Fi router
      <- Connects base and rover wirelessly
      <- NTRIP corrections on port 2101

### Software - Base Station
    - RTKBase v2.7.0
    - Raspberry Pi OS

### Software - Rover
    - Raspberry Pi OS
    - PyGPSClient (Graphical Diagnostics)
    - FarmDog-App
        ├── FarmDog.py (Primary surverying and positioning application)
        ├── install.sh (First time install script)
        ├── requirements.txt
        ├── startserver.sh (Script to manually FarmDog program)
        ├── output (Folder for exported CSV will be stored here)
        ├── static
        ├── js 
        ├── templates


## FarmDog Interface

#### Menu
<img src="https://raw.githubusercontent.com/Farm-Dog-ICT302/Farm-Dog-RTK-GNSS-System/main/images/screenshots/Screenshot Menu.png" width="70%" alt="Main Menu">

#### Map Mode
<img src="https://raw.githubusercontent.com/Farm-Dog-ICT302/Farm-Dog-RTK-GNSS-System/main/images/screenshots/Screenshot MapMode.png" width="70%" alt="Map Mode">

#### Find Mode
<img src="https://raw.githubusercontent.com/Farm-Dog-ICT302/Farm-Dog-RTK-GNSS-System/main/images/screenshots/Screenshot FindMode.png" width="70%" alt="Find Mode">

# Installation & Setup
This repository contains both the GNSS data processing backend and the Web GUI interface. 

### Prerequisites
* Base Station Raspberry Pi running ***RTKBase*** [RTKBase setup guide](https://github.com/Stefal/rtkbase) for installation.
* Python 3.10+ installed.

## How to Install and Run the FarmDog App

If you only want to deploy the Python processing engine to your rover hardware, follow these steps to download and setup FarmDog Python program and Web GUI:


##### 1. Install the FarmDog-App
```
git clone https://github.com/Farm-Dog-ICT302/FarmDog-App.git
```

##### 2. Navigate into the application directory
```
cd FarmDog-App
```

##### 3. Run the installation script (installs Flask and other dependencies)
```
chmod +x install.sh
./install.sh
```

##### 4. Start the Flask Web GUI and Python backend
```
./startserver.sh
```

##### 5. Navigate to Web Browser on any device on the same network
```
http://[IP ADDRESS]:5000
```

## Program Versions

### farmdog.py (v1.0) - Initial Release Prototype
    - this program connects directly to the ZED-F9P serial port.
    - proven working with real RTK Fixed data base on equation provided.

### farmdog.py (v2.0) - WEB UI with Flask Server
    - OOP rewrite with clean class separation (GPS source, RTK client, web server, CSV writer)
    - Flask web interface running on port 5000, accessible from any device on the same network.
    - Two modes: Map Mode (live position display) and Find Mode (navigate to target coordinates)
    - Geodesic distance and azimuth via 'geographiclib' (WGS84 ellipsoid)
    - Mock GPS source for offline development when hardware is unavailable


## Team FarmDog - ICT302 Team IT01 (Semester 1 - 2026)

**Supervisor:** David MURRAY

**Client:** Terry KOZINIEC

***Students*** 
Clark Carpentero, 
Tim Fausten,
Vo Thu,
Flynn McAlpine-Monkhouse,
Daniel Scott, and 
Aldo Keo

## Acknowledgements

    - Built on top of [RTKBase](https://github.com/Stefal/rtkbase) by Stéphane Péchard 
    - the [u-blox ZED-F9P](https://www.u-blox.com/en/product/zed-f9p-module) receiver
    - the [pynmea2](https://github.com/Knio/pynmea2) and [geographiclib](https://geographiclib.sourceforge.io/) libraries.
