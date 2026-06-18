## INSTALLATION MANUAL 

RTK GNSS Survey and Positioning System 

Date: 05/06/2026 Version 2.1 

Client: Terry Koziniec Supervisor: David Murray 

Clark Carpentero, Flynn McAlpine-Monkhouse, Aldo Keo, Daniel Scott, Vo Thu, Pema Selden, Tim Fausten 


## 1 INTRODUCTION 

This installation manual outlines the necessary steps required to install the Raspberry  Pi  OS  onto  the  system  SD  cards  and  details  the  mandatory configuration tasks that must be completed prior to deploying the Farm Dog software. This workflow includes installing the required Wi-Fi drivers, setting up SSH  access  for  remote  terminal  administration,  and  configuring  static  IP addresses for both the Base Station and the Rover. 

**Note:** This document should be read in conjunction with the Farm Dog User Manual. 

## 2 SOFTWARE REQUIREMENTS 

Before initiating the installation process, make sure that the following requirements are met before proceeding: 

- **OS Imaging Software:** To install Raspberry Pi OS onto an SD card, download Raspberry Pi Imager from the following website: www.raspberry.com/software 

- **Remote Console Access:** For remotely accessing the Raspberry Pi for configuration, ensure you have access to Terminal / Command Prompt or software like Putty. 

- **Remote Desktop Access (Optional):** If you want to use the Desktop version, ensure you have access to a VNC application (such as UltraVNC Viewer or RealVNC). Please note that VNC needs to be enabled on the Raspberry Pi first. For information on how to enable this function, please read the configuration of VNC section. 

- **Network Environment:** During the initial installation and configuration process, ensure that the user’s host computer and both Raspberry Pi units are connected on the same local network. 

## 3 HARDWARE REQUIREMENTS 

Before starting the physical installation process, ensure that you have active internet connection to download and install the necessary software packages and system updates for the Raspberry Pi modules. 

Also make sure that you have access to the following: 

- Micro SD cards 

- Micro SD card reader 

- A computer or laptop with USB ports to connect the card reader 

- The USB Wi-Fi module and its external antenna 

- The Raspberry Pi’s 

For hardware installation of the Base Station and Rover enclosures, please have 

the following tools and components ready: 

- Philips head screws and screwdriver 

- Metal Standoffs for the Raspberry Pi boards 

- Adhesive Velcro tape 

- The IP66 ABS plastic enclosures (for both Base Station and Rover) 

- A power drill with appropriate drill bits 


## 4 SOFTWARE INSTALLATION 

## 4.1 INSTALLING RASPBERRY PI OS 

Before beginning the software installation, ensure you have a reliable internet connection and that the host computer is on the exact same local network as the two Raspberry Pi units. 

- **Step 1:** Navigate to www.raspberry.com/software. 

- **Step 2:** Download the “Raspberry Pi Imager” application. 


## 4.2 RASPBERRY PI IMAGER 

To install the Raspberry Pi Imager on a Windows operating system, execute the downloaded installer, select language and follow the setup wizard prompts: 

- **Step 1:** Read and agree to the License Agreement. 

- **Step 2:** Select the destination folder where you would like the Raspberry Pi Imager to be installed. 

- **Step 3:** Wait for the extraction and installation process to complete (go grab a coffee whilst the program is being installed). 

- **Step 4:** If prompted by Windows Security, grant permission to allow the Raspberry Pi Imager device software to be installed. 

- **Step 5:** Click **"Finish"** once the setup wizard indicates the installation is complete. 

- **Step  6:** With  the  application  successfully installed, prepare your Micro SD card and insert it into your computer's Micro SD card reader. 

## 4.3 FLASHING AND CONFIGURING THE OPERATING SYSTEM 

Once the Raspberry Pi Imager is installed, proceed with configuring and writing the OS to your Micro SD card. 

