#Import all required modules
import serial
import pynmea2
import socket
import threading
import math
import csv
from datetime import datetime
import os
import time
from dataclasses import dataclass, asdict
from flask import Flask, render_template, jsonify, request
import sys
import random
from typing import Optional
from geographiclib.geodesic import Geodesic



#A data class holds all the settings for the GPS functions
@dataclass
class Config:
    gpsPort: str = '/dev/ttyACM0'
    baudRate: int = 9600
    baseIP: str = '10.0.0.10'
    basePort: int = 2101
    mountPoint: str = 'BaseStation'
    refreshSec: int = 1

#A class that holds all the web server settings
@dataclass
class WebServerConfig:
    host: str = '127.0.0.1'
    port: int = 5000


#A dataclass that holds all the GPS data
@dataclass
class NMEAGPSData:
    #Data
    latitude:float
    longitude:float
    altitude:float
    fix:int
    satellites:int
    hdop:float


#A class that acts as a shared state between the GPS logic and the Webserver
class GPSState:
    def __init__(self):
        self._lock = threading.Lock()
        self._data: Optional[NMEAGPSData] = NMEAGPSData(0.0,0.0,0.0,0,0,0.0)

    def update(self, data: NMEAGPSData):
        with self._lock:
            self._data = data

    def get(self) -> Optional[NMEAGPSData]:
        with self._lock:
            return self._data

#A class that generates html based on the provided data structure so that the front end is less tied to specific data types
class HTMLGenerator:
    #Generates a html string based on its own data structure to send to the front end so that the front end is not tied to the structure of the data
    @staticmethod
    def generateMapModeDataViewHTML(orderArray, measurementArray):
        #Define the variable outside of the if statement and for loop statement
        htmlString = ""
        #Loops through the element names in the order array and the measurement strings in the measurement array
        for element, measurement in zip(orderArray, measurementArray):
            #Generates the HTML content
            htmlString += (
                f'<div id = "{element}" class = "mapModeDataDisplay">\n'
                f'  <div id = "{element}Label" class = "mapModeDataLabel">\n'
                f'      {element.capitalize()}\n'
                f'  </div>\n'
                f'  <div id = "{element}ValueView" class = "mapModeDataView">\n'
                f'      <div id = "{element}Value" class = "mapModeDataValue">\n'
                f'          0.0\n'
                f'      </div>\n'
                f'      <div id = "{element}Measurement" class = "mapModeData">\n'
                f'          {measurement}\n'
                f'      </div>\n'
                f'  </div>\n'
                f'</div>\n'
                )
        #Returns HTML string
        return htmlString

    #Generates a html string based on its own data structure to send to the front end so it is not tied to any specific data structure
    @staticmethod
    def generateMapModeMenuHTML(orderArray):
        #Start of the HTML menu
        htmlString = (
            '<div id = "showHideLabel">\n'
            '   Show/Hide Data:\n'
            '</div>\n'
            )
        #Loop through the array
        for element in orderArray:
            #Add a set of HTML elements to the htmlString variable
            htmlString += (
                f'<div id = "{element}Menu">\n'
                f'  {element.capitalize()} <input type="checkbox" id="{element}Checkbox" class = "mapMenuCheckbox" checked/>\n'
                f'</div>\n'
                )
        #return HTML string
        return htmlString









#TESTING
#TESTING
#DO NOT LEAVE THIS IN THE FINAL PRODUCT
#TESTING
#TESTING

