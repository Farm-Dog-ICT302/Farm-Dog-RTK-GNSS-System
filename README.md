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

### Rover
    - Raspberry Pi 4B 4GB
    - u-blox ZED-F9P GNSS module
    - GNSS antenna (mounted on 2m pole)
    - Tripod Height - 2metres
    - ABS IP66 enclosure
    - Power bank

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

