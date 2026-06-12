## USER MANUAL 

RTK GNSS Survey and Positioning System 

Client: Terry Koziniec Supervisor: David Murray 

Clark Carpentero, Flynn McAlpine-Monkhouse, Aldo Keo, Daniel Scott, Vo Thu, Pema Selden, Tim Fausten 



## 1 Introduction 

Welcome  to  the  Farm  Dog  RTK  GNSS  System  User  Manual.  This document is designed to provide comprehensive, step-by-step instructions on how to set up, configure, and operates the Farm Dog system for high-precision field surveying. 

This  guide  covers  everything  from  the  initial  network  and  hardware configuration of the Base Station and Rover, to utilizing the core software features (Map Mode and Find Mode), and troubleshooting common operational issues. Whether you are mapping agricultural boundaries, validating measurements, or conducting precise point-to-point navigation, this manual will ensure you achieve the optimal centimetre-level accuracy the system is designed to deliver. 

## 2 System Overview 

Maintaining an accurate field survey record can be time-consuming and error-prone when done manually. The Farm Dog RTK GNSS System simplifies this process by combining highly precise GPS hardware with an easy-to-use digital interface. 

Instead of relying on rough estimates or handwritten notes, users can capture structured coordinate data in real time and export it for reporting and analysis. Reliable location records are essential for farm planning and decision-making. With a consistent digital workflow, it becomes incredibly easy to map fence lines, paddocks, and other points of interest. With a consistent digital workflow, it becomes incredibly easy to map paddocks, validate measurements, compare repeated observations, and demonstrate survey accuracy. 

## 2.1 Key Features 

- RTK GNSS positioning using the u-blox ZED-F9P 

- Web-based interface built with Flask 

- Live coordinate display 

- Find Mode navigation to target coordinates 

- CSV coordinate logging 

- NTRIP correction support 

- Sub-2.5 cm positioning accuracy (under ideal conditions) 

## 3 Technical Specifications 

## 3.1 In the Box 

The Farm Dog system consists of the following components: 

- Base station 

- Rover 

- 2x tripods 

The base station and rover consist of multiple parts which are listed in 

the technical specifications below. 

## 3.2 Base Station 

- 1x Raspberry Pi 4B 4GB RAM 

- 1x 128 GB Micro SD Card 

- 1x Power Bank 20000Mha 

- 1x IP66 Enclosure box 

- 1x USB Wi-Fi Adapter 

- 1x SparkFun GPS-RTK-RMA-SMA 

- 1x SMA GNSS Antenna 

- 1x Metal disc 

## 3.3 Rover 

- 1x Raspberry Pi 4B 4GB RAM 

- 1x 128 GB Micro SD Card 

- 1x Power Bank 20000Mha 

- 1x IP66 Enclosure box 

- 1x USB Wi-Fi Adapter 

- 1x SparkFun GPS-RTK-RMA-SMA 

- 1x SMA GNSS Antenna 

- 1x Metal disc 

## 4 Requirements 

## 4.1 Minimum PC/Host Requirements 

- **RTKBase Configuration** - a host computer running macOS, Windows 10 to Windows 11, or a Linux distribution is required to launch the RTKBase software and configure the base Station’s known location. 

- **Web Application Access** – to launch the Farm Dog web application, the user can use any device (e.g., smartphone, tablet, or laptop) that has a standard web browser installed. 

- **Network Constraints** – the Base Station and Rover must be connected to the exact same local Wi-Fi network to function. The Farm Dog project relies on local data transmission and currently does not support external remote connections via the internet. 

## 4.2 Wireless Access Point 

- A sufficient outdoor wireless access point is required to allow the Base Station and Mobile Rover to communicate and transmit NTRIP correction data. 

- Both devices must be on the same local network as data is transmitted entirely locally. 

- Furthermore, this network connection allows the user to access Mobile Rover and Base Station via SSH and remote desktop to complete the initial setup process. 

