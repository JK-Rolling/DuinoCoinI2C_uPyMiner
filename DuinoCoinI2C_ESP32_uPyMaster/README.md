# DuinoCoinI2C_ESP32_uPyMaster
This micropython firmware binary running in ESP32 will act as a host to get jobs from Duino-Coin server, then distribute jobs to connected AVR worker via I2C.

## Steps

1. Load .bin file into ESP32 using web browser or esptool
2. Edit and save secrets.py `SSID`, `PASS`, `USERNAME`, `MINING_KEY`
3. Edit and save settings.py `DUINO_OFFLINE_TESTBENCH_MODE`
4. Reboot ESP32 and start mining!

## Load .bin file into ESP32
1. Download the .bin
2. Connect ESP32 using USB cable with data transfer capability
3. Follow subchapter below for your preferred way. Web browser is the easiest.
   
### Web Browser
1. Visit https://esp.huhn.me/
2. Click `CONNECT` button
3. Select the ESP32 and click `Connect`. You may see something along the line CP2102
4. On row 0x1000, click `SELECT`, then browse to the .bin file downloaded
5. Click `ERASE`
6. Click `PROGRAM`

### esptool
#### Linux
1. (First Time) `pip install esptool`
2. `esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash`. Replace device path to your actual one
3. `esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 DuinoCoinI2C_ESP32_uPyMaster.bin`. Replace device path and .bin path to your actual one

#### Windows
1. (First Time) Download esptool from [esp_tool](https://github.com/espressif/esptool/releases). Example: esptool-v4.7.0-win64.zip
2. (First Time) Extract the .zip then look for esptool or esptool.exe in Windows Explorer
3. Open up a command prompt. You may use `Shift + Right click` in Windows Explorer to pick `Open in Terminal` from menu
4. `esptool.exe --chip esp32 --port COM4 erase_flash`. Replace COM port to your actual one
5. `esptool.exe --chip esp32 --port COM4 write_flash -z 0x1000 DuinoCoinI2C_ESP32_uPyMaster.bin`. Replace COM port and .bin path to your actual one

## Update secrets.py (DO NOT SHARE THIS FILE)
1. Use any micropython IDE. See [here](https://randomnerdtutorials.com/micropython-ides-esp32-esp8266/) for some idea
2. Edit and save. Make sure to use only 2.4GHz WIFI as ESP32 does not support 5GHz WIFI.
   
|Name|Description|
|:-|:-|
|SSID|WIFI Name|
|PASS|WIFI Password|
|USERNAME|Duino-Coin Wallet username|
|MINING_KEY|Duino-Coin mining key|

## Update settings.py
1. Use any micropython IDE. See [here](https://randomnerdtutorials.com/micropython-ides-esp32-esp8266/) for some idea
2. Edit and save. You may use single or dual I2C in testbench mode without actually connecting to Duino-Coin server to validate the mining rig setup.
When the mining rig is ready, change `DUINO_OFFLINE_TESTBENCH_MODE` to `False` to start actual mining

|Name|Description|Default|
|:-|:-|:-|
|I2C0_EN|Enable/disable I2C0|True|
|I2C0_AUTO_SCAN|Scan I2C0 worker address|True|
|I2C0_ADDR|Hardcode worker address. Ignored if I2C0_AUTO_SCAN is True|20,21|
|I2C0_RIG_ID|Worker specific name|None|
|I2C1_EN|Enable/disable I2C1|False|
|I2C1_AUTO_SCAN|Scan I2C1 worker address|True|
|I2C1_ADDR|Hardcode worker address. Ignored if I2C1_AUTO_SCAN is True|14,15|
|I2C1_RIG_ID|Worker specific name|None|
|PERIODIC_REPORT|Print summary report periodically|60|
|DUINO_OFFLINE_TESTBENCH_MODE|Testbench mode|True|
|I2C0_SDA_PIN|I2C0 SDA Pin|21|
|I2C0_SCL_PIN|I2C0 SCL Pin|22|
|I2C0_SCL_FRQ|I2C0 clock frequency|100000|
|I2C1_SDA_PIN|I2C0 SDA Pin|4|
|I2C1_SCL_PIN|I2C0 SCL Pin|5|
|I2C1_SCL_FRQ|I2C0 clock frequency|100000|

## Notes
Current ESP32 is soft limiting worker count to 3 only.

Stay tuned for future update when the limit can be removed and support up to 9 workers!
