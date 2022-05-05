# Servo Motor Motion Detector (Watch Tower)
<h2> Materials </h2>
1. Raspberry Pi 4 <br>
2. GPIO Extension Board <br>
3. Bread Board <br>
4. PIR Motion Sensor <br>
5. Micro Servo Motor <br>
6. 3 Male-Male jumpers <br>
7. 3 Male-Female jumpers <br>

<h2>Set-Up</h2>
<h4>Servo Motor</h4>
Using Male-Male jumpers: <br>
1. Connect brown wire to ground on breadboard <br>
2. Connect orange wire to GPIO12 pin on breadboard <br>
3. Connect red wire to 5V pin on breadboard <br>

<h4>PIR Motion Sensor</h4>
Using Male-Female jumpers: <br>
1. Connect (-) to ground on breadboard <br>
2. Connect (S) to GPIO4 pin on breadboard <br>
3. Connect (+) to 5V pin on breadboard <br> 

<h4>Relevant Links/Resouces</h4>
https://www.youtube.com/watch?v=Tw0mG4YtsZk <br>
https://github.com/Zero-Day-Z/Motion-Sensor <br>
https://www.youtube.com/watch?v=_fdwE4EznYo <br>
https://github.com/garyexplains/examples/tree/master/servo <br>

<h4>Images</h4>
<img src="https://user-images.githubusercontent.com/98985878/164813562-aeead17d-a86d-494d-94c3-9768ef8e345f.png"> <br>
<img src="https://user-images.githubusercontent.com/98985878/164814225-3ef43250-2301-45ea-b63f-80a998802dee.jpg"> <br>


<h2>Instructions</h2>
1. Open "watch_tower.py" in Python editor <br>
2. Enter "sudo pigpiod" into terminal <br>
3. Run code in Python editor <br>