## 4.3 Supported Web Browsers for GUI 

- The Farm Dog system interface can be accessed by simply entering the Rover’s IP address directly into a web browser. 

- Therefore, the system supports a wide variety of modern web browsers including Safari, Google Chrome, Firefox, Microsoft Edge, Brave and Opera GX. 


## 5 Using the device 

## 5.1 Hardware installation 

The initial hardware installation of the Farm Dog system is explained in the Installation Manual. If you want to set up the base station and rover before using the system to use the map mode or find mode, please see the Hardware Setup section below. The base station runs RTKBase which allows the user to monitor the satellite signal strength and to set the known location of the base station. This package comes pre-installed. 

The rover has Raspberry Pi OS and the python program installed on its Micro SD card which contains the main Farm Dog program the user interacts with. This program can be found in the GitHub repository so it can be redownloaded in the case of the equipment being damaged or for project expansion in the case of the user wanting to add new functionality to the Farm Dog projec 

The Farm Dog GitHub Repository can be found here: 

https://github.com/Farm-Dog-ICT302/Farm-Dog-RTK-GNSS-System 

## 5.2 Getting started: User Interface Guide 

## 5.2.1 Map mode 

This mode displays the current GNSS position in real-time. Users can save points directly to a CSV file for later review and further processing, with the option to append a custom “Description” to each point. 

## 5.2.2 Find mode 

This feature helps the user navigate to target coordinates by displaying the real-time distance and direction to the destination. Once the Rover reaches within 2.4 cm of the target, an “Arrived at target!” message will appear on the screen. 

## 5.2.3 CSV Output 

All saved coordinate points are automatically exported to a CSV file, which can be seamlessly opened in standard spreadsheet software such as Microsoft Excel, Numbers. 

## 5.2.4 RTK Status 

For the highest accuracy, points should only be logged when an active “RTK Fix” is available. The system achieves this when it displays the number code **4** . _(For more information on the different RTK Fix statuses, please read the RTK Fix Status section)_ . 

## 5.2.5 Non-Core features and Customization 

- **Global Options:** Includes a toggle to enable Dark Mode acroos the application 

- Map Mode Data Toogles: Users can customize their screen by choosing 

to show or hide specific data fields, including: 

- Latitude 

- Longitude 

- Altitude 

- Fix 

- Satellites 

- HDOP 

## 6 Recommended Usage 

For the best results and maximum survey accuracy, please adhere to the 

following field practices: 

- **Initial Base Station Calibration** – The Base Station must remain entirely stationary in its setup location for a minimum of 2 hours during first-time use to establish a highly accurate known location. 

- **Wait for Stabilization** – Allow the positioning telemetry to fully stabilize before logging any points. 

- **Clear Sky View** – Record points in open areas with good sky visibility to prevent satellite signal obstruction. 

- **Consistent  Placement** –  Keep  your  antenna  placement  consistent throughout the entire surveying session. 

- **Stay  Stationary** –  Completely avoid  moving  the  Rover while  actively logging a point of interest. 

- **Require RTK Fix** – If an RTK Fix is available, it should always be used to ensure high-accuracy point collection. 

## 7 Hardware Setup 

The Farm Dog system requires the following equipment to run properly so it is important to ensure that you have all required equipment before starting the system 

## 7.1 Equipment needed 

Provided equipment: 

- Base Station 

- Rover 

- 2x Tripods 

User-Provided Equipment: 

- Laptop, Desktop device or smartphone 

- Wi-Fi access point 

- _Optional:_ Ethernet cable for a more stable Base Station connection 

## 7.2 Setting up the equipment 

Once all the required equipment is gathered, follow the steps below to deploy the Farm Dog system for operation. 

## 7.2.1 Base Station 

**NOTE:** When setting up the Base Station, make sure you place it in an area with 360-degree sky coverage. It must have adequate height clearance to avoid ground static interference and physical obstructions. 

