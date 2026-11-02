# Summary of Python Modules
## Main
Main run file for program. Runs at startup and calls all the other modules for program operation.  
* Inputs: N/A
* Outputs: N/A
* Dependencies: sync_rtc, poll_sensors, set_flags, archive_data, cloud_sync, negotiate_wakeup  
* Link: [main.py](../src/main.py)
## sync_rtc
Interfaces with the Witty Pi via their bash script to update the pi's RTC  
* Inputs: N/A
* Outputs: N/A
* Dependencies: subprocess  
* Link: [sync_rtc.py](../src/sync_rtc.py)
## poll_sensors
Controls the input polling. Turns the sensors on and off via GPIO, calls each polling submodule, interprets the sensor data into a depth, repeats polling until a reasonable value is reached,  and saves a timestamp of the successful measurement  
* Inputs: N/A
* Outputs: average depth in inches, depth error in inches, site photo, timestamp string
* Dependencies: RPI.GPIO, time, poll_pressure, poll_ultrasonic, estimate_depth, poll_camera  
* Link: [poll_sensors.py](../src/poll_sensors.py)
## poll_pressure
Interfaces with the pressure sensor over the GPIO pins to collect the current reading. Converts the output to kPA for later calculations  
* Inputs: N/A
* Outputs: pressure reading in kPa
* Dependencies: TBD  
* Link: [poll_pressure.py](../src/poll_sensors/poll_pressure.py)
## poll_ultrasonic
Interfaces with the ultrasonic sensor over UART to collect the current reading. Converts the output to m for later calculations  
* Inputs: N/A
* Outputs: ultrasonic reading in meters
* Dependencies: pyserial  
* Link: [poll_ultrasonic.py](../src/poll_sensors/poll_ultrasonic.py)
## estimate_depth
Determines the depths obtained from the pressure (kPa) and ultrasonic (m) readings. Returns the average between the two measurements and the absolute error between them  
* Inputs: pressure reading kPa, ultrasonic reading in meters
* Outputs: average depth in inches, depth error in inches
* Dependencies: N/A  
* Link: [poll_ultrasonic.py unit tests](../tests/poll_sensors/poll_ultrasonic_test.py)
## poll_camera
Interfaces with the camera over USB to capture a photo of the site  
* Inputs: N/A
* Outputs: site photo
* Dependencies: pyusb  
* Link: [poll_camera.py](../src/poll_sensors/poll_camera.py)
## set_flags
If the average depth measured is greater than the threshold, sets the flood_flag high and sets the wakeup interval for the shorter flood mode value. Otherwise, sets the flood_flag low and sets the wakeup interval for the normal operation value  
* Inputs: average
* Outputs: flood flag bool, wakeup interval in minutes
* Dependencies: N/A  
* Link: [set_flags.py](../src/set_flags.py)
## archive_data
Appends the timestamp, average_depth, depth_error, and site_photo to a numpy memmap stored on the SD card to avoid performance issues as the archive grows  
* Inputs: average depth in inches, depth error in inches, site photo, timestamp string, and flood flag bool
* Outputs: N/A
* Dependencies: numpy  
* Link: [archive_data.py](../src/archive_data.py)
## cloud_sync
Transmits data to chosen cloud service. Thingsboard uses with HTTP for communication. First probe network with head request to check connection. If unsuccessful, append data to failed uploads list on disk. Otherwise, upload current measurement and each measurement on list to server via HTTP call. If upload for an entry was successful, remove it from the list  
* Inputs: failed uploads list, most recent row in archive memmap (current interval measurement)
* Outputs: N/A
* Dependencies: http  
* Link: [cloud_sync.py](../src/cloud_sync.py)
## negotiate_wakeup
Interfaces with the Witty Pi via their bash script to negotiate the next startup. Uses the wakeup interval found in set_flags  
* Inputs: wakeup interval in minutes
* Outputs: N/A
* Dependencies: subprocess  
* Link: [negotiate_wakeup.py](../src/negotiate_wakeup.py)
