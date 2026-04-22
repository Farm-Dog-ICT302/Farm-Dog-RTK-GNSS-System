#=================================================
# Farm Dog - RTK GNSS Survey Tool
# Team IT01 - Farm Dog
# Murdoch University ICT302 S1 2026
# Version 1.0 - Initial Release
# Live Coordinate Display
#=================================================
# Show live RTK corrected coordinates
# from ZED-F9P via base station corrections
#=================================================


#=================================================
# Import necessary libraries
# Serial for GPS communication
# Socket for network communication with base station
# Threading for concurrent tasks
# pynmea2 for parsing NMEA sentences
# datetime for timestamping
#=================================================   

import time
import serial
import socket
import threading
import pynmea2
from datetime import datetime


#=================================================
# Settings
# Serial port settings for ZED-F9P
# Base station settings (IP and port)
# Baud rate for GPS communication
# NTRIP settings for receiving corrections
# NTRIP Mountpoint and credentials
#=================================================

GPS_PORT  = '/dev/ttyACM0'  # Adjust as needed
BAUD_RATE = 9600            # ZED-F9P default baud rate for NMEA output
BASE_IP   = '10.0.0.10'     # Base station IP
BASE_PORT = 2101            # Base station port
MOUNTPOINT = 'BaseStation'  # NTRIP mountpoint

# Fix Descriptions for display

FIX_DESCRIPTION = {
    0: 'No Fix',
    1: 'GPS Fix',
    2: 'DGPS',
    4: 'RTK FIXED',
    5: 'RTK FLOAT',
    6: 'Estimated (dead reckoning)',
}

#=================================================
# Global variables for storing GPS data and corrections
# These will be updated by the respective threads
#=================================================

# We use global variables here to allow the feed_rtk_correc 
# function to access the gps_serial variable
# This allows us to send RTK corrections to the GPS from the feed_rtk_correc function
# In a more complex program, we might want to use a more 
# robust method of sharing data between threads (e.g. queues, locks, etc.)

gps_serial = None # Serial connection to GPS


#=================================================
# FEED RTK CORRECTIONS FROM BASE STATION
# This function connects to the base station via socket
# and continuously receives RTK correction data
# runs in background thread
#=================================================

def feed_rtk_correc(): # Connect to base station and feed RTK corrections to GPS
    
    while True: # Continuously try to connect to base station and receive RTK corrections
        
        try: # Try to connect to base station and receive RTK corrections
            
            # We create a socket connection to the base station to receive RTK corrections
            # We set a timeout on the socket to avoid blocking indefinitely if there are issues with the
            # connection to the base station. 
            # If the connection fails, we catch the exception and retry after a short delay.
            
            ntrip = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create socket for NTRIP connection
            ntrip.settimeout(10)
            
            ntrip.connect((BASE_IP, BASE_PORT)) # Connect to base station
            print(" Connected to base station! ")
            
            request = (
                f"GET /{MOUNTPOINT} HTTP/1.0\r\n"
                f"User-Agent: FarmDog/1.0\r\n"
                f"\r\n"
            )
            
            ntrip.send(request.encode()) # Send NTRIP request to base station
            
            while True: # Continuously receive RTK corrections and send to GPS
                
                rtcm = ntrip.recv(1024)
                if rtcm:
                    gps_serial.write(rtcm)  # Send corrections to GPS
                else:
                    break
        except:
            print("RTK connection error, retrying in 5 seconds...")
            time.sleep(2) # Wait before retrying connection to base station
            continue # Retry connection to base station if there is an error

#=================================================
# Connect to GPS and read NMEA sentences
# This function continuously reads from the GPS serial port
#=================================================