## **CRITICAL WARNING: BASE STATION INITIALIZATION (SURVEY-IN)** 

To  achieve  true  centimetre-level  accuracy,  the  Base  Station  must establish an absolute fixed coordinate before it can send valid correction data to the Rover: 

- **Minimum  Time  Requirement** –  if  you  are  deploying  in  a completely new, unknown location, you must leave the Base Station powered on, completely stationary, and tracking satellites for a **minimum of 2 hours** prior to conducting the survey. 

- **Do Not Move** – this wait time allows the software to average out atmospheric interference. Moving or bumping the Base Station tripod during this period will corrupt the data and force the 2-hour calculation process to restart. 

## **Setup Steps:** 

1. Locate a flat ground surface where the Base Station tripod will stand. 

2. Extend the tripod legs and firmly plant it. 

3. Screw the metal reflector disc onto the top thread of the tripod. 

4. Place the GPS antenna directly on top of the metal reflector. 

5. Place the Base Station enclosure box neatly on the ground beneath the tripod. 

6. Plug the USB Type-A connector into the power bank to power on the system. 

7. Close the lid of the box and use the clips to securely lock. 

## **Connecting to the Network (First-Time Setup):** 

If this is the first time the Base Station is connecting to your local network, 

follow these steps: 

1. Connect the Base Station to your Wi-Fi network or connect it directly 

to your network via an ethernet cable. 

2. Ensure that both the Base Station and the Wi-Fi access point are fully operational.  The  Base  Station’s  USB  Wi-Fi  module  features  a blinking light, which visibly indicates that it is receiving network signals. The Wi-Fi access point should also have a status light indicating it is operational. 

_(For detailed steps on how to activate the Wi-Fi connection, please read “Activate the USB Wi-Fi connection and set Static IP address” in the Installation Manual)_ 

## 7.2.2 Mobile Rover 

Once the Base Station is fully operational, carry the Rover and place it approximately 5 meters away from the Base Station. This initial physical separation is necessary to ensure an accurate baseline reading. 

## **Setup steps:** 

1. Extend the tripod legs and firmly plant it on the ground. 

2. Screw the metal reflector disc onto the top thread of the tripod. 

3. Place the GPS antenna directly on top of the metal reflector. 

4. Strap and tighten the Rover enclosure box securely onto the tripod stand. 

5. Plug the USB Type-A connector into the power bank to power on the Rover. 

6. Close the lid of the box and use the clips to securely lock it. 

7. _Optional:_ Mount your mobile phone onto the provided phone mount 

   - for easy screen access. 

Connecting to the Network (First-Time Setup): 

If this is the first time Rover is connecting to your local network, follow these steps: 

1. Connect the Rover to your Wi-Fi network. 

2. Ensure that both the Rover and the Wi-Fi access point are fully operational. The Rover’s USB Wi-Fi module features a blinking light, which visibly indicates that it is current receiving network signals. The Wi-Fi access point should also have a status light indicating it is operational. 

_(For detailed steps on how to activate the Wi-Fi connection, please read “Activate the USB Wi-Fi connection and set Static IP address” in the Installation Manual)._ 

## **Final Check:** 

Once both the Base Station and Rover are situated in their correct positions,  powered  on,  and  successfully  connected  to  the  wireless  LAN network, your hardware setup is complete. You can now move on to the software configuration. 


## 8 Software Setup 

## 8.1 Base Station Initial Setup 

Once the hardware is set up and operational, you must connect your laptop or 

desktop device to the Base Station to collect and configure the RTK data. 

## 8.1.1 Device Configuration 

Turn on your desktop or laptop device and complete the following steps 

to properly connect and use the Farm Dog System. 

1. Open the Wi-Fi menu on your device, select the same Wi-Fi network that  the  Base  Station  is  connected  to,  and  enter  the  network password. 

2. Open your default web browser and enter your router’s IP address (this is typically 192.168.0.1 or 10.0.0.1). 

3. Enter the administrator password for your router. 