# --- Mock GPS Data Source (Implements IGPSDataSource) ---
class GPSLogicClassTest:
    def __init__(self, config: Config, gpsState: GPSState):
        self.config = config
        self.gpsState = gpsState
        self.stopFlag = False

        self.latitude_range = (47.0, 49.0)  # Simulating a region of latitude
        self.longitude_range = (8.0, 10.0)  # Simulating a region of longitude
        self.altitude_range = (100, 2000)  # Altitude in meters
        self.satellite_range = (5, 30)  # Number of satellites
        self.hdop_range = (0.5, 3.0)  # Horizontal Dilution of Precision
        self.fix_quality_range = (1, 4)  # Simulate GPS fix quality: 1 (no fix), 2 (2D fix), 4 (3D fix)



    def connect(self):
        return True

    def threadStart(self):
        thread = threading.Thread(target=self._run, daemon=True)
        thread.start()

    def _generate_fake_data(self) -> NMEAGPSData:

        lat = random.uniform(*self.latitude_range)
        lon = random.uniform(*self.longitude_range)
        alt = random.uniform(*self.altitude_range)
        sats = random.randint(*self.satellite_range)
        gpsFix = random.choice([1, 2, 4])  # Randomly choose a GPS fix quality
        hodiofpr = random.uniform(*self.hdop_range)  # Random HDOP value

        returnData = NMEAGPSData(
            latitude= lat,
            longitude=lon,
            altitude=alt,
            fix=gpsFix,
            satellites=sats,
            hdop=hodiofpr
        )

        return returnData

    def _run(self):
        while not self.stopFlag:
            data = self._generate_fake_data()

            # 🔥 This is the key line (same as real GPS)
            self.gpsState.update(data)

            time.sleep(self.config.refreshSec)

    def stop(self):
        self.stopFlag = True

#END TESTING
#END TESTING
#DO NOT LEAVE THIS IN THE FINAL PRODUCT
#END TESTING
#END TESTING


#A class that handles the GPS logic
class GPSLogicClass:
    def __init__(self, config: Config, gpsState: GPSState): #Constructor method
        self.config = config #import the config class
        self.serial = None #define the serial object but don't populate it yet
        self.gpsState = gpsState #Shared GPS data class
        self.stopFlag = False;

    #Define a method that will handle connecting to the GPS
    def connect(self):
        try:
            self.serial = serial.Serial(
                self.config.gpsPort,
                self.config.baudRate,
                timeout = 1
            )
            return True
        #Capture error from trying to connect to GPS
        except Exception as e:
            print(f"Error connecting to GPS {e}")
            return False

    def threadStart(self): #Starts its functions in a separate thread
        thread = threading.Thread(target=self._run, daemon=True) #Daemon will kill this process when the main process is killed.
        thread.start();

    #Define a method that will handle reading the data from the GPS serial port
    def read(self):
        line = self.serial.readline().decode('utf-8', errors='ignore').strip() #Read the next line of the serial
        print("Please check to see if the messages being recieved are being filtered out")
        print(f"GPS Raw: {line}")

        if '$GNGAA' in line or '$GPGGA' in line: #Check to see if it is an NMEA message
            try:
                msg = pynmea2.parse(line)
            except pynmea2.ParseError as e:
                print(f"Error parsing NMEA message: {e}")
                return

            print ("Please send me a screenshot of this output")
            print (msg.__dict__)

            if msg.latitude and msg.longitude: #Check to see if the message contains the latitude and longitude
                #return an instance of the NMWAGPSData dataclass
                data = NMEAGPSData(
                    msg.latitude,
                    msg.longitude,
                    getattr(msg, "altitude", 0),
                    getattr(msg, "gps_qual", 0),
                    getattr(msg, "num_sats", 0),
                    getattr(msg, "horizontal_dil", 0)
                )
                #Update the shared GPS instance
                self.gpsState.update(data)

    #start the GPSPolling loop
    def start(self):
        while self.stopFlag == False:
            self.read()

    #stop the GPSPolling loop
    def stop(self):
        self.stopFlag = True;

    #Call the functions to connect the GPS then start the polling loop
    def _run(self):
        self.connect()
        self.start()

    #Sends corrections
    def sendCorrections(self, data):
        if self.serial:
            self.serial.write(data)