- **Step 1:** The Raspberry Pi Imager will launch automatically after clicking "Finish" during the installation process. Ensure your Micro SD card is inserted into the card reader. 

- **Step  2:** Under  the  device  selection  menu,  choose  the  appropriate hardware model, which in this case is the " **Raspberry Pi 4** ". 

- **Step 3:** For the operating system, select " **Raspberry Pi OS (64-bit)** " and click **Next.** 

- **Step 4:** Select your inserted Micro SD card as the target storage device. 

- **Step  5:** When  prompted  to  customize  settings,  enter  a  designated **hostname** for the device and click **Next** . 

- **Step 6:** Configure the localization settings by selecting the appropriate capital city (e.g., Canberra for Australia), time zone, and keyboard layout. 

- **Step 7:** Establish a secure username and password for the device. 

- **Step 8:** To connect the device to your secure Wi-Fi network automatically, enter the corresponding network SSID and password. 

- **Step 9:** Enable SSH and choose password authentication to allow remote administrative access via the terminal. 

- **Step 10:** Leave the "Raspberry Pi Connect" option disabled and select **Next** . 

- **Step 11:** Review your configuration choices, then click **"Write"** to begin flashing the image to the SD card. 

- **Step 12:** A system warning will appear advising that all existing data on the target drive will be erased; click **"I understand, erase and write"** to proceed. 

- **Step 13:** Wait for the writing process to finalize. A success message will appear upon completion. 

- **Step 14A:** Once the OS image has been successfully written for the Rover, repeat this exact process (Steps 2 through 13) for the Base Station. **Crucial Note:** Ensure that the hostname and username for the Base Station distinctly differ from the credentials established for the Rover. 

- **Step 14B:** Once the OS image has been successfully written for the Rover, repeat this exact process (Steps 2 through 13) for the Base Station. **Crucial Note:** Ensure that the hostname and username for the Base Station distinctly differ from the credentials established for the Rover. 

- **Step 15:** Safely unplug the Micro SD card reader from your computer or laptop and remove the Micro SD card. 

- **Step 16:** Insert the newly flashed Micro SD card into the Micro SD slot on the Raspberry Pi 4B. 

- **Step 17:** To power on the Rover or Base Station, plug the USB Type-C cable into the USB-C port on the side of the Raspberry Pi and connect the USB Type-A connector into the power bank or another appropriate power source. 

## 5 RASPBERRY PI INITIAL SETUP 

Once  the  device  is  powered  on,  proceed  with  the  initial  network 

configuration and system updates. 

**Note:** It is highly recommended to use a wired Ethernet connection for this initial SSH session. Making changes to the wireless settings over a Wi-Fi connection may cause the network to drop out during configuration. 

- **Step 1:** Access your Wireless Access Point (AP) administration portal to retrieve the dynamically assigned IP address of the Rover. 

- **Step 2:** Open a Terminal (macOS/Linux) or an SSH client like PuTTY (Windows) to establish a remote connection to the Rover by executing the following command: 

`ssh -l user-rover [IP Adress of rover]` 

- **Step 3:** If prompted with a security warning regarding an unrecognized host key, accept the key to establish the connection. 

- **Step 4:** Log in using the specific username and password that you configured for the Rover earlier during the OS imaging process. 

**`** 

- **Step 5:** Once successfully authenticated, execute the following command to ensure all system packages and dependencies are fully updated: 

`sudo apt update && sudo apt upgrade -y` 

## 6 INSTALL FARM DOG PROGRAM 

Once the operating system is fully updated, you can proceed with installing the proprietary software on the Rover unit. 

- **Step 1:** On the Rover terminal, utilize the `git clone` command to pull the 

Farm Dog application repository directly from GitHub: 

`git clone https://github.com/Farm-Dog-ICT302/FarmDog-App.git` 

- **Step 2:** Change into the clone Farm-Dog-RTK-GNSS-System directory: 

`cd FarmDog-App` 