4. Once logged in, view the list of connected devices to find the IP addresses for both your Base Station and Rover. Copy the Base Station’s IP address. 

5. Open a new browser tab and paste the Base Station’s IP address. You will be redirect to the RTKBase login page. Enter the password 

   - ( **admin** ) to sign in. 

6. Navigate to the **Settings** tab. Under “Main service”, click on **Options** 

   - then click **Detect/Configure** to allow the system to search for the GNSS Receiver. 

7. The system should automatically detect the u-blox ZED-F9P module 

and display a confirmation prompt. Click **Apply then configure** . 

8. A success message will appear indicating that the GNSS Receiver 

   - has been configured successfully. Click **Close** . 

9. Navigate to the Status page and copy the base Station’s current coordinates. Return to the **Settings** tab, paste these into the “Base Coordinates” field to lock in the known location, and click **Save** . 

10. Switch the “Ntrip Caster service” toggle to **On** and click **Options** . 

Enter the following credentials for the local caster: 

- **Username:** user-base 

- **Password:** user-base 

- **Mount Name:** basestation 

- Click **Save** to apply the changes 

11.  Once these settings are saved, the Base Station is fully configured. You can now process to set up the Rover. 

## 8.2 Rover Initial Setup 

The Rover comes with the Farm Dog Python program pre-installed and is designed to run automatically as soon as the device boots up. Once powered on, you can access the Farm Dog interface by simply entering the Rover’s IP address and port number into a web browser on any device connected to the same local network. 

_(Note: If you ever experience a hardware failure or the software becomes corrupted, complete instructions for reinstalling the Python program from scratch are provided in Section 8.2.2 below)._ 

## 8.2.1 Device Configuration and Manual Startup 

Normally, the Rover’s software will start automatically. However, to access the web interface, you first need to locate the Rover’s IP address. If the program fails to start on boot, you can also use these steps to start it manually. 

Turn on your smartphone, tablet or laptop device and complete the following steps to properly connect and use the Farm Dog System, by entering the static IP Address of the rover. 

To manually start the Farm Dog System: 

1. Open the Wi-Fi menu on your smartphone, tablet, or laptop and connect to the exact same Wi-Fi network that the Base Station and Rover are connected to. 

2. Once connected to the local Wi-Fi network open your default web browser and paste your router’s IP address (typically 192.168.0.1 or 10.0.0.1) and enter the router password. View the list of connected devices, find the Rover, and copy its IP address. 

3. On this web page you can now view the IP addresses of all connected devices, this includes your Base Station and Rover, copy the IP address of the Rover and continue. 

4. Open Putty (or your preferred SSH client) and connect to the Rover using the IP address you just copied. 

5. Once logged into the Rover’s terminal, you can start the web server using the automatic script: 

. `/startserver.sh` 

6. Alternatively,  you  can  manually  activate  environment  and  run  the program with these commands: 

`cd  FarmDog-App` 

Now activate the binary file and run the python program: 

`source ~/FarmDog/bin/activate` 

`python3 Farm Dog.py` 

7. The Putty terminal output will display the active IP address and port number. Copy this exact address, open a new tab in your web browser, and paste it into the address bar. 

8. You should now see the Farm Dog web application on your screen and can begin using Map Mode or Find Mode! 

## 8.2.2 Connecting the Rover to the Base Station (NTRIP Setup) 

Before starting the application, you must configure the Rover, so it knows exactly where to look for the Base Station’s correction data. 

**1. Open the Configuration File** 

While connected to the Rover via the Putty SSH terminal, navigate to the application folder and open the Python script using the nano text editor: 

`cd  FarmDog-App` 

`sudo nano FarmDog.py` 

**2. Update the Credentials** 

Change the credentials for the Rover to communicate with the Base Station. Enter the following parameters to allow correction data to flow: 

`sudo nano FarmDog.py` 

`Change the baseIP: str = ‘[IP BASESTATION]’` 

