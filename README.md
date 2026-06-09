# Farm-Dog-RTK-GNSS
This respository contains information about a setup of an RTK GNSS Surveying and Positioning System built using the u-blox ZED-F9P module, RTKBase, PyGPSClient and a Python script to log positional data.

The system consists of 2 components - a base station which receives GPS data from the satellites and calculates the correction offset and a rover which receives these correction offsets and calculate these with its own GPS setellite data to achieve centimetre-level accuracy.

The goal is to achieve sub-2.5 centimetre-level accuracy.

## What it does
A custom Python survey tool that connects to a ublox ZED-F9P GNSS, receiver, this feeds RTK
corrections from a base station via NTRIP, and records sub-2.5cm accurate coordinates to CSV.

## Hardware Required

### Base Station
    - Raspberry Pi 4B 4GB
    - u-blox ZED-F9P GNSS module
    - GNSS antenna
    - Tripod Height - 2metres (used for field testing)
    - ABS IP66 enclosure
    - Power bank or fixed power supply
    - Wi-Fi router (shared) - GL-MT3000

![Base Station](https://github.com/Farm-Dog-ICT302/Farm-Dog-RTK-GNSS-System/blob/main/images/hardware_images/BaseStation.jpeg)

### Rover
    - Raspberry Pi 4B 4GB
    - u-blox ZED-F9P GNSS module
    - GNSS antenna (mounted on 2m pole)
    - Tripod Height - 2metres
    - ABS IP66 enclosure
    - Power bank
    
![Rover Image](https://raw.githubusercontent.com/Farm-Dog-ICT302/Farm-Dog-RTK-GNSS-System/main/images/hardware_images/Rover2.jpeg)

### Network
    - GL-MT3000 portable Wi-Fi router
      <- Connects base and rover wirelessly
      <- NTRIP corrections on port 2101

### Software - Base Station
    - RTKBase v2.7.0
    - Raspberry Pi OS

### Software - Rover
    - farmdog.py (this program introduce as solution)
    - PyGPSClient (graphical monitoring)
    - Raspberry Pi OS

## Program Versions

### farmdog.py (v1.0) - Initial Release Prototype
    - this program connects directly to the ZED-F9P serial port.
    - proven working with real RTK Fixed data base on equation provided.

### farmdog.py (v2.0) - WEB UI with Flask Server
    - OOP rewrite with clean class separation (GPS source, RTK client, web server, CSV writer)
    - Flask web UI on port 5000 this is accessible from any device on the same network
    - Two modes: Map Mode (live position display) and Track Mode (navigate to target coordinates)
    - Geodesic distance and azimuth via 'geographiclib' (WGS84 ellipsoid)
    - Mock GPS source for offline development when hardware is unavailable


## Team - ICT302 Team IT01 (S1 2026)

**Supervisor:** David MURRAY
**Client:** Terry Koziniec

## Acknowledgements

    - Built on top of [RTKBase](https://github.com/Stefal/rtkbase) by Stéphane Péchard 
    - the [u-blox ZED-F9P](https://www.u-blox.com/en/product/zed-f9p-module) receiver
    - the [pynmea2](https://github.com/Knio/pynmea2) and [geographiclib](https://geographiclib.sourceforge.io/) libraries.
