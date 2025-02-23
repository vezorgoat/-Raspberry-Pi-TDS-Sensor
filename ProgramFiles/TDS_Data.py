import time
import smbus

# Define I2C address and register addresses for the TDS sensor
TDS_ADDRESS = 0x48  # I2C address of the TDS sensor
TDS_CMD_READ = 0x00  # Command to read data from the sensor

# Create an instance of the smbus for I2C communication
bus = smbus.SMBus(1)  # Use bus 1 for Raspberry Pi 3, use 0 for older models
#Reads information from Tds Sensor.
def read_tds_value():
    bus.write_byte(TDS_ADDRESS, TDS_CMD_READ)
    time.sleep(0.5)
    data = bus.read_i2c_block_data(TDS_ADDRESS, 0x00, 2)
    tds_value = (data[0] << 8) | data[1]
    return tds_value

def main():
    try:
        while True:
            tds = read_tds_value()
            print("TDS Value:", tds)
            time.sleep(2)
    except KeyboardInterrupt:
        #Prints For Ctrl C or print force Close!
        print("Exiting...")

if __name__ == "__main__":
    main()
