

//A class to handle getting the location from the server
class LocationClass {

    //Constructor
    constructor(pollInterval = 500) {
        this.pollInterval = pollInterval;
        this.timer = null;
        this.isStopped = false;
        this.isRequestRunning = false;
    }

    //start the recursive polling function
    startPolling(callback) {

        //Check if already running
        if (!this.isStopped && this.timer) return;
        this.isStopped = false;
        this.isRequestRunning = false;

        const pollServerGPSData = () => {
            //Call to the server for specific information, providing the back end a latitude and a longditude target based on input
            $.ajax({
                url: "/trackGPSData",
                data: {targetLat: $("#targetLat").val(), targetLon: $("#targetLon").val()},
                type: "GET",
                dataType: "json",
                success: (data) => {
                    callback(data.latitude, data.longitude, data.distance, data.azimuth);
                    console.log(data);
                },
                error: (xhr, status, error) => {
                    console.error("Polling error: " + status + error);
                },
                complete: () => {
                    this.isRequestRunning = false;
                    if (!this.isStopped) {
                        this.timer = setTimeout(() => pollServerGPSData(), this.pollInterval);
                    }
                }
            });
        };
        pollServerGPSData();
    }

    stopPolling() {
        this.isStopped = true;
        if (this.timer) clearTimeout(this.timer);
    }
}


class CompassClass {
    constructor() {
        this.listener = null;
    }

    startPolling(callback) {
        const handleOrientation = (event) => {
            const heading = event.webkitCompassHeading || event.alpha;
            if (event.alpha != null) callback(heading);
        };

        // Check to see if if DeviceOrientationEvent is supported
        if (typeof DeviceOrientationEvent === 'undefined') {
            console.error('DeviceOrientationEvent is not supported on this device.');
            $("#compass").html("The compass is not supported by this device");
            return;
        }

        //Request permission on iOS13+ devices
        if (typeof DeviceOrientationEvent.requestPermission === 'function') {
            DeviceOrientationEvent.requestPermission()
            .then(permissionState => {
                if (permissionState === 'granted') {
                    window.addEventListener('deviceorientation', handleOrientation);
                    this.listener = handleOrientation;
                } else {
                    $("#compass").html("Permission must be given for compass to function");
                    console.error('Permission denied for device orientation.');
                }
            })
            .catch(console.error);
        } else {
            //Non IOS devices
            window.addEventListener('deviceorientation', handleOrientation);
            this.listener = handleOrientation;
        }
    }

    stopPolling() {
        if (this.listener) window.removeEventListener('deviceorientation', this.listener);
    }
}

class NavigationUtilitiesClass {

    // Converts degrees to radians
    static degToRad(deg) {
        return deg * (Math.PI / 180);
    }

    // Converts radians to degrees
    static radToDeg(rad) {
        return rad * (180 / Math.PI);
    }

    // Calculate arrow rotation for the phone screen
    static getArrowRotation(azimuth, phoneHeading) {
        // Arrow rotation = difference between azimuth and phone heading
        let rotation = azimuth - phoneHeading;
        // Normalize to 0-360°
        rotation = (rotation + 360) % 360;
        console.log("current rotation = " + String(rotation));
        return rotation;
    }
}

class UIClass {
    constructor(arrowSelector) {
        this.arrow = $(arrowSelector);
        this.latValue = null;
        this.lonValue = null;
    }

    updateArrow(rotation) {
        this.arrow.css('transform', `rotate(${rotation}deg)`);
    }

    updateValues(lat, long, distance) {
        $("#longitudeValue").html(long.toFixed(2) + "°");
        $("#latitudeValue").html(lat.toFixed(2) + "°");
        $("#distanceValue").html(distance.toFixed(2) + " meters");
    }

    static async toggleDiv(name) {
        if ($("#" + name + "Checkbox").is(":checked")) {
            $("#" + name).show();
            localStorage.setItem(name, 'true');
        } else {
            $("#" + name).hide();
            localStorage.setItem(name, 'false');
        }
    }

}

class ConvertFloatOrZero {
    static convert (value) {
        const f = parseFloat(value);
        if (isNaN(f)) {
            console.log("error not an acceptable value, using 0.00 degrees");
            return 0.00;
        }
        return f;
    }
}

//Cross your fingers this all works
class TrackModeApp {
    constructor() {
        this.locationClass = new LocationClass();
        this.compassClass = new CompassClass();
        this.uiClass = new UIClass("#arrow");
        this.currentLat = null;
        this.currentLon = null;
        //Boolean for telling parent class if this one is running or not
        this.isRunning = false;
        this.currentAzimuth = 0.0;
    }

    start() {
        //Flip running boolean
        this.isRunning = true;
        //Start the GPS server polling
        this.locationClass.startPolling((lat, lon, dist, azimuth) => {
            this.currentLat = lat;
            this.currentLon = lon;
            this.uiClass.updateValues(lat, lon, dist);
            this.azimuth = azimuth;
        });

        //Start polling the phone's compass
        this.compassClass.startPolling((heading) => {
            if (this.currentLat != null && this.currentLon != null && this.azimuth != null) {
                const targetLat = ConvertFloatOrZero.convert($("#targetLat").val());
                const targetLon = ConvertFloatOrZero.convert($("#targetLon").val());
                const rotation = NavigationUtilitiesClass.getArrowRotation(
                    this.azimuth,
                    heading
                );
                this.uiClass.updateArrow(rotation);
                console.log(`Arrow rotation ${rotation.toFixed(2)}°`);
            }
        });

    }

    stop() {
        this.locationClass.stopPolling();
        this.compassClass.stopPolling();
        this.isRunning = false;
    }
}