- **Step 3:** Execute the initialization script to start the local server and run the application: 

 `./startserver.s` 

- **Step 4:** (Optional Diagnostic) You can optionally install a graphical user interface tool called PyGPSClient to monitor the raw GNSS receiver data directly. To install it, run the following command: 

`pip install pygpsclient` 

## 7 INSTALLING RTKBASE FOR BASE STATION 

With the operating system installed and updated, proceed with installing the RTKBase software to handle the GNSS correction data. 

- **Step 1:** Access your Wireless Access Point (AP) administration portal to retrieve the dynamically assigned IP address of the Base Station. 

- **Step  2:** Ensure  your  GNSS  receiver  (u-blox  ZED-F9P)  is  physically connected via USB to the Base Station Raspberry Pi. 

- **Step 3:** Open an SSH terminal session to the Base Station and execute the following commands sequentially to download, grant permissions, and run the RTKBase installation script: 

`cd ~` 

`wget` 

`https://raw.githubusercontent.com/Stefal/rtkbas e/master/tools/install.sh -O install.sh chmod +x install.sh` 

`sudo ./install.sh --all release` 

- **Step 4:** Once the terminal script finishes processing, open a web browser on  your  host  computer  and  navigate  to  `http://ip_of_your_sbc`  (the installation script will output the exact IP address you need to use). Log in to the web interface using the default password: `admin`. 

- **Step 5:** Navigate to the “Settings” tab, click on "Options" under the Main Service section, and then click "Detect/Configure" to allow the system to identify the connected GNSS Receiver. 

- **Step 6:** The system should automatically detect the ZED-F9P module and prompt a confirmation message. Click "Apply then configure". 

- **Step 7:** A success message will appear confirming that the GNSS Receiver has been configured successfully. Click "Close". 

- **Step 8:** Navigate to the “ **Status** ” page and copy the active coordinates of the Base Station. Paste these exact values into the “ **Base Coordinates** ” field in the settings to establish the fixed reference location, then click **Save** . 

- **Step 9:** To enable the correction broadcast,  toggle the “Ntrip Caster Service” to "On" and click "Options". Enter the designated username and password for the Base Station user, set the local caster mount name to "basestation", and click **Save** . 


## 8 INSTALL DRIVERS FOR SIMPLECOM NW621 USB WI-FI ADAPTER 

This section walks you through the installation of the USB Wi-Fi adapter 

that is used for the Base Station and the Rover. It also includes steps to modify 

the configuration file to ensure a more stable Wi-Fi connection. 

- **Step 1:** Plug the USB Wi-Fi module into the USB 3.0 port on the Raspberry Pi. 

- **Step 2:** Navigate to the following GitHub page to download a third-party open-source driver: 

https://github.com/morrownr/88x2bu-20210702 

- **Step 3:** Connect to the Raspberry Pi using SSH through PuTTY. 

- **Step 4:** Install the required packages with the following command: 

`sudo apt install -y linux-headers-$(uname -r)` 

`build-essential bc dkms git` 

- **Step 5:** Create a directory to hold the downloaded driver using this 

command: 

`mkdir -p ~/src` 

- **Step 6:** Move to the newly created directory: 

`cd ~/src` 

- **Step 7:** Download the driver from the GitHub repository using the `git clone` command: 

`git clone https://github.com/morrownr/88x2bu-20210702.git` 

- **Step 8:** Move to the newly created driver directory: 

`cd ~/src/88x2bu-20210702` 

- **Step 9:** Run the installation script with this command: 

`sudo ./install-driver` 

- **Step 10:** After the driver has been successfully installed, you will be asked 

   - if you want to edit the driver options file now. Type **"Yes"** and press Enter. 

- **Step 11:** Inside the driver options file, locate the commented line: _"Edit the following line to change, add or delete options:"_ . 

