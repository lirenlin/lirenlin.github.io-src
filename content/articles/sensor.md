Title: Sensors
Date: Sun 17 Feb 15:54:30 CET 2019
Category: SLAM
Tags: SLAM

# Sensor
* Proprioceptive sensors
	* Motor speed, heading of the robot
* Exteroceptive sensors
	* distances to objects, images

* Passive sensors
	* Measure energy coming from the environment, very much influenced by
	the environment.
* Active sensors
	* emit their proper energy and measure the reaction. Better
	performance, but some influence on environment.

For example:

some encoders, PC, P
Vision-based sensors, EC, P
Active ranging, EC, A

compass: 罗盘, magnetic field on earth
gyroscope: 陀螺仪
provide an absolute measure for the heading of a mobile system

inclinometer: 测斜仪
Accelerometer
## IMU: Inertial Measurement Unit
An inertial measurement unit (IMU) is a device that uses measurement systems
such as gyroscopes and accelerometers to estimate the relative position (x, y, z),
orientation (roll, pitch, yaw), velocity, and acceleration of a moving
vehicle with respect to an inertial frame.

* IMUs are extremely sensitive to measurement errors in gyroscopes and
accelerometers: drift in the gyroscope unavoidably undermines the estimation of
the vehicle orientation relative to gravity, which results in incorrect
cancellation of the gravity vector. Additionally observe that, because the
accelerometer data is integrated twice to obtain the position, any residual
gravity vector results in a quadratic error in position.
* After long period of operation, all IMUs drift.  To cancel it, some external
reference like GPS or cameras has to be used

## Beacons
Beacons are signaling guiding devices with a precisely known position

* Beacons require changes in the environment. Initial setup and maintain -> costly.
* Limit flexibility and adaptability to changing environment.

## Augmented Reality Tag
## Global Position System
### Differential Global Positioning System (dGPS)
DGPS requires that a GPS receiver, known as the base station, be set up on a
precisely known location.The base station receiver calculates its position
based on satellite signals and compares this location to the known location.
The difference is applied to the GPS data recorded by the roving GPS receiver

position accuracies in sub-meter to cm range

## Range sensors
Large range distance measurement. key element for localization and environment
modeling

Ultrasonic sensors as well as laser range sensors make use of propagation speed
of sound or electromagnetic waves respectively.

* Quality of time of flight range sensors
	* Inaccuraciesin the time of fight measurement(laser range sensors)
	* Opening angle of transmitted beam (especially ultrasonic range sensors)
	* Interaction with the target (surface, specular reflections)
	* Variation of propagation speed (sound)
		* sound
		* electromagnetic signal
	* Speed of mobile robot and target (if not at stand still)

Laser Range finder are also known as Lidar (Light Detection And Ranging)
### Sonar
### Laser range finder

# Sensor Model

# Sensor Fusion


https://www.ethz.ch/content/dam/ethz/special-interest/mavt/robotics-n-intelligent-systems/asl-dam/documents/lectures/autonomous_mobile_robots/spring-2015/04_-_Perception_I_-_Sensors.pdf
