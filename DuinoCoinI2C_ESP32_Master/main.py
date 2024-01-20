'''
Quick start guide
1. Load sketch into worker (AVR) using Arduino IDE. Modify DEV_INDEX in .ino accordingly
2. Load ESP32 MircroPython OTA (https://micropython.org/resources/firmware/ESP32_GENERIC-OTA-20231227-v1.22.0.bin)
   Instruction: https://micropython.org/download/ESP32_GENERIC/
   2.1 esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash
   2.2 esptool.py --chip esp32 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x1000 ESP32_GENERIC-OTA-20231227-v1.22.0.bin
3. Setup ESP32 I2C wiring to worker(s) - soft limited to 3 workers in beta version
   Strongly recommended to use Logic-Level-Shifter if the worker operating voltage is 5V and ESP at 3.3V
   I2C Bus0 - SDA (21), SCL (22)
   I2C Bus1 - SDA (4), SCL (5)
   I2C Frequency - 100KHz
   Tested on Nano/Uno
4. Launch Thonny and setup webrepl. User may change 'password' below
   4.1 >>> import webrepl_setup
   4.2 Would you like to (E)nable or (D)isable it running on boot?
       > E
   4.3 New password (4-9 chars): password
   4.4 Confirm password: password
   4.5 Would you like to reboot now? (y/n) y
5. Load all .py and .mpy files into ESP32 using Thonny
6. Edit 'secrets.py' to update WIFI and Duino Wallet credential. Save file
7. Push 'EN' button on ESP32 or Ctrl-D in Thonny to reboot
8. Check the worker are detected and working in testbench mode. Debug step 3 and 5 if something is wrong
9. When testbench mode passed, edit 'settings.py' DUINO_OFFLINE_TESTBENCH_MODE=False
10. Push 'EN' button on ESP32 to start mining
'''

import app