def connect_gps(): # Connect to GPS and start reading NMEA sentences
    
    # We declare gps_serial as global here so that we can assign to it within this function
    
    # This allows us to use gps_serial in the feed_rtk_correc 
    # function to send corrections to the GPS
    
    global gps_serial
    
    try: # Try to connect to GPS and start RTK corrections
        
        # Connect to GPS serial port
        # We set a timeout to ensure we don't block indefinitely if there are issues with the GPS connection
        # If the GPS is not connected or the port is incorrect, 
        # this will raise an exception which we catch and print an error message for
        
        gps_serial = serial.Serial(GPS_PORT, BAUD_RATE, timeout=1) # Connect to GPS serial port
        print("Connected to GPS") # Print success message for GPS connection
        
        # Start RTK correction thread
        # We use a daemon thread so that it will automatically close when the main program exits
        # This thread will continuously receive RTK corrections from the base station and feed them to the GPS
        
        t = threading.Thread(target=feed_rtk_correc, daemon=True) # Start RTK correction thread
        t.start() # Start RTK correction thread
        
        print(" RTK Corrections streaming! ")
        
        # We return True here to indicate that we successfully connected 
        # to the GPS and started the RTK correction thread
        
        return True # Successfully connected to GPS and started RTK corrections
    
    # If there is an error connecting to the GPS (e.g. port not found, permission issues, etc.),
    # we catch the exception and print an error message to the user.
    
    except Exception as e: # Handle GPS connection errors
    
        # We print the error message to the user so they know what went wrong with the GPS connection
        # This is important for troubleshooting, as common issues include incorrect port, 
        # GPS not connected, or permission issues with the serial port.    
        
        print(f"Error connecting to GPS: {e}")
        
        # We return False here to indicate that we failed to connect to the GPS,
        return False


#=================================================
# Main function to display live coordinates
# This function continuously reads NMEA sentences from the GPS
# and displays the current coordinates and fix status
#=================================================

