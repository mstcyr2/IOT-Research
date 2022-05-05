# Touch Activated Controller
<h2> Materials </h2>
1. Raspberry Pi 4 <br>
2. GPIO Extension Board <br>
3. Bread Board <br>
4. DHT11 <br>
5. Touch Sensor Module <br>
6. 8 Male-Male jumpers <br>
7. 4 Male-Female jumpers <br>

<h2>Set-Up</h2>
<h4>Touch Sensor</h4>
1. Connect GND wire to (-) on breadboard <br>
2. Connect S wire to GPIO13 pin on breadboard <br>
3. Connect VCC wire to (+) pin on breadboard <br>

<h4>DHT11</h4>
Using Male-Male jumpers: <br>
1. Connect GND to (-) on breadboard <br>
2. Connect 5V to (+) pin on breadboard <br> 
3. Connect VRX to A6 on ADS7830
4. Connect VRY to A7 on ADS7830

<h4>Raspberry Pi 4</h4>
Using Male-Male jumpers: <br>
1. Connect 3.3V pin to (+) on breadboard <br>
2. Connect GND to (-) on breadboard <br>

<h2>Relevant Links/Resouces</h2>
https://www.youtube.com/watch?v=fX225p-Sh58 <br>
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c <br>

<h2>Images</h2>



<h2>Instructions</h2>
1. Open "touch-activated-controller.py" in Python editor <br>
2. Configure i2c interfacing <br>
3. Run code in Python editor <br>
4. Hold touch sensor to read Joystick position <br>
