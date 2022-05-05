# Humidity Sensor with Fan
<h2> Materials </h2>
1. Raspberry Pi 4 <br>
2. GPIO Extension Board <br>
3. Bread Board <br>
4. DHT11 <br>
5. 10K Resistor <br>
6. L293D <br>
7. Breadboard Power Supply Module <br>
8. 12 Male-Male jumpers <br>
9. 2 Male-Female jumpers <br>

<h2>Set-Up</h2>
<h4>DHT11</h4>
Using Male-Male jumpers: <br>
1. Connect resistor from OUT pin on DHT11 to (+) pin on DHT11 <br>
2. Connect (-) to (-) on right side of breadboard <br>
3. Connect OUT to GPIO4 pin on breadboard <br>
4. Connect (+) to (-) on right side of breadboard <br>

<h4>Breadboard Power Supply Module</h4>
1. Align (+) and (-) pins with (+) and (-) pins on the breadboard <br>
2. Move voltage cover to the OFF position on the right side <br> 
3. Move voltage cover to the 5V position on the left side <br>
4. Connect DC-IN port to a 9V power source <br>

<h4>L293D</h4>
Using Male-Male jumpers: <br>
1. Connect ENABLE to GPIO22 pin on breadboard <br>
2. Connect INPUT1 to GPIO27 <br>
3. Connect OUTPUT1 to left pin on DC Motor <br>
4. Connect GND to (-) on breadboard <br>
5. Connect GND to (-) on breadboard <br>
6. Connect OUTPUT2 to right pin on DC Motor <br>
7. Connect INPUT2 to GPIO17 <br>
8. Connect VS to (+) on the left side of the breadboard <br>
9. Connect VSS to (+) on the right side of the breadboard <br>

<h4>Raspberry Pi 4</h4>
Using Male-Male jumpers: <br>
1. Connect 3.3V pin to (+) on right side of the breadboard <br>
2. Connect GND to (-) on right side of the breadboard <br>

<h2>Relevant Links/Resouces</h2>
https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ <br>
https://www.instructables.com/DC-Motor-Control-With-Raspberry-Pi-and-L293D/ <br>

<h2>Images</h2>


<h2>Instructions</h2>
1. Open "humidity.py" in Python editor <br>
2. Run code in Python editor <br>
3. Use breath or steam to increase humidity <br>