#A class that handles the RTK Correction logic
class RTKLogicClass:
    def __init__(self, config: Config, gpsLogicClass: GPSLogicClass): #Constructor
        self.config = config
        self.gpsLogicClass = gpsLogicClass

    def threadStart(self): #Starts its functions in a separate thread
        thread = threading.Thread(target=self._run, daemon=True) #Daemon will kill this process when the main process is killed.
        thread.start();

    def _run(self):
        while True: #Infinite loop only killed when the main function is killed
            try:
                #Create a TCP client socket
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

                #Connect to the server
                sock.connect((self.config.baseIP, self.config.basePort))

                #Create the HTTP request
                request = (
                    f"GET /{self.config.mountPoint} HTTP/1.0\r\n"
                    f"User-Agent: FarmDog/1.0\r\n\r\n"
                )
                #Send the request
                sock.send(request.encode())

                while True:
                    data = sock.recv(1024) #Read up to 1024 bytes from the server

                    if not data: #Check if server closed the connection
                        break

                    self.gpsLogicClass.sendCorrections(data) #Send data to the class responsible for handling GPS logic

            except Exception as e: #Error handling
                print("RTK error:")
                print(e)
                print("retrying...")
                time.sleep(2)
            finally:
                sock.close()


#A class for calculating distance between two GPS co-ordinates and returning a directional hint
class GeoCalculator:

    @staticmethod #Static so there is no need to create an instance. This function calculates the arc distance between two points.
    def distanceBetweenCoordinates(lat1, lon1, lat2, lon2): #Now with geodesic so that it can maintain the cm accuracy
        result = Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)

        distance = result["s12"] #Distance in meters

        return distance

    def azimuthBetweenCoordinates(lat1, lon1, lat2, lon2):
        result = Geodesic.WGS84.Inverse(lat1, lon1, lat2, lon2)

        azimuth = result["azi1"]

        return azimuth

    @staticmethod #Static so there is no need to create an instance. This function calculates the arc distance between two points.
    def distanceBetweenCoordinatesOLD(lat1, lon1, lat2, lon2):
        R=6371000 #Approximately the earths radius in meters

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)

        #Use haversine formula to account for the earths curvature

        a = math.sin(dlat/2)**2 + \
        math.cos(math.radians(lat1)) * \
        math.cos(math.radians(lat2)) * \
        math.sin(dlon/2)**2

        #Calculate final distance
        arcDistance = R * 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

        return arcDistance

#A class for handling the writing of the CSV file