- **Step 12:** Change the option for the USB mode from `rtw_switch_usb_mode=0` to `rtw_switch_usb_mode=1` so the USB Wi-Fi module is forced to use the USB 3.0 mode instead of the slower USB 
2.0 mode. 

- **Step 13:** Add `rtw_power_mgnt=0` to the exact same line to turn off power saving. 

- **Step 14:** Save the file by pressing **CTRL+O** and hit **Enter** to keep the same 

file name. After this, press **CTRL+X** to exit the file. 

## 9 ACTIVATE THE USB WI-FI CONNECTION AND SET STATIC IP ADDRESS 

After  making  the  changes  to  the  driver  options,  activate  the  Wi-Fi connection on the USB module and set a static IP address for the base station and the rover so both devices have a fixed IP address. 

- 9.1 ACTIVATE THE WI-FI CONNECTION 

**Important Note:** Before continuing, it is advised that the Raspberry Pi is connected  via  Ethernet  since  the  onboard  Wi-Fi  of  the  Raspberry  Pi  will disconnect  when  activating  the  USB  Wi-Fi  connection  and  therefore,  the connection will be lost. 

- **Step 1:** In Putty, type the following command to get to the TUI network manager: 

   - `sudo nmtui` 

- **Step 2:** Use your down arrow key to highlight **"Activate a connection"** and hit Enter. 

- **Step 3:** You are now in the Wi-Fi connection activation menu. Navigate to the USB Wi-Fi network that you want to activate under the USB Wi-Fi heading. 

- **Step 4:** Use the right arrow key to navigate to **"Activate"** and press Enter. 

- **Step 5:** When asked for the Wi-Fi password, type it in. After that, navigate 

   - to **"OK"** and press Enter. 

- **Step 6:** Once you are back in the previous window, navigate to **"Back"** and press Enter to get back to the main screen of the TUI network manager. 

## 9.2 SET STATIC IP ADDRESS 

From the main screen, select “Edit a Connection” and press enter. 

- **Step 1:** From the main TUI screen, select **“Edit a Connection”** and press Enter. 

- **Step 2:** From the list of available networks, choose the Wi-Fi connection that you previously activated and select **“Edit…”** . 

- **Step 3:** Navigate down to **IPv4 Configuration** and change the setting from _Automatic_ to **Manual** . 

- **Step 4:** Input an unallocated static IP address for the device. This must include the subnet mask in CIDR format (e.g., /24), the IP address of the default gateway, and the IP address of the DNS server. 

- **Step 5:** Once the network parameters are entered, exit the TUI network manager by selecting **“Back”** and then **“Quit”** on the main screen. 

- **Step 6:** In order for the new static IP address to apply, you must either deactivate and reactivate the current connection, or simply enter the following command into the Terminal to restart the device: 

   - `sudo reboot` 

- **Step 7:** Once you have successfully completed all the steps in Section 9 for the Base Station, repeat the entire process for the Rover. 

This wraps up the entire network and static IP configuration! 


## 10 CONFIGURATION FOR VNC REMOTE DESKTOP 

To enable VNC and provide the system with a graphical user interface for remote  administration,  you  must  enable  the  service  through  the  built-in configuration tool. 

- **Step 1:** Enter the following command into your active SSH Terminal: 

`sudo raspi-config` 

- **Step 2:** This command opens the Raspberry Pi Software Configuration 

Tool. Use your arrow keys to navigate down and select **“3 Interface** 

## **Options”** . 

## **Step 3:** In the next window, navigate down and select **“I3 VNC”** . 

- **Step 4:** When prompted to enable the service, select **“Yes”** to enable the VNC Server. 

- **Step 5:** You should receive a confirmation screen stating that the VNC Server has been successfully enabled. Select **“OK”** to exit the prompt and then navigate to **"Finish"** to exit the configuration tool. 

## 11 ADDITIONAL SOFTWARE 

