# Servo Motor Controller
<h2> Materials </h2>
1. Raspberry Pi 4 <br>
2. GPIO Extension Board <br>
3. Bread Board <br>
4. ADS7830 <br>
5. Micro Servo Motor <br>
6. Analog Joystick <br>
7. 11 Male-Male jumpers <br>
8. 4 Male-Female jumpers <br>

<h2>Set-Up</h2>
<h4>Servo Motor</h4>
Using Male-Male jumpers: <br>
1. Connect brown wire to ground on breadboard <br>
2. Connect orange wire to GPIO12 pin on breadboard <br>
3. Connect red wire to 5V pin on breadboard <br>

<h4>Joystick</h4>
Using Male-Female jumpers: <br>
1. Connect GND to (-) on breadboard <br>
2. Connect 5V to (+) pin on breadboard <br> 
3. Connect VRX to A6 on ADS7830
4. Connect VRY to A7 on ADS7830

<h4>ADC ADS7830</h4>
Using Male-Male jumpers: <br>
1. Connect VCC to (+) on breadboard <br>
2. Connect SDA to SDA1 pin on breadboard <br>
3. Connect SCL to SCL1 pin on breadboard <br>
4. Connect GND to (-) on breadboard <br>
5. Connect A6 to VRX on Joystick <br>
6. Connect A7 to VRY on Joystick <br>

<h4>Raspberry Pi 4</h4>
Using Male-Male jumpers: <br>
1. Connect 3.3V pin to (+) on breadboard <br>
2. Connect GND to (-) on breadboard <br>

<h4>Relevant Links/Resouces</h4>
https://www.youtube.com/watch?v=fX225p-Sh58 <br>
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c <br>
https://www.youtube.com/watch?v=_fdwE4EznYo <br>
https://github.com/garyexplains/examples/tree/master/servo <br>

<h4>Images</h4>



<h2>Instructions</h2>
1. Open "controller.py" in Python editor <br>
2. Configure i2c interfacing <br>
3. Run code in Python editor <br>
4. Use the Joystick to move the Servo arm <br>