class CSVWriter:
    def __init__(self, folderPath): #Constructor creates a new csv file at the path
        self.fileExists = True
        self.count = 0
        self.headers = ["count","latitude","longitude","altitude","fix","satellites","hdop","Note"]
        #Set folder path for the duration of the CSVWriter instance and make it if it doesn't exist
        self.folderPath = folderPath
        #Make the folder if it doesn't exist
        os.makedirs(self.folderPath, exist_ok=True)
        #Sets the filepath
        self.filePath = self.setFilePath()
        #Creates the CSV file with appropriate headers
        self.createFile()

    #function to determine the nearest available filePath
    def setFilePath(self):
        #Initial file name
        fileName = datetime.now().strftime('%d-%m-%Y_%H-%M-%S') + ".csv"
        tempFilePath = self.folderPath + fileName
        # BUG #3: Path concatenation issue - should use os.path.join() for cross-platform compatibility
        # Current: tempFilePath = self.folderPath + fileName  (missing path separator on Windows)
        # Should be: tempFilePath = os.path.join(self.folderPath, fileName)


        
        #Count for the attempts to find a clear file
        attemptCount = 0
        #Check if file already exists when initialising the class to make sure no data is overwritten
        while self.fileExists:
            if os.path.isfile(tempFilePath):
                attemptCount += 1
                tempFilePath = self.folderPath + fileName[:-4] + "_" + str(attemptCount) + ".csv" #Change file to folderPath/filePath_{count}.csv
            else:
                if attemptCount != 0:
                    tempFilePath = self.folderPath + fileName[:-4] + "_" + str(attemptCount) + ".csv" #Change file to folderPath/filePath_{count}.csv
                    print(f"File already exists, exporting instead to {tempFilePath}")
                self.fileExists = False;
        return tempFilePath

    #Function to create a blank CSV file with the provided headers
    def createFile(self):
        with open(self.filePath, mode='w', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(self.headers)
                  # BUG #1: Using writerows() instead of writerow()
            # writerows() expects list of lists (multiple rows)
            # writerow() is for a single row
            # Should be: writer.writerow(self.headers)   ← CORRECT: All headers in one row

    #Function to write the provided data to the CSV file
    def write(self, data):
        with open(self.filePath, mode='a', newline='', encoding='utf-8') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(data.strip().split(","))
                        # BUG #2: Using writerows() instead of writerow()
            # writerows() expects list of lists (multiple rows)
            # writerow() is for a single row with one comma-separated value list
            # Current: writer.writerows(data.strip().split(","))  ← WRONG: Each value becomes separate row
            # Should be: writer.writerow(data.strip().split(","))   ← CORRECT: All values in one row
            self.count = self.count + 1

    #Function to provide the current entry count
    def getCount(self):
        return self.count


#A class for handling the locate mode
class TrackMode:

    @staticmethod
    def generateTrackModeJSON(gpsData: NMEAGPSData, targetLat, targetLon):
        if gpsData is None:
            return jsonify({"error" : "no data"}), 404
        else:
            try:
                targetLat = float(targetLat)
                targetLon = float(targetLon)

            except (TypeError, ValueError):
                return jsonify({"error": "invalid or missing target coordinates"}), 400

            distance = GeoCalculator.distanceBetweenCoordinates(
                gpsData.latitude,
                gpsData.longitude,
                targetLat,
                targetLon
            )

            azimuth = GeoCalculator.azimuthBetweenCoordinates(
                gpsData.latitude,
                gpsData.longitude,
                targetLat,
                targetLon
            )
 # BUG #6: Excessive console output - prints every GPS update (every 1 second)
            # This causes console spam making it hard to see actual errors
            # Consider reducing these prints or using logging framework
            print("Target Latitude =" + str(targetLat))
            print("Target Longitude =" + str(targetLon))
            print("Actual Latitude =" + str(gpsData.latitude))
            print("Actual Longitude = " + str(gpsData.longitude))
            print("Distance between target and actual = " + str(distance))

            gpsDataDict = {
                "latitude": gpsData.latitude,
                "longitude": gpsData.longitude,
                "distance": distance,
                "azimuth": azimuth
            }

        return jsonify(gpsDataDict)


#A class for handling the map mode
class MapMode:
    @staticmethod
    def generateMapModeJSON(gpsData: NMEAGPSData, savedPoints):
        #Return 404 if no data
        if gpsData is None:
            return jsonify({"error" : "no data"}), 404

        #Generate dictionary from gpsData
        gpsDataDict = asdict(gpsData)

        #Add the number of saved points
        gpsDataDict["savedPoints"] = savedPoints

        #Return the dictionary
        return jsonify(gpsDataDict)






#A class for handling the FLASK webserver, as the main interface goes through this it acts as the main routing hub for user input and gps output
class FlaskWebServerClass():
    def __init__(self, config: WebServerConfig, gpsState: GPSState): #Constructor
        self.config = config
        self.app = Flask(__name__)
        self.gpsState = gpsState #Shared GPS data class
        self.logger = CSVWriter("output") #Create the CSV file writer

        #GPS Data structure
        self.GPSDataOrder = ["latitude", "longitude", "altitude", "fix", "satellites", "hdop"] #Order that the elements should be displayed
        self.GPSDataMeasurement = measurement = ["meters", "meters", "meters", "", "", ""] #A measurement for each element in the order array



    def _setupPaths(self):
        #path for main menu
        @self.app.route('/')
        def index():
            #renders the main index menu
            return render_template("index.html")

        @self.app.route("/mainMenu")
        def mainMenu():
            #Renders the main menu inside of the index
            return render_template("mainMenu.html")

        @self.app.route('/trackMode')
        def trackMenu():
            #renders track mode
            return render_template("trackMode.html")

        @self.app.route('/mapMode')
        def mapMenu():
            #renders map mode
            return render_template("mapMode.html")

        @self.app.route('/mapMenuOptions')
        def mapMenuOptions():
            #adds the options to the menu when in map mode
            return HTMLGenerator.generateMapModeMenuHTML(self.GPSDataOrder)

        @self.app.route('/mapModeDataDisplay')
        def getMapMode():
            return HTMLGenerator.generateMapModeDataViewHTML(self.GPSDataOrder, self.GPSDataMeasurement)


        @self.app.route('/mapGPSData')
        def mapGPSData():
            print(self.gpsState.get())
            return MapMode.generateMapModeJSON(self.gpsState.get(), str(self.logger.getCount()))

        @self.app.route('/trackGPSData')
        def trackGPSData():
            targetLat = request.args.get("targetLat")
            targetLon = request.args.get("targetLon")
            return TrackMode.generateTrackModeJSON(self.gpsState.get(), targetLat, targetLon)

        @self.app.route('/csvWrite', methods = ['POST'])
        def csvWrite():
            currentGPSState = self.gpsState.get()
             # BUG #7: Missing None check - if currentGPSState is None, accessing .latitude will crash
            # Current code assumes GPS data is always available, but it could be None during startup
            # Should check: if currentGPSState is None: return error response
            dataString = str(self.logger.getCount()) + "," + str(currentGPSState.latitude) + "," + str(currentGPSState.longitude) + "," + str(currentGPSState.altitude) + "," + str(currentGPSState.fix) + "," + str(currentGPSState.satellites) + "," + str(currentGPSState.hdop) + "\n"

            self.logger.write(dataString)

            return "OK", 200

    def run(self):
        self._setupPaths()
        # BUG #5: debug=True is hardcoded and enabled
        # This is a security risk - exposes Flask debugger to anyone accessing the server
        # Should use environment variable: debug_mode = os.getenv('FLASK_DEBUG', 'false').lower() == 'true'
        # Then: self.app.run(..., debug=debug_mode, ...)
        self.app.run(host = self.config.host, port = self.config.port, debug = True, threaded = True)



#A class for controlling the main app
class MainApp:
    def __init__(self):
        #Setup config classes
        self.config = Config()
        self.webServerConfig = WebServerConfig()

        #Setup GPS state
        self.gpsState = GPSState()

        #Setup GPS and RTK logic threads
        self.gps = GPSLogicClassTest(self.config, self.gpsState)
        # BUG #4: RTK thread is always started, even in test mode with mock GPS
        # This causes connection errors when base station (10.0.0.10:2101) is not available
        # Should be conditional: only start if RTK is actually configured/needed
        # Example: use_rtk = os.getenv('USE_RTK', 'false').lower() == 'true'
        #          if use_rtk: self.rtk = RTKLogicClass(...)
        self.rtk = RTKLogicClass(self.config, self.gps)

        #Setup webserver thread
        self.webServer = FlaskWebServerClass(self.webServerConfig, self.gpsState)




    def run(self):
        #Start GPS Logic thread
        print("connecting to GPS")
        if not self.gps.connect():
            print("could not connect to GPS")
            return

        #start gps thread
        self.gps.threadStart()

        #Start rtk logic thread
        self.rtk.threadStart()

        #Start webserver main task
        print("starting application")

        self.webServer.run()

    def quit(self):
        print("Thankyou for using the Farm Dog GNSS RTK system.")
        time.sleep(5)
        sys.exit()

if __name__ == "__main__":
    app = MainApp() #Create an instance of the MainApp class
    app.run() #Call the run function
