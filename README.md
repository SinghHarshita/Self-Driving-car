# Self Driving Car
A miniature AI - based self - driving car model is developed through this project. This miniature autonomous vehicle uses sophisticated sensors to capture continuous data about the surrounding environment. The model is highly capable of sensing the lane and navigating accordingly. Advanced control systems interpret sensory information to keep track of  their position even though the conditions change.

### Motivation
There are a lot of accidents that happen due to rash driving and violation of traffic rules. These will be eliminated by using self-driving car technology. At the same time, users can control the start and stop of the car i.e. users can call upon the car to pick them up or give commands like go to the market etc. 

The motivation for this project was to make the roads safer and simple for users to navigate.

## About the Project
This section throws light on the proposed system of the project - miniature self-driving cars. A lot of different components constitute the project. Raspberry Pi and Arduino Uno boards have been used for the efficient working of the car and PiCam is used to detect the surroundings. RPi does the analysis of surrounding data collected by the PiCam and based on the analysis sends a signal to the Arduino Uno. Arduino Uno board analyses the signal received by the RPi and commands / steers the car accordingly. 

### The System
The user logs onto our app. This app simplifies the user’s job of giving commands to the self - driving car. When the user says start, the user location along with the command is sent to the car via the internet.
Through the internet the brain of the car, Raspberry Pi, receives the command ‘start’ and the user location. The RPi then starts the PiCam and the video streamed by the PiCam is analysed by the algorithm stored on RPi. With the help of this algorithm, specific commands (signals) are sent to Arduino Uno.

Based on the signals received from Raspberry Pi, Arduino Uno sends signals to the H Bridge which is connected to it. Based on these signals, the polarity of the H Bridge is decided. The H Bridge has four motors connected to it. These motors control the wheels of the car. According to the polarity of the H Bridge, the wheels move forward, backward, left or right i.e. the wheels are steered accordingly.

#### Hardware Requirements
* Raspberry Pi 3B+
* Raspberry Pi 3B+ Clear Case
* EMO 4 wheel 2 layer Robot Smart Car Chassis Kits with Speed Encoder for Arduino DIY
* L298 H Bridge
* RaspiCam 2 with 12’’ CSI Cable 
* 10000mAh Power Bank and a USB cable for power bank
* Arduino Uno
* 16GB SD Card
* Motors
* LEDS
* Capacitor(1000µF 25V)

#### Software Requirements
* Raspbian OS (Stretch)
* Android / Browser
* OpenCV
* Arduino IDE
* Python 3
* C ++

#### Client-Server Architecture
The user machine (computer / laptop / mobile phone ) is the client. When the user logs on the system, he gets connected to the Pi Board which is the server. The user sends commands such as “Start” or “Stop”. Based on these commands the server starts or stops the miniature vehicle.

#### Master-Slave Architecture
Master-slave architecture is proposed for communication between RPi and Arduino Uno boards. The Rpi is the master device as it receives the client request of “Start” or  “Stop” and performs the functions accordingly. Based on the Rpi signals/commands, the arduino works and steers the car. Rpi forms the brain of the system and arduino is the part that receives the commands.

1. Rpi and PiCam

PiCam is the sensor that senses the environment and collects data of the surroundings of the Rpi board and the car. This data is received by the Rpi. This data which is in the form of a video is analysed by the programs running on Rpi. Image processing is performed by the Rpi and based on this processed information the Rpi sends commands to the slave device. These commands are like “Left”, “Right”, “Forward”, “Lane End” etc.

2. Arduino Uno, H bridge and DC motors

The slave device arduino is used to control the speed and dc motors. It does the steering of the car based on the commands received from Rpi. H bridge is used to connect dc motors and arduino uno.
The speed is controlled based on the voltage output of the arduino. This output is equally given to all the motors by the H bridge.


*The proposed system uses Raspberry Pi 3B+ Board along with Arduino Uno. Rpi is the master device and controls the arduino (slave device). It is also the server and serves the user request.*