`mountpoint: str = ‘[NAME OF MOUNT POINT]’ ntripUser: str = ‘[USER BASE STATION]’ ntripPass: str = ‘[USER PASSWORD BASE STATION]’` 

**3.** The terminal will now supply a local IP address to for the Farm Dog web UI. Copy this link from the terminal and paste into your web browser to access the program via the GUI. 

`http://[IP ADDRESS]:5000` 

**4.** You should now see the Farm Dog web application on your screen and can begin using Map Mode or Find Mode. 

## 8.2.3 Software Recovery and Reinstallation 

In the event that scripts become corrupted or the Raspberry Pi board needs to be replaced, follow these steps to set up the Farm Dog software on a fresh Raspberry Pi. 

**1. Connect to Local Wi-Fi** 

Ensure your device is connected to the same local Wi-Fi network as the Base Station and Rover. You will need an active internet connection to download the necessary dependencies. 

**2. Download the Python Script** 

Open a Putty terminal window connected to the Rover and clone the software repository directly from GitHub by entering the following command: 

`git clone` 

`https://github.com/Farm-Dog-ICT302/FarmDog-App.git` 

**3. Launch the Automatic Installation Script** 

Once the repository is cloned, navigate into the folder, grand execution permissions to the install script, and run it. _(Note: This will automatically install any missing dependencies and start the web server upon completion)._ 

## 8.2.4 Automatic installation script 

**NOTE:** Internet  is  always  required,  as  this  will  allow  the installation of missing dependencies. 

Change directory into “FarmDog-App” 

`cd FarmDog-App` 

Give execute permissions for “install.sh” script and after finishing it will start the program and web server. 

`chmod +x install.sh` 

`./install.sh` 

**4. Future Restarts** 

If you ever need to manually restart the program after this fresh installation, simply enter: 

`./startserver.sh` 

## 8.2.5 Manually run the program 

If you prefer to start the application manually, or if you need to bypass the automatic script for troubleshooting, you can run the Python environment directly. 

**1. Activate and Run** 

In the Putty terminal, enter the following commands one by one to launch the program manually: 

`cd FarmDog-App` 

Now activate the binary file and run the python program: 

`source ~/FarmDog/bin/activate` 

`python3 Farm Dog.py` 

**2. Access the Web GUI** 

