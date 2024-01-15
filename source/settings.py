# I2C0
I2C0_EN = True   # Enable/disable I2C0. True
I2C0_AUTO_SCAN = True # scan i2c slave address. False
# if AUTO_SCAN is True, I2C0_ADDR and I2C1_RIG_ID are ignored
# if AUTO_SCAN is False, user to manually provide worker addresses
I2C0_ADDR = "20,21" # comma separated integer. range 8-119. example: "8,9,10"
I2C0_RIG_ID = "" # "rig0A,rig0B" - optional

# I2C1
I2C1_EN = True   # Enable/disable I2C1. True
I2C1_AUTO_SCAN = True # scan i2c slave address. False
# if AUTO_SCAN is True, I2C1_ADDR and I2C1_RIG_ID are ignored
# if AUTO_SCAN is False, user to manually provide worker addresses
I2C1_ADDR = "14,15" # comma separated integer. range 8-119. example: "8,9,10"
I2C1_RIG_ID = "" # "rig1A,rig1B" - optional

# Host
SOC_TIMEOUT = 45 # seconds. 45 - Duino-Coin server connection timeout
AVR_TIMEOUT = 6 # seconds. 6 - worker timeout
ENCODING = "utf-8" # "utf-8"
SEPARATOR = ',' # ','
START_GAP = 5 # seconds. 5 - pause before starting next worker
DUINOIOT_EN = "n" # not implemented yet
PERIODIC_REPORT = 60  # seconds. 60. set 0 to disable reporting
VER = "4.0"
WDT_TIMEOUT = 180000 # milliseconds. 180000. set 0 to disable WDT. WDT feed at PERIODIC_REPORT or 60s (for disabled reporting)
BOOT_DELAY = 3 # seconds. 3
WORKER_FALLOUT_CHECK_PERIOD = 30 # seconds. 30

# Debug
DUINO_OFFLINE_TESTBENCH_MODE = True  # set to False to connect actual Duino-Coin server

# GPIO
LED_PIN = 2 # 2
LED_HEARTBEAT_EN = True # True

'''
VERBOSITY LEVEL
- QUIET
- MINIMAL
- NORMAL
- VERBOSE
- DEBUG
'''
from constant import *
VERBOSITY = MINIMAL  # MINIMAL

I2C_SCAN_COUNT = 3 # 3. used when I2C_AUTO_SCAN enabled
# I2C0
I2C0_BUS_ID = 0 # 0
I2C0_SDA_PIN = 21 # 21
I2C0_SCL_PIN = 22 # 22
I2C0_SCL_FRQ = 100000 # 100000

# I2C1
I2C1_BUS_ID = 1 # 1
I2C1_SDA_PIN = 4 # 4
I2C1_SCL_PIN = 5 # 5
I2C1_SCL_FRQ = 100000 # 100000

I2C_REPEAT_WR = 1 # 1. repeat I2C packet