Additional software was installed to assist the team throughout the testing phase. LibreOffice was utilized to temporarily view generated CSV files directly on the mobile Rover, and a Samba NAS (Network Attached Storage) was set up to easily export those CSV files over the network to a laptop for temporary mapping. 

## 11.1 ROVER 

- **Step 1:** Update and refresh the system packages by executing the following command: 

   - `sudo apt update && sudo apt upgrade -y` 

- **Step 2:** Install LibreOffice, Samba, and Btop by running: 

   - `sudo apt install libreoffice btop samba sambacommon-bin -y` 

- **Step 3:** Open the Samba configuration file using a text editor such as nano: 

   - `sudo nano /etc/samba/smb.conf` 

- **Step 4:** Add or modify the settings inside the configuration file to match the following parameters: 

`[global] workgroup = WORKGROUP server string = Rover RTK Station server role = standalone server og file = /var/log/samba/log.%m max log size = 1000 logging = file panic  action  =  /usr/share/samba/panic-action %d` 

`# Security settings security = user map to guest = Bad User` 

 `[RoverHome] comment = Share for Home Directory path = /home/user-rover/ browseable = yes read only = yes guest ok = no alid users = user-rover force user = user-rover` 

`[RoverShare] comment = Farm Dog RTK Final Test Build path = /home/user-rover/Downloads/Farm-Dog-RTKGNSS-System-Final-Test-Buildv3 browseable = yes read only = no guest ok = no valid users = user-rover force user = user-rover` 

- **Step 5:** Save the configuration file by pressing **CTRL+O** , press **Enter** to confirm the file name, and then press **CTRL+X** to exit the text editor. 

## 11.2 BASE 

- **Step  1:** Update  and  refresh  the  Base  Station  system  packages  by executing the following command: 

`sudo apt update && sudo apt upgrade -y` 

- **Step 2:** Install the required Samba NAS packages to enable network file 

sharing on the Base Station: 

`sudo apt install` 

## 11.3 SETTING UP SAMBA NAS 

- **Step 1:** To install the required Samba NAS packages and enable network file sharing, execute the following command: 

`sudo apt install samba samba-common-bin -y` 


## 12 HARDWARE ASSEMBLY 

Before beginning the physical assembly of the Base Station and Rover enclosures, ensure all necessary tools, fasteners, and components are organized and readily available. 

## 12.1 REQUIRED TOOLS 

- Drill 

- Hammer 

- Assortment of drill bits 

   - 3/32 drill bit 

   - Serrated drill bit 

- Ruler 

- Pencil 

- Masking Tape 

## 12.1.1 ADDITIONAL PARTS 

- 12x - M.5 Screws 

- 12x - M.5 Nuts 

- 9x - M.25*20+6mm standoffs 

- 4x - M.25*11+6mm standoffs 

- 2x Waterproof Cable Glands PG9 4mm – 8mm 

## 12.2 ADDITIONAL COMPONENTS 

- 1x Right Angle SMA Male to Female connector 

- 2x 15cm Male to Female extension cable 

## 12.3 INSTALLATION OF COMPONENTS FOR THE MOBILE ROVER 

**Step 1:** Unscrew 2x Philips screw to remove metal plate from IP66 Small ABS Box 

**Step 2:** Use masking tape to tape up the metal mounting plate, this will allow to mark the holes/dimension to easily mount up the standoff to then mount the Raspberry Pi 

**Step 3:** Temporally place the Raspberry Pi onto the masked metal plate in the top left corner and using a pencil mark out the mounting holes on the Raspberry Pi onto masked mounting plate. (Please be mindful of the placement of the Raspberry Pi to close the edge of the mounting plate as it will not provide enough clearance when install the mounting plate back into the ABS box) 

**Step 4** : Using a hammer and centre punch, create small indentation on the 4 marked crosses. Using a drill and 3/32 drill bit carefully drill out the 4 marked holes for mounting the metal standoffs. Afterwards, remove the masking tape and align the metal stand offs and using a 4x M.5 Nuts tighten down the 4x M.25*20+6mm stand offs to the metal base. 