Ther  terminal  will  output  a  local  IP address  and  port number  (e.g., http://[ROVER_IP_ADDRESS]:5000).  Copy  this exact link, open a new tab in your web browser, and paste it into the address bar. 

**3. Setup Complete** 

The Farm Dog interface will load on your screen, indicating that the system is fully operational and receiving correction data. You can now begin surveying.  

## 9 Software Guide 

The Farm Dog software features two primary modes for utilizing the RTK GNSS technology. Map Mode and Find Mode where both core functions, along with a safe shutdown option to turn off the RTK devices, can be accessed directly from the Main Menu. 

## 9.1 Find Mode 

Find Mode allows the user to physically navigate to a specific, pre-determined location in the real world. 

## **How to Use Find Mode:** 

**1. Enter Coordinates** 

Load your desired destination by entering the exact X and Y coordinates (Latitude and Longitude). You can either manually type these values into the program or copy them from a previously generated CSV file. 

**2. Start Navigating** 

Click the **Find Target** button to lock in the coordinates. 

**3. Follow the Interface** 

The web GUI will update in real-time, displaying critical navigation data to guide you. This includes your current coordinates, the exact distance remaining to the target, and the compass direction you need to travel. 

**4. Arrival** 

Continue moving according to the on-screen directions. Once your Rover reaches within 10 centimetres of the destination, the 

interface will display an “ **Arrived at Target** ” message to confirm you have successfully located the point. 

## 9.2 Map Mode 

Map Mode is designed for construction and positioning tasks using the 

RTK GNSS system. It allows the user to track specific points of interest in the 

field and export that data into a CSV file for later processing. 

## **Using Map Mode:** 

When active, the Map Mode interface displays the following real-time 

telemetry for the Rover’s current position: 

** Latitude and Longitude** 

- Altitude 

- **RTK Fix Status** _(For more information, refer to the RTK Fix Status_ 

_section)_ 

- **Connected Satellites** 

- **HDOP** (For more information, refer to the HDOP section) 

- **Description (Optional):** A custom note entered by the user for the 

specific plot. 

To log a coordinate, simply enter an optional description and click the Add Location to CSV button at the bottom of the GUI. This records the current telemetry and outputs it directly into a formatted CSV file. 

## **Retrieving Your CVS Data:** 

The  generated  CSV  files  are  stored  locally  on  the  Rover  in  the following directory: /home/user-rover/FarmDog-App/output. 

To easily retrieve these files on your host computer, you can remotely access the Rover’s Network Attached Storage (NAS) via the pre-configured Samba share: 

1. Ensure your computer is connected to the same local network as the Rover. 

2. Open your computer’s file explorer. 

3. Enter the Rover’s Samba address into the address bar: 

`smb://192.168.255.20` 

_(Note: If your Rover’s IP address is different, replace 192.168.255.20 with your specific IP)._ 

4. Access the shared folder to view and copy the CSV files to your local device. 

## 9.3 RTK Fix Status 

The Farm Dog program will display different RTK status values and colour codes during operation. These numbers directly map to the quality and accuracy of the GPS data currently being collected by the Rover. RTK Fixed (4) is the optimal status, delivering the true 1.5-centimetre accuracy required for precise surveying. 

- **0 – No Fix Available (Dark Red)** – the system is not using GNSS and may typically be relying on router data itself. This provides a very broad, inaccurate range of 2km to 5km. 

- **1  –  Standard  GNSS/GPS  (Red)** –  the  system  is  using  standard, uncorrected satellite data. The accuracy of this data is approximately 3 to 10 metres. 

- **2 – DGPS / Differential GNSS (Goldenrod)** – the system is using basic differential corrections. This provides a horizontal accuracy of approximately 0.5 to 1 meter. 

- **4 – RTK Fixed (Green)** – the system has successfully locked onto the Base Station’s correction data. This provides a highly precise 1 to 2 cm horizontal accuracy and 2 to 3 cm vertical accuracy. 

- **5 – RTK Float (Orange)** – the system is receiving correction data but has not fully resolved the exact position yet. The accuracy of this data type ranges from 20 cm to 3 metres. 

## 9.4 HDOP (Horizontal Dilution of Precision) 

Horizontal Dilution of Precision (HDOP) is a critical metric that indicates the quality of the satellite geometry currently visible to your system. 

In terms of the Farm Dog project, HDOP helps communicate the level of signal quality and potential interference between the Base Station, the Rover, and the satellites. A lower HDOP value means the satellites are widely spaced across the sky, resulting in a highly accurate calculation. A higher HDOP value indicates poor satellite geometry, often caused by physical obstruction like tall building or dense tree canopy which reduces positional accuracy. 

Use the following guide to assess your HDOP reading in the field: 

- **< 1:** Best (Ideal surveying conditions) 

- **1 – 2:** Excellent 

- **2 – 5:** Good 

- **> 5:** Poor (consider waiting for better satellite visibility or moving away from obstruction) 

## 10 Error Handling & Recovery 

The Farm Dog software is designed with built-in safeguards to handle several major errors gracefully, ensuring the system does not crash during active fieldwork. The system currently handles the following errors: 

** Missing GPS Data (CSV Export)** 

If a user attempts to save a plot point to the CSV file without a valid GPS lock or data, the system will prevent the save and return a JSON 400 error 

** RTK Stream Connection Lost** 

If the connection to the Base Station’s RTK stream fails or drops mid-session, the system will securely log the error and automatically enter a retry loop, continually attempting to reconnect after a shirt delay. 

** NMEA Parsing Error** 

If the Rover receives corrupted or unreadable raw GPS data (NMEA sentences) form the satellites, it will safely skip the faulty line of data and seamlessly continue reading the next one. 

** Invalid Input Type** 

If incorrect or unreadable data type are entered into the system (such as invalid coordinate formats during Track/Mode), the application will reject the input and return a 400 Error. 

## 11   Troubleshooting 

## 11.1 I cannot open the Farm Dog web page 

- Ensure the Farm Dog program is actively running on the Rover (refer to Section 8.2.3 or 8.2.4) 

- Verify that the exact IP address and port number are entered correctly in your web browser. 

- If you are attempting to open the interface from a smartphone or secondary device, ensure that device is connected to the exact same local Wi-Fi network as the Rover. 

## 11.2 GPS data is not updating 

- Verify that the GNSS receiver is securely connected to the Rover’s hardware. 

- Check the physical connection of the GPS antenna to ensure it has not come loose. 

- Restart the Farm Dog application and wait a few moments for the telemetry data to refresh. 

## 11.3 RTK correction is not working 

- Confirm the Base Station is fully powered on, configured, and operating 

normally. 

- Check that the Rover is connected to the correct network and that the 

   - Base Station credentials in the FarmDog.py file is perfectly accurate. 

- Wait a few moments to allow the correction data stream to establish a 

solid connection. 

## 11.4 Points are not saving to CSV 

- Ensure you have an active GPS lock and that live coordinates are visible on the GUI before attempting to save. 

- Wait a few seconds for the data stream to stabilize, then attempt to click 

save again. 

- Check that the local output folder 

(/home/user-rover/FarmDog-App/output) exists on the device and is writable. 

## 11.5 Position appears unstable 

- Move the Rover to an open area with a clear, unobstructed view of the sky. 

- Avoid operating directly next to tall buildings, dense tree canopies, or large metal structures, as these can block satellites or cause signal bouncing (multipathing). 

- Wait for the RTK Fix Status to reach **4 (RTK Fixed)** and the HDOP to 

drop below **2** before logging critical survey points. 


## 12Appendix 

## 12.2 Appendix A — NMEA Input Format 

The Rover’s ZED-F9P hardware module outputs corrected positional data as NMEA 0183 sentences via a USB serial connection to the Rover Raspberry Pi at a baud rate of 115200. NMEA 0183 is an industry-standard protocol that utilizes ASCII text strings to communicate geospatial data between GNSS receivers and connected software systems. 

The primary NMEA sentence utilized by the Farm Dog system is $GNGGA (Global Navigation Fix Data), which contains the following critical operational metrics: 

- UTC Time 

- Latitude (degrees, minutes) 

- Longitude (degrees, minutes) 

- Altitude above mean sea level 

- Fix Quality (0=No Fix, 1=GPS Only, 2=DGPS, 4=RTK Fixed, 5=RTK Float) 

- Number of Satellites tracked 

- HDOP (Horizontal Dilution of Precision) 

The FarmDog.py application reads these sentences in real-time and parses them using the pynmea2 Python library. It then translates and presents this data to the user through the companion web application interface. Most notably, the system relies on the NMEA data stream to verify the Fix Quality. A Fix Quality of 4 (RTK Fixed) indicates  to  the  application  that  carrier  phase  ambiguity  has  been  successfully resolved and that centimetre-level pass-to-pass accuracy has been achieved. 

## 12.3 Appendix B — CSV Output Format 

The following shows a screenshot of a CSV output file after the user finished adding points to the CSV file in Map Mode and opens the generated CSV file using software such as Microsoft Excel or Libre Office. 

The CSV file is saved on the Micro SD card on the Rover Raspberry Pi in the following format: survey_DD-MM-YYYY_HH-MM-SS.csv. 

It contains the columns count, latitude, longitude, altitude, fix, satellites, hdop and the note that the user entered for a specific point. 

