# Fingerprint Catcher
<h2>Description</h2>
This project uses an R307 fingerprint reader to read and validate fingerprints and send images of unauthorized fingerprints to a given email.

<h2> Materials </h2>
1. Raspberry Pi 4 <br>
2. GPIO Extension Board <br>
3. Bread Board <br>
4. R307 Fingerprint Module <br>
5. 4 Male-Male jumpers <br>

<h2>Set-Up</h2>
<h4>Fingerprint Reader</h4>
Using Male-Male jumpers: <br>
1. Connect red wire to 3.3V on breadboard <br>
2. Connect black wire to GND <br>
3. Connect green wire to RXD0 (Pin 10) on breadboard <br>
4. Connect white wire to TXD0 (Pin 8) on breadboard <br>

<h2>Download Libraries</h2>

In the terminal:
```
sudo bash
```
Necessary packages:
```
wget -O - http://apt.pm-codeworks.de/pm-codeworks.de.gpg | apt-key add -
wget http://apt.pm-codeworks.de/pm-codeworks.list -P /etc/apt/sources.list.d/
```
Lastly:
```
exit
```

<h2>Customize Library Files</h2>
Change "/dev/ttyUSB0" to "/dev/ttyS0" in example_enroll.py:

```
sudo nano /usr/share/doc/python-fingerprint/examples/example_enroll.py
```

In "config.txt" add "enable_uart=1":
```
sudo nano /boot/config.txt
```

<h2>Relevant Links/Resouces</h2>
https://tutorials-raspberrypi.com/how-to-use-raspberry-pi-fingerprint-sensor-authentication/<br>

<h2>Images</h2>


<h2>Instructions</h2>
Register an authorized fingerprint:

  ```
  python2 /usr/share/doc/python-fingerprint/examples/example_enroll.py
  ```

Create fingerprint-catcher.py:
  ```
  sudo nano /usr/share/doc/python-fingerprint/fingerprint-catcher.py
  ```

Copy code from https://github.com/mstcyr2/IOT-Research/blob/main/Fingerprint%20Catcher/fingerprint-catcher.py into new file. <br>

Run code:
  ```
  sudo nano /usr/share/doc/python-fingerprint/fingerprint-catcher.py
  ```
Follow instructions in terminal
