import time
import smbus

# Define I2C address and register addresses for the TDS sensor
TDS_ADDRESS = 0x48  # I2C address of the TDS sensor
TDS_CMD_READ = 0x00  # Command to read data from the sensor

# Create an instance of the smbus for I2C communication
bus = smbus.SMBus(1)  # Use bus 1 for Raspberry Pi 3, use 0 for older models

def read_tds_value():
    # Send command to request TDS data
    bus.write_byte(TDS_ADDRESS, TDS_CMD_READ)
    # Wait for a short time to allow the sensor to process the request
    time.sleep(0.5)
    # Read 2 bytes of TDS data from the sensor
    data = bus.read_i2c_block_data(TDS_ADDRESS, 0x00, 2)
    # Combine the two bytes into a single integer value
    tds_value = (data[0] << 8) | data[1]
    return tds_value

def main():
    try:
        while True:
            # Read TDS value from the sensor
            tds = read_tds_value()
            # Print the TDS value to the console
            print("TDS Value:", tds)
            # Wait for some time before reading again (adjust as needed)
            time.sleep(2)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("Exiting...")

if __name__ == "__main__":
    main()
