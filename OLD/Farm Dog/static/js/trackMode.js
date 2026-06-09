// Function to start polling the compass

class LocationClass {
    constructor(pollInterval = 500) {
        this.pollInterval = pollInterval;
        this.timer = null;
        this.isStopped = false;
        this.isRequestRunning = false;
    }

    startPolling(callback) {
        const pollServerGPSData = () => {
            $.ajax({
                url: "/trackGPSData",
                data: {targetLat: 0.0, targetLon: 0.0},
                type: "GET",
                dataType: "json",
                success: (data) => {
                    callback(data.latitude, data.longitude);
                    console.log(data);
                    $("#longitudeValue").html(data.longitude.toFixed(2) + "°");
                    $("#latitudeValue").html(data.latitude.toFixed(2) + "°");
                    $("#distanceValue").html((data.distance/1000).toFixed(2) + "meters");
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
            if (event.alpha != null) callback(event.alpha);
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

class NavigationClass {

    // Converts degrees to radians
    static degToRad(deg) {
        return deg * (Math.PI / 180);
    }

    // Converts radians to degrees
    static radToDeg(rad) {
        return rad * (180 / Math.PI);
    }

    // This is calculated here to reduce the network traffic from the front and back ends
    static calculateBearing(lat1, lon1, lat2, lon2) {
        const latitude1 = this.degToRad(lat1);
        const latitude2 = this.degToRad(lat2);
        const changeInLongitude = this.degToRad(lon2 - lon1);

        const y = Math.sin(changeInLongitude) * Math.cos(latitude2);
        const x =
        Math.cos(latitude1) * Math.sin(latitude2) -
        Math.sin(latitude1) * Math.cos(latitude2) * Math.cos(changeInLongitude);

        let calculatedAngle = Math.atan2(y, x); // Bearing in radians
        calculatedAngle = this.radToDeg(calculatedAngle); // Convert to degrees
        return (calculatedAngle + 360) % 360; // Normalize to 0-360°
    }

    // Calculate arrow rotation for the phone screen
    static getArrowRotation(currentLat, currentLon, targetLat, targetLon, phoneHeading) {
        const bearingToTarget = this.calculateBearing(currentLat, currentLon, targetLat, targetLon);
        // Arrow rotation = difference between bearing and phone heading
        let rotation = bearingToTarget - phoneHeading;
        // Normalize to 0-360°
        rotation = (rotation + 360) % 360;
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
        if (this.arrow.length) {
            this.arrow.css('transform', `rotate(${rotation}deg)`);
        }
    }
}

class convertFloatOrZero {
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

//Create all of the instances
window.locationClass = new LocationClass();
window.compassClass = new CompassClass();
window.uiClass = new UIClass("#arrow");

window.currentLat = null;
window.currentLon = null;

window.locationClass.startPolling((lat, lon) => {
    window.currentLat = lat;
    window.currentLon = lon;
});

window.compassClass.startPolling((heading) => {
    if (window.currentLat != null && window.currentLon != null) {
        const rotation = NavigationClass.getArrowRotation(
            window.currentLat,
            window.currentLon,
            convertFloatOrZero.convert($("#targetLat").val()),
            convertFloatOrZero.convert($("#targetLon").val()),
            heading
        );
        window.uiClass.updateArrow(rotation);
        console.log(`Arrow rotation: ${rotation.toFixed(2)}°`);
    }
});