def main(): # Main function to display live coordinates
    
    print("\033[H\033[J") # Clear terminal on start
    print("=================================================")
    print(" Farm Dog - RTK GNSS Survey Tool ")
    print(" Team IT01 - Farm Dog ")
    print(" Murdoch University ICT302 2026 ")
    print(" Version 1.0 - Initial Release ")
    print(" Live Coordinate Display ")
    print("=================================================\n")
    
    # Attempt to connect to GPS and start RTK corrections
    # If connection fails, print error message and exit
    # This ensures users know if there is an issue with the GPS connection 
    # before we start trying to read coordinates
    
    # If we can't connect to GPS, there's no point in trying to read coordinates, 
    # so we exit early with a clear message about the issue.
    
    if not connect_gps(): # Attempt to connect to GPS
        print(" Cannot connect to GPS! ")
        print(" Check /dev/ttyACM0 is correct and GPS is connected. ")
        return # Exit if GPS connection fails
    
    
    print(" Reading coordinates... ")
    print(" Press Ctrl+C to stop. ")
    print("=================================================\n")
    
    while True: # Continuously read GPS data and display coordinates
        
        try: # Try to read GPS data and display coordinates
            
            line = gps_serial.readline().decode('utf-8', errors='ignore').strip() # Read line from GPS serial
            
            if '$GNGGA' in line or '$GPGGA' in line: # Check for GGA sentence which contains fix and coordinate info
                msg = pynmea2.parse(line) # Parse NMEA sentence
                
                if msg.latitude and msg.longitude: # Check if we have valid coordinates
                    fix_num = int(msg.gps_qual or 0) # Get GPS fix quality
                    hdop = float(msg.horizontal_dil or 0) # Get HDOP for accuracy indication
                    
                    # Get fix description based on fix quality
                    # For example, 4 = RTK FIXED, 5 = RTK FLOAT, etc.
                    # This helps users understand the quality of the GPS fix they have
                    # We can use the fix quality to estimate the accuracy of the coordinates
                    
                    # Estimate accuracy based on HDOP
                    # HDOP (Horizontal Dilution of Precision) 
                    # is a measure of the quality of the GPS signal and how it affects the accuracy of the position fix.
                    
                    # ZED-F9P data sheet indicates typical accuracies for different fix types
                    # RTK Fixed accuracy = 0.01m + HDOP effect
                    # RTK Float accuracy = 0.5m + HDOP effect
                    # GPS Only accuracy = 2.5m + HDOP effect
                    
                    # So we multiply HDOP by a factor depending on the fix type to get an estimated accuracy
                    
                    # Example with HDOP by those base accuracy estimates:
                    # RTK Fixed: accuracy = HDOP * 0.01 (since RTK fixed is very accurate, we use a small multiplier)
                    # RTK Fixed: 0.55 x 0.01 = 0.0055m (5.5mm)
                    
                    # RTK Float: accuracy = HDOP * 0.5 (since RTK float is less accurate than fixed, we use a larger multiplier)
                    # RTK Float: 0.55 x 0.5 = 0.275m (27.5cm)
                    
                    # GPS Only: accuracy = HDOP * 2.5 (since GPS only is much less accurate, we use an even larger multiplier)
                    # GPS Only: 0.55 x 2.5 = 1.375m (137.5cm)
                    
                    if fix_num == 4: # RTK FIXED
                        accuracy = round(hdop * 0.01, 4) # RTK fixed accuracy ~1cm
                    
                    elif fix_num == 5: # RTK FLOAT
                        accuracy = round(hdop * 0.5, 4) # RTK float accuracy ~0.5m
                    
                    else: # Other fixes
                        accuracy = round(hdop * 2.5, 4) # General accuracy estimate
                        
                    fix_desc = FIX_DESCRIPTION.get(fix_num, 'Unknown') # Get fix description for display
                        
                    sub25 = 'YES' if accuracy <= 0.25 else 'NO' # Indicate if sub-25cm accuracy is achieved
                    
                    print("\033[H\033[J") # Clear terminal for live update
                    print("=================================================")
                    print(" FARM DOG RTK GNSS SURVEY TOOL ")
                    print(" Team IT01 - Farm Dog ")
                    print(" Murdoch University ICT302 2026 ")
                    print(" Version 1.0 - Initial Release ")
                    print(" Live Coordinate Display ")
                    print("=================================================\n")
                    print(f" Time:           {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    print(f" Fix:            {fix_desc}")
                    print(f" Latitude:       {msg.latitude:.8f}°")
                    print(f" Longitude:      {msg.longitude:.8f}°")
                    print(f" Altitude:       {float(msg.altitude or 0):.2f} m")
                    print(f" HDOP:           {hdop:.2f}")
                    print(f" Est. Accuracy:  {accuracy:.4f} m")
                    print(f" Sub-25cm:       {sub25}")
                    print(f" Corr Age:       {msg.age_gps_data or 'N/A'} s")
                    print("=================================================\n")
                    print(" Press Ctrl+C to stop. ")
                    print("=================================================\n")
                    
        except KeyboardInterrupt: # Handle Ctrl+C to exit
            print("\nExiting...")
            break
        except:
            pass # Ignore other errors and continue reading
        
    if gps_serial:
        gps_serial.close() # Close GPS serial connection on exit
    
    print("=================================================")
    print(" Farm Dog survey tool stopped. ")
    print("=================================================")
    
    
#=================================================
# Run the main function when the script is executed
#=================================================

# This is the standard Python idiom for making code only run when the script is executed directly
# and not when it is imported as a module in another script.

# This allows us to have the main functionality of the program in the main() function,
# and only run it when we want to execute this script directly.

if __name__ == "__main__": # Run the main function when the script is executed
    main() # Run the main function to start the program
    
    
# =================================================
# End of Farm Dog RTK GNSS Survey Tool v1.0
# Team IT01 - Farm Dog
# Murdoch University ICT302 S1 2026
# Version 1.0 - Initial Release
# Live Coordinate Display
# =================================================        