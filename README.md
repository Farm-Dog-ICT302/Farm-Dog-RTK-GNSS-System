# Farm-Dog-RTK-GNSS
This respository contains information about a setup of an RTK GNSS Surveying and Positioning System built using the u-blox ZED-F9P module, RTKBase, PyGPSClient and a Python script to log positional data.

The system consists of 2 component - a base station which receives GPS data from the satellites and calculates the correction offset and a rover which receives these correction offsets and combines these with its own GPS setellite data to achieve centimetre-level accuracy.
