## CQRobot Ocean TDS Meter Sensor ##
Overview (**Note: I do not own all the images seen here**)

The CQRobot Ocean TDS Meter Sensor is a reliable tool designed to measure Total Dissolved Solids (TDS) in water. This sensor is widely used in various applications such as water quality monitoring, hydroponics, aquariums, and industrial processes.

## Requirements

Before using the CQRobot Ocean TDS Meter Sensor, ensure you have the following:
* [CQRobot Ocean: TDS Meter Sensor](https://www.amazon.com/CQRobot-Ocean-Compatible-Scientific-Laboratory/dp/B08KXRHK7H/)
* [ADS1115 16-Bit Sensor Analog Signal](https://www.amazon.com/CQRobot-Ocean-Acquisition-Conversion-Motherboards/dp/B08KFZ3PVT/)

### Software Requirements

You will need the following software installed on your Raspberry Pi or microcontroller:

- **Python**: Ensure Python is installed on your system. You can download it from the official Python website: [Python.org](https://www.python.org/downloads/)
- **smbus Library**: Install the `smbus` library for I2C communication. You can install it using the package manager on your system. For Raspberry Pi, use the following command:

    ```
    sudo apt-get install python3-smbus
    ```

    If you're using Python 2, replace `python3-smbus` with `python-smbus`.

### Enabling I2C

If you're using a Raspberry Pi or similar microcontroller, you need to enable the I2C interface. Follow the instructions below to enable it.