**Step 5:** Using 3x M.5 screws, carefully screw down the raspberry pi onto the 4x M.25*20+6mm stand offs. Using another standoff screw it into the bottom right position. 

**Step 6:** Carefully place the GPS module on top of the mount and screw it on top of the standoff. This will give enough clearance to prevent the components from short circuiting. Plug in the external Simplecom NW621 USB Wi-Fi Module and screw in the female SMA 15cm cable to the end of the male SMA connector 

**Step 7:** Carefully lowering the mounted components on the metal mounting base plate into the ABS box and carefully screw it into the original screw down points. 

**Step 8:** Temporarily place the power bank into the case/box for alignment, once satisfied with the location of the battery use Velcro tape and remove the adhesive tape place one side of the Velcro into positioning. Place the other Velcro tape onto the battery, cut off any excess. 

**Step 9:** Using masking tape, tape up the short right side of the ABS box masking tape, eyeball and using pencil to mark out the cut out for the cable glands and male SMA connector. Please be mindful of the metal plate. 

**Step 10:** Carefully drill out both holes for the cable gland connector and the male SMA connector. Use the appropriate drill bits in this case a 3/32 and serrated drill bit was used. After the desired size hole is drill out, remove the masking tape. Removing any debris or material. 

**Step 11:** Clean up the excess and carefully and screw in and remount the metal mounting plate with mounted components back into the box. 

## 12.4 INSTALLATION OF COMPONENTS FOR THE BASE STATION 

**Step 1:** Temporally place the components into the box to see spacing and where the components would be mounted permanently. 

**Step 2:** Unscrew and use masking tape to tape up the metal mounting plate, this will allow to mark the holes/dimension to easily mount up the standoff to then mount the Raspberry Pi and SparkFun GPS-RTK-SMA ZED-F9P 

**Step 3:** Trace out the holes of the mounting points from the Raspberry Pi and SparkFun GPS-RTK-SMA ZED-F9P, this can be achieved using the existing base mounting plate from the “Mobile Rover” to outline the holes for the Raspberry Pi. Continue trace out the mounting holes from the SparkFun GPS-RTK-SMA ZED-F9P. 

**Step 4:** Using a hammer and centre punch, create small indentation on the 4 marked crosses. Using a drill and 3/32 drill bit carefully drill out the 8 marked holes for mounting the metal stand offs. Afterwards, remove the masking tape and align the metal stand offs and screw down the 4x M.25*20+6mm stand offs and 4x M.25*11+6mm to the metal base. Afterwards, you can temporarily test fit the components to see if they are aligned. 

**Step 5:** Carefully screw in the remaining component to the corresponding standoffs. 

**Step 6:** Moving over to the exterior Large ABS IP66 Enclosure, mask up and use a ruler to centre and mark the cable gland hole and another hole for the SMA male connector hole. Use a drill and serrated drill bit to carefully drill out both holes to the corresponding size. 

**Step 7:** Install and mount the cable gland and SMA connector into the drilled-out holes. 

**Step 8:** Finish mounting and screw in the metal stand offs onto the mounting plate for the mounting plate, afterwards mount and screw in both Raspberry Pi and ZED F9P GPS modules. 

**Step 7:** Cable and plug in the Simplecom NW621 USB Wi-Fi Module and screw in 15 cm SMA extension cable to the end of the USB Wi-Fi module. 

**Step 8:** Carefully lowering the mounted components on the metal mounting base plate into the ABS box and carefully screw it into the original screw down points. 

**Step 9:** Connected the components into the corresponding USB ports, connect the SMA male to female extension cable 

**Step 10:** Temporarily place the power bank into the case/box for alignment, once satisfied with the location of the battery use Velcro tape and remove the adhesive tape place one side of the Velcro into positioning. Place the other Velcro tape onto the battery, cut off any excess. 




