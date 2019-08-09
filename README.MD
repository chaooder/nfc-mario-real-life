# Real Life Super Mario Game
Real life Super Mario game with NFC & Raspberry Pi 

## Getting Started

### Hardware Logistics
See `notes/hardware.docx` for hardware and Raspberry Pi setup. This needs to be done before python app can be run.

### Software Installation
* Install raspbian on raspberry pi - https://www.raspberrypi.org/documentation/installation/installing-images/windows.md
* Install required pip packages on raspberry pi, run `pip install -r requirements.txt`.

### Running the Application
Start the Application by running `python app.py` (you can daemonize it with `nohup python app.py &`).

## Resources/Acknowledgements
* Preparing the wiring of PN532 NFC board - https://learn.adafruit.com/adafruit-pn532-rfid-nfc/breakout-wiring
* Free up UART - https://learn.adafruit.com/adafruit-nfc-rfid-on-raspberry-pi/freeing-uart-on-the-pi
* Playing sounds with Raspberri Pi - https://learn.adafruit.com/downloads/pdf/playing-sounds-and-using-buttons-with-raspberry-pi.pdf
* Raspi GPIO usage - https://www.raspberrypi.org/documentation/usage/gpio/

## Built With
* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) - Raspbian Jessie OS
* [Win32DiskImager](http://sourceforge.net/projects/win32diskimager/) - Writing Raspbian Image to SD Card via Windows
* [nfcpy](https://launchpad.net/nfcpy/0.10/0.10.2/+download/nfcpy-0.10.2.tar.gz) - Use of tagtool.py to check NFC tag type
* [MySQL](https://www.mysql.com/) - Database for storing players' data
* [mpg123](https://www.mpg123.de/) - Library for playing mp3 files
* [raspberry-gpio-python](https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/) - For using GPIO pins for lighting up LEDs