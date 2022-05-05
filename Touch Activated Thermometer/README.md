# Touch Activated Thermometer
<h2> Materials </h2>
1. Raspberry Pi 4 <br>
2. GPIO Extension Board <br>
3. Bread Board <br>
4. DHT11 <br>
5. Touch Sensor Module <br>
6. 5 Male-Male jumpers <br>

<h2>Set-Up</h2>
<h4>Touch Sensor</h4>
1. Connect GND wire to (-) on breadboard <br>
2. Connect S wire to GPIO13 pin on breadboard <br>
3. Connect VCC wire to (+) pin on breadboard <br>

<h4>DHT11</h4>
Using Male-Male jumpers: <br>
1. Connect resistor from OUT pin on DHT11 to (+) pin on DHT11 <br>
2. Connect (-) to (-) on right side of breadboard <br>
3. Connect OUT to GPIO4 pin on breadboard <br>
4. Connect (+) to (-) on right side of breadboard <br>

<h4>Raspberry Pi 4</h4>
Using Male-Male jumpers: <br>
1. Connect 3.3V pin to (+) on breadboard <br>
2. Connect GND to (-) on breadboard <br>

<h2>Relevant Links/Resouces</h2>
https://pimylifeup.com/raspberry-pi-humidity-sensor-dht22/ <br>

<h2>Images</h2>



<h2>Instructions</h2>
1. Open "touch-activated-thermometer.py" in Python editor <br>
3. Run code in Python editor <br>
4. Hold touch sensor to read temperature <br>